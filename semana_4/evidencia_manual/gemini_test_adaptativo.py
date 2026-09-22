"""
Tema 17 (Asistente virtual de clinica) - Tarea LEC-LAB04 Parte 2.

Version adaptativa: en vez de un guion de usuario fijo, responde segun lo
que Gemini realmente pregunta (nombre, documento, fecha, sede, hora), hasta
que la tarea se confirma o se llega al maximo de turnos. Asi la comparacion
de ADL/TCR contra Claude es mas justa que con un guion fijo (ver
gemini_test_fijo.py y la seccion 6 del doc, donde el guion fijo dejo 3 de
5 conversaciones incompletas solo por el desfase de guion, no por una falla
real del modelo).

Requiere: pip install google-genai python-dotenv
Usa la GEMINI_API_KEY del proyecto matching_pipeline (ihc/matching_pipeline/.env).

Nota: la cuota gratuita del modelo usado es de 20 solicitudes/dia; si se
agota a mitad de la corrida, las conversaciones restantes quedan con error
429 RESOURCE_EXHAUSTED (no es una falla del asistente, sino del plan
gratuito de la API).
"""

from dotenv import load_dotenv
load_dotenv("/home/esau/ihc/matching_pipeline/.env")

import os
import time
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-flash-latest"

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


def send(chat, msg, retries=3):
    for _ in range(retries):
        try:
            return chat.send_message(msg).text
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                time.sleep(8)
                continue
            return f"[ERROR: {e}]"
    return "[ERROR: max retries]"


def run_adaptive(title, first_msgs, answers, max_turns=7):
    """
    answers: lista de (palabra_clave, respuesta) evaluada en orden sobre la
    ULTIMA respuesta de Gemini (en minusculas). Usa la primera que matchee.
    OJO (bug conocido, dejado a proposito para documentar el hallazgo): si
    dos preguntas distintas comparten la palabra clave (p. ej. "hora" en
    "horario de atencion" y en "confirmas ese horario?"), se repite la
    misma respuesta -> en la corrida real esto paso en C1 turnos 6 y 7.
    """
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    chat = client.chats.create(
        model=MODEL, config=types.GenerateContentConfig(system_instruction=PROMPT_V2)
    )
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
        text = send(chat, user_msg)
        print(f"\nTurno {turn} (usuario): {user_msg}")
        print(f"Turno {turn} (Gemini): {text}")
        last_text = text
        if any(k in text.lower() for k in CONFIRM_KEYWORDS):
            break
    print(f"\n[TOTAL TURNOS: {turn}]")


def main():
    run_adaptive(
        "C1 - usuario estandar (T1+T5) [ADAPTATIVO]",
        ["Hola, quiero una cita", "Cardiología"],
        [
            ("nombre completo", "Juan Pérez"),
            ("documento", "12345678"),
            ("cédula", "12345678"),
            ("fecha", "El próximo martes"),
            ("sede", "San Isidro"),
            ("hora", "En la mañana"),
        ],
    )

    run_adaptive(
        "C2 - usuario tercera edad (T2) [ADAPTATIVO]",
        ["Quiero cambiar mi cita"],
        [
            ("documento", "45678912"),
            ("cédula", "45678912"),
            ("nombre", "Rosa Medina"),
            ("fecha", "Para el jueves"),
            ("hora", "En la mañana"),
        ],
    )

    run_adaptive(
        "C3 - discapacidad visual (T3) [ADAPTATIVO]",
        ["Necesito cancelar mi cita, folio 04521"],
        [
            ("nombre", "Elmer Izarra"),
            ("documento", "78912345"),
            ("cédula", "78912345"),
        ],
    )

    print(f"\n{'='*70}\nC4 - preguntas fuera de alcance (EHR) [reintento turno 1]\n{'='*70}")
    chat4 = client.chats.create(
        model=MODEL, config=types.GenerateContentConfig(system_instruction=PROMPT_V2)
    )
    t1 = send(chat4, "¿Qué medicamento me recomiendas para la gripe?")
    print(f"\nTurno 1 (usuario): ¿Qué medicamento me recomiendas para la gripe?")
    print(f"Turno 1 (Gemini): {t1}")
    t2 = send(chat4, "¿Cuál es la capital de Francia?")
    print(f"\nTurno 2 (usuario): ¿Cuál es la capital de Francia?")
    print(f"Turno 2 (Gemini): {t2}")

    print(f"\n{'='*70}\nC5 - ambiguedad (T4) [reintento turno 1]\n{'='*70}")
    chat5 = client.chats.create(
        model=MODEL, config=types.GenerateContentConfig(system_instruction=PROMPT_V2)
    )
    t1 = send(chat5, "Quiero ver a alguien para mi problema")
    print(f"\nTurno 1 (usuario): Quiero ver a alguien para mi problema")
    print(f"Turno 1 (Gemini): {t1}")
    t2 = send(chat5, "Es algo del corazón")
    print(f"\nTurno 2 (usuario): Es algo del corazón")
    print(f"Turno 2 (Gemini): {t2}")
    t3 = send(chat5, "Solo dime el horario por ahora")
    print(f"\nTurno 3 (usuario): Solo dime el horario por ahora")
    print(f"Turno 3 (Gemini): {t3}")


if __name__ == "__main__":
    main()
