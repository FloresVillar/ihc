"""
Tema 17 (Asistente virtual de clinica) - Tarea LEC-LAB04 Parte 2, seccion 6.

Corre el prompt v2 (el mejorado, con la lista cerrada de 5 tareas) contra
DeepSeek real, con las mismas 5 conversaciones usadas con Claude en la
seccion 4 de la Parte 2. Sustituye a Gemini en esta seccion (la cuota
gratuita de Gemini se agoto antes de poder correr las 5 completas).

Es adaptativo: si DeepSeek pide un dato no incluido en el guion original
(nombre, documento, sede, hora), responde con un valor de la lista de
respaldo en vez de quedarse atascado, hasta un maximo de turnos.

Requiere: pip install openai python-dotenv
Usa la DEEPSEEK_CHAT_API_KEY de SkillOpt/.env.example (cuenta de pago).
"""

from dotenv import load_dotenv
load_dotenv("/home/esau/SkillOpt/.env.example")

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_CHAT_API_KEY"],
    base_url=os.environ.get("DEEPSEEK_CHAT_URL", "https://api.deepseek.com/v1"),
)
MODEL = os.environ.get("DEEPSEEK_CHAT_MODEL", "deepseek-chat")

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

CONFIRM_KEYWORDS = (
    "confirm", "queda", "listo", "agendad", "cancelad", "reprogramad", "registrad",
)


def run_adaptive(title, first_msgs, answers, max_turns=8):
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    messages = [{"role": "system", "content": PROMPT_V2}]
    turn = 0
    pending = list(first_msgs)
    last_text = ""
    while turn < max_turns:
        if pending:
            user_msg = pending.pop(0)
        else:
            lt = last_text.lower()
            user_msg = None
            for kw, ans in answers:
                if kw in lt:
                    user_msg = ans
                    break
            if user_msg is None:
                break
        turn += 1
        messages.append({"role": "user", "content": user_msg})
        try:
            resp = client.chat.completions.create(model=MODEL, messages=messages)
            text = resp.choices[0].message.content
        except Exception as e:
            text = f"[ERROR: {e}]"
        messages.append({"role": "assistant", "content": text})
        print(f"\nTurno {turn} (usuario): {user_msg}")
        print(f"Turno {turn} (DeepSeek): {text}")
        last_text = text
        if any(k in text.lower() for k in CONFIRM_KEYWORDS):
            break
    print(f"\n[TOTAL TURNOS: {turn}]")


def run_fixed(title, turns):
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    messages = [{"role": "system", "content": PROMPT_V2}]
    for i, user_msg in enumerate(turns, 1):
        messages.append({"role": "user", "content": user_msg})
        try:
            resp = client.chat.completions.create(model=MODEL, messages=messages)
            text = resp.choices[0].message.content
        except Exception as e:
            text = f"[ERROR: {e}]"
        messages.append({"role": "assistant", "content": text})
        print(f"\nTurno {i} (usuario): {user_msg}")
        print(f"Turno {i} (DeepSeek): {text}")


def main():
    # C1 - usuario estandar (T1+T5)
    run_adaptive(
        "C1 - usuario estandar (T1+T5)",
        ["Hola, quiero una cita", "Cardiología", "El próximo martes"],
        [
            ("nombre completo", "Juan Pérez"),
            ("documento", "12345678"),
            ("cédula", "12345678"),
            ("sede", "San Isidro"),
            ("exacta", "A las 10:00 de la mañana"),
            ("hora", "A las 10:00 de la mañana"),
            ("cobertura", "Particular"),
        ],
    )

    # C2 - usuario tercera edad (T2)
    run_adaptive(
        "C2 - usuario tercera edad (T2)",
        ["Quiero cambiar mi cita", "Rosa Medina", "Para el jueves"],
        [
            ("documento", "45678912"),
            ("cédula", "45678912"),
            ("cobertura", "Particular"),
            ("exacta", "A las 9:00 de la mañana"),
            ("9 o a las 11", "A las 9 de la mañana"),
            ("hora", "A las 9:00 de la mañana"),
        ],
    )

    # C3 - discapacidad visual (T3), un solo turno con todo el dato
    run_fixed(
        "C3 - discapacidad visual, lector de pantalla (T3)",
        ["Necesito cancelar mi cita, folio 04521"],
    )

    # C4 - preguntas fuera de alcance (EHR)
    run_fixed(
        "C4 - preguntas fuera de alcance (EHR)",
        [
            "¿Qué medicamento me recomiendas para la gripe?",
            "¿Cuál es la capital de Francia?",
        ],
    )

    # C5 - ambiguedad (T4)
    run_fixed(
        "C5 - ambiguedad (T4)",
        [
            "Quiero ver a alguien para mi problema",
            "Es algo del corazón",
            "Solo dime el horario por ahora",
        ],
    )


if __name__ == "__main__":
    main()
