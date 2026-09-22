"""One bar chart per indicator (TCR, CRR, ADL, EHR), comparing providers
(item 5 of the section 8 proposal)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

CHARTS_DIR = Path(__file__).parent / "charts"

_TITLES = {
    "TCR": "TCR — Tasa de éxito de la tarea (%)",
    "CRR": "CRR — Tasa de aclaración (%, proxy vía juez LLM)",
    "ADL": "ADL — Turnos por tarea exitosa",
    "EHR": "EHR — Manejo de excepciones (%)",
}


def generate(results: list[dict]) -> list[Path]:
    CHARTS_DIR.mkdir(exist_ok=True)
    written = []
    for metric, title in _TITLES.items():
        providers = [r["provider"] for r in results if r[metric] is not None]
        values = [r[metric] for r in results if r[metric] is not None]
        if not providers:
            continue
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.bar(providers, values, color="#4C72B0")
        ax.set_title(title)
        ax.set_ylabel(metric)
        for i, v in enumerate(values):
            ax.text(i, v, f"{v:.1f}", ha="center", va="bottom")
        fig.tight_layout()
        out_path = CHARTS_DIR / f"{metric.lower()}.png"
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        written.append(out_path)
    return written
