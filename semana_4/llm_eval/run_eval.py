"""CLI entrypoint: runs the 5 scenarios against one or more providers, stores
every turn, judges CRR, computes metrics and writes the comparison charts.

Usage:
    python -m llm_eval.run_eval --providers deepseek gemini
    python -m llm_eval.run_eval --providers deepseek --no-judge --clear
"""

from __future__ import annotations

import argparse

from llm_eval import charts, storage
from llm_eval.judge import judge_crr
from llm_eval.metrics import compute_all
from llm_eval.providers import PROVIDERS, get_provider
from llm_eval.scenarios import PROMPT_V2, SCENARIOS


def run_scenario(provider, provider_name: str, scenario, judge_provider: str | None) -> None:
    history: list[dict] = []
    pending = list(scenario.opening_turns)
    last_text = ""
    turn = 0
    while turn < scenario.max_turns:
        if pending:
            user_msg = pending.pop(0)
        else:
            lt = last_text.lower()
            user_msg = next((ans for kw, ans in scenario.answer_bank if kw in lt), None)
            if user_msg is None:
                break
        turn += 1
        history.append({"role": "user", "content": user_msg})
        storage.append_turn(provider_name, scenario.scenario_id, scenario.category,
                             scenario.task_id, turn, "user", user_msg)

        try:
            text = provider.chat(PROMPT_V2, history)
        except Exception as e:
            text = f"[ERROR: {e}]"
        history.append({"role": "assistant", "content": text})

        crr_flag = None
        if judge_provider and not text.startswith("[ERROR"):
            try:
                crr_flag, _reason = judge_crr(text, judge_provider)
            except Exception:
                crr_flag = None
        storage.append_turn(provider_name, scenario.scenario_id, scenario.category,
                             scenario.task_id, turn, "assistant", text, crr_flag)

        last_text = text
        if any(p in text.lower() for p in _confirm_patterns()):
            break


def _confirm_patterns():
    from llm_eval.scenarios import CONFIRM_PATTERNS
    return CONFIRM_PATTERNS


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--providers", nargs="+", default=["deepseek"], choices=list(PROVIDERS))
    parser.add_argument("--judge-provider", default="deepseek", help="'' to disable CRR judging")
    parser.add_argument("--clear", action="store_true", help="wipe data/runs.csv before running")
    args = parser.parse_args()

    if args.clear:
        storage.clear_runs()

    judge_provider = args.judge_provider or None
    ran = []
    for name in args.providers:
        try:
            provider = get_provider(name)
        except Exception as e:
            print(f"[SKIP] {name}: {e}")
            continue
        print(f"=== {name} ===")
        for scenario in SCENARIOS:
            print(f"  -> {scenario.scenario_id}: {scenario.description}")
            run_scenario(provider, name, scenario, judge_provider)
        ran.append(name)

    if not ran:
        print("Ningún proveedor pudo correr (revisa las API keys). Nada que graficar.")
        return

    results = compute_all(ran)
    print("\n=== Métricas ===")
    for r in results:
        print(r)

    written = charts.generate(results)
    print("\nGráficos escritos:")
    for path in written:
        print(f"  {path}")


if __name__ == "__main__":
    main()
