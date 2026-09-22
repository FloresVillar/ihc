"""LLM-as-judge for CRR (item 4 of the section 8 proposal).

Honesty note: the assignment's CRR method assumes a live user who reacts
with "no entiendo" / "puedes repetir" to a confusing reply. Our test
"users" are scripted, so they never do that. This judge is a proxy: it
reads only the assistant's reply (no ground truth about whether a real
user was confused) and predicts whether an average patient would likely
need to ask for clarification — unexplained jargon, ambiguity, or asking
for something already given. It is a heuristic stand-in, not a real CRR
measurement; report it as such.
"""

from __future__ import annotations

from llm_eval.providers import get_provider

_JUDGE_PROMPT = (
    "Eres un evaluador de UX conversacional. Lee la siguiente respuesta de un "
    "asistente de citas médicas y decide si un paciente promedio, al leerla, "
    "probablemente necesitaría pedir una aclaración (por jerga no explicada, "
    "ambigüedad, o por pedir un dato que el paciente ya dio antes). "
    "Responde en una sola línea con el formato: SI|NO - <razón breve>.\n\n"
    "Respuesta del asistente:\n{text}"
)


def judge_crr(text: str, judge_provider: str = "deepseek") -> tuple[bool, str]:
    provider = get_provider(judge_provider)
    verdict = provider.chat(
        system_prompt="Responde siempre en el formato pedido, sin texto adicional.",
        history=[{"role": "user", "content": _JUDGE_PROMPT.format(text=text)}],
    )
    flagged = verdict.strip().upper().startswith("SI")
    reason = verdict.split("-", 1)[1].strip() if "-" in verdict else verdict.strip()
    return flagged, reason
