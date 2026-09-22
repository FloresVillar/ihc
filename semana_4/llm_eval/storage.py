"""Structured storage for run records, keyed by provider + scenario + turn
(item 2 of the section 8 proposal). CSV instead of a real DB: it's the
simplest format that's also a spreadsheet, which is what the assignment
itself asks to graph from.
"""

from __future__ import annotations

import csv
import time
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
RUNS_CSV = DATA_DIR / "runs.csv"

FIELDS = ["provider", "scenario_id", "category", "task_id", "turn", "role", "text", "crr_flag", "ts"]


def append_turn(provider: str, scenario_id: str, category: str, task_id: str | None,
                 turn: int, role: str, text: str, crr_flag: bool | None = None) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    is_new = not RUNS_CSV.exists()
    with RUNS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow({
            "provider": provider,
            "scenario_id": scenario_id,
            "category": category,
            "task_id": task_id or "",
            "turn": turn,
            "role": role,
            "text": text,
            "crr_flag": "" if crr_flag is None else int(crr_flag),
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        })


def read_runs() -> list[dict]:
    if not RUNS_CSV.exists():
        return []
    with RUNS_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def clear_runs() -> None:
    if RUNS_CSV.exists():
        RUNS_CSV.unlink()
