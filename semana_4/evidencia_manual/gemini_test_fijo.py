"""
Tema 17 (Asistente virtual de clinica) - Tarea LEC-LAB04 Parte 2.

Corre el prompt v2 contra Gemini real (API), con un guion de turnos FIJO
(identico al usado con Claude). Sirve para ver donde el guion fijo no es
justo: si Gemini pide datos que el guion no anticipa (nombre, documento),
la tarea queda incompleta aunque el modelo no haya "fallado".

Requiere: pip install google-genai python-dotenv
Usa la GEMINI_API_KEY del proyecto matching_pipeline (ihc/matching_pipeline/.env).
"""

from dotenv import load_dotenv
load_dotenv("/home/esau/ihc/matching_pipeline/.env")

import os
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

CONVERSATIONS = {
    "C1 - usuario estandar (T1+T5)": [
        "Hola, quiero una cita",
        "Cardiología",
        "El próximo martes",
    ],
    "C2 - usuario tercera edad (T2)": [
        "Quiero cambiar mi cita",
        "Rosa Medina",
        "Para el jueves",
    ],
    "C3 - discapacidad visual, lector de pantalla (T3)": [
        "Necesito cancelar mi cita, folio 04521",
    ],
    "C4 - preguntas fuera de alcance (EHR)": [
        "¿Qué medicamento me recomiendas para la gripe?",
        "¿Cuál es la capital de Francia?",
    ],
    "C5 - ambiguedad (T4)": [
        "Quiero ver a alguien para mi problema",
        "Es algo del corazón",
        "Solo dime el horario por ahora",
    ],
}


def main():
    for title, turns in CONVERSATIONS.items():
        print(f"\n{'='*70}\n{title}\n{'='*70}")
        chat = client.chats.create(
            model=MODEL,
            config=types.GenerateContentConfig(system_instruction=PROMPT_V2),
        )
        for i, user_msg in enumerate(turns, 1):
            try:
                resp = chat.send_message(user_msg)
                text = resp.text
            except Exception as e:
                text = f"[ERROR: {e}]"
            print(f"\nTurno {i} (usuario): {user_msg}")
            print(f"Turno {i} (Gemini): {text}")


if __name__ == "__main__":
    main()
