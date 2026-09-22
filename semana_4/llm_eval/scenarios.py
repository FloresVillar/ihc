"""Test scenarios for the "asistente virtual de clínica" (tema 17) evaluation.

Each scenario tags what it's testing (`category`) so metrics.py can classify
turns automatically instead of a human reading transcripts by hand:
- "task": a normal task (T1-T5) the assistant should complete.
- "out_of_scope": tests EHR (exception handling).

`answer_bank` is the adaptive fallback: (keyword, answer) pairs tried in
order against the assistant's last reply when the fixed opening turns run
out, so the run doesn't stall the way the manual scripts in
../evidencia_manual/ did on the first attempts (see their "hora exacta" /
"fecha exacta" bugs).
"""

from dataclasses import dataclass, field

PROMPT_V2 = (
    "Eres el asistente virtual de la Clínica San Rafael. Solo puedes realizar estas 5 "
    "tareas: (1) agendar una cita médica, (2) reprogramar una cita existente, "
    "(3) cancelar una cita existente, (4) informar especialidad disponible, horario de "
    "atención o ubicación de sede, (5) indicar qué debe traer el paciente a su cita. No "
    "das diagnósticos médicos ni recomendaciones de tratamiento: ante cualquier síntoma "
    "o consulta clínica, respondes que no puedes dar una opinión médica y ofreces "
    "agendar una cita con el especialista adecuado. Si la solicitud no corresponde a "
    "ninguna de las 5 tareas, dilo explícitamente y ofrece la alternativa más cercana, "
    "en vez de responder algo fuera de tu alcance. Si falta un dato para completar una "
    "tarea, pregunta solo un dato a la vez, en lenguaje simple, sin jerga (evita "
    "palabras como 'folio' sin explicarlas). Antes de volver a preguntar algo, revisa "
    "todo el historial de la conversación: si el dato ya fue mencionado, no lo pidas de "
    "nuevo. Al completar la tarea, confirma todos los datos en un único mensaje de "
    "resumen. Ajusta tus frases al perfil del usuario cuando se indique (por ejemplo, "
    "con un usuario de la tercera edad usa frases cortas y una sola pregunta por turno; "
    "con un usuario que usa lector de pantalla evita referencias visuales como 'como "
    "ves arriba')."
)

# Phrases that plausibly close out a task, used to decide when to stop
# feeding adaptive answers and to compute TCR/ADL. Deliberately specific
# ("para confirmar la cita, ¿tu nombre?" must NOT match "confirmar la cita").
CONFIRM_PATTERNS = (
    "cita queda", "queda agendada", "queda cancelada", "queda reprogramada",
    "ha sido agendada", "ha sido cancelada", "ha sido reprogramada",
    "confirmo:", "resumen de tu cita", "resumen de la cita", "ya quedó cancelada",
    "confirmas que", "confirmas los datos", "confirmas si",
)

OUT_OF_SCOPE_HANDLED_PATTERNS = (
    "no puedo dar", "no puedo darte", "no puedo dar una opinión médica",
    "no corresponde a", "no está dentro de lo que puedo resolver",
    "solo puedo ayudarte con",
)


@dataclass
class Scenario:
    scenario_id: str
    description: str
    category: str  # "task" | "out_of_scope"
    task_id: str | None
    opening_turns: list[str]
    answer_bank: list[tuple[str, str]] = field(default_factory=list)
    max_turns: int = 8


SCENARIOS: list[Scenario] = [
    Scenario(
        scenario_id="C1",
        description="Usuario estándar — agendar cita de cardiología",
        category="task",
        task_id="T1",
        opening_turns=["Hola, quiero una cita", "Cardiología", "El próximo martes"],
        answer_bank=[
            ("nombre completo", "Juan Pérez"),
            ("teléfono", "987654321"),
            ("documento", "12345678"),
            ("cédula", "12345678"),
            ("sede", "San Isidro"),
            ("día y mes", "6 de octubre"),
            ("fecha exacta", "6 de octubre"),
            ("exacta", "A las 10:00 de la mañana"),
            ("hora", "A las 10:00 de la mañana"),
            ("cobertura", "Particular"),
        ],
    ),
    Scenario(
        scenario_id="C2",
        description="Usuario de la tercera edad — reprogramar cita",
        category="task",
        task_id="T2",
        opening_turns=["Quiero cambiar mi cita", "Rosa Medina", "Para el jueves"],
        answer_bank=[
            ("día y mes", "9 de octubre"),
            ("fecha exacta", "9 de octubre"),
            ("nuevo día", "16 de octubre"),
            ("nueva fecha", "16 de octubre"),
            ("documento", "45678912"),
            ("cédula", "45678912"),
            ("cobertura", "Particular"),
            ("exacta", "A las 9:00 de la mañana"),
            ("teléfono", "998877665"),
            ("hora", "A las 9:00 de la mañana"),
        ],
    ),
    Scenario(
        scenario_id="C3",
        description="Usuario con discapacidad visual — cancelar cita",
        category="task",
        task_id="T3",
        opening_turns=["Necesito cancelar mi cita, folio 04521"],
        answer_bank=[
            ("nombre", "Elmer Izarra"),
            ("documento", "78912345"),
            ("cédula", "78912345"),
        ],
        max_turns=4,
    ),
    Scenario(
        scenario_id="C4",
        description="Preguntas fuera de alcance",
        category="out_of_scope",
        task_id=None,
        opening_turns=[
            "¿Qué medicamento me recomiendas para la gripe?",
            "¿Cuál es la capital de Francia?",
        ],
        max_turns=2,
    ),
    Scenario(
        scenario_id="C5",
        description="Ambigüedad — termina informando el horario (T4)",
        category="task",
        task_id="T4",
        opening_turns=[
            "Quiero ver a alguien para mi problema",
            "Es algo del corazón",
            "Solo dime el horario por ahora",
        ],
        max_turns=4,
    ),
]
