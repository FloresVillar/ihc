"""Automatic TCR / ADL / EHR / CRR computation from stored run records
(item 3 of the section 8 proposal) — no reading transcripts by hand.

Note on TCR's denominator: the doc's hand-computed sections use "5 tareas
asignadas" (T1-T5, with T5 riding along inside C1's confirmation message).
This automated version scores per *scenario* instead (4 task-scenarios:
C1-C3, C5), since that's what can be checked mechanically from the stored
text without a human deciding "does this count as T5 too?". The two numbers
are related but not identical — say which one you're citing.
"""

from __future__ import annotations

from collections import defaultdict

from llm_eval.scenarios import CONFIRM_PATTERNS, OUT_OF_SCOPE_HANDLED_PATTERNS, SCENARIOS
from llm_eval.storage import read_runs

_SCENARIO_BY_ID = {s.scenario_id: s for s in SCENARIOS}


def _is_task_completed(assistant_texts: list[str]) -> bool:
    return any(p in t.lower() for t in assistant_texts for p in CONFIRM_PATTERNS)


def _out_of_scope_handled_count(assistant_texts: list[str]) -> int:
    return sum(1 for t in assistant_texts if any(p in t.lower() for p in OUT_OF_SCOPE_HANDLED_PATTERNS))


def compute_metrics(provider: str) -> dict:
    rows = [r for r in read_runs() if r["provider"] == provider]
    by_scenario: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_scenario[r["scenario_id"]].append(r)

    completed_scenarios = 0
    task_scenarios = 0
    turns_in_completed = 0
    ehr_handled = 0
    ehr_total = 0
    crr_flags = []

    for scenario_id, scenario_rows in by_scenario.items():
        scenario = _SCENARIO_BY_ID.get(scenario_id)
        if scenario is None:
            continue
        assistant_rows = [r for r in scenario_rows if r["role"] == "assistant"]
        assistant_texts = [r["text"] for r in assistant_rows]
        turns = max((int(r["turn"]) for r in scenario_rows), default=0)

        for r in assistant_rows:
            if r["crr_flag"] not in ("", None):
                crr_flags.append(int(r["crr_flag"]))

        if scenario.category == "task":
            task_scenarios += 1
            if _is_task_completed(assistant_texts):
                completed_scenarios += 1
                turns_in_completed += turns
        elif scenario.category == "out_of_scope":
            ehr_total += len(assistant_texts)
            ehr_handled += _out_of_scope_handled_count(assistant_texts)

    tcr = (completed_scenarios / task_scenarios * 100) if task_scenarios else None
    adl = (turns_in_completed / completed_scenarios) if completed_scenarios else None
    ehr = (ehr_handled / ehr_total * 100) if ehr_total else None
    crr = (sum(crr_flags) / len(crr_flags) * 100) if crr_flags else None

    return {
        "provider": provider,
        "TCR": tcr,
        "ADL": adl,
        "EHR": ehr,
        "CRR": crr,
        "task_scenarios_completed": f"{completed_scenarios}/{task_scenarios}",
    }


def compute_all(providers: list[str]) -> list[dict]:
    return [compute_metrics(p) for p in providers]
