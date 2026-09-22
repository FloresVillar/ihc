"""
Tema 17 (Asistente virtual de clinica) - Tarea LEC-LAB04 Parte 1, seccion 5.

Corre el prompt v1 (el original de la Parte 1, no el mejorado v2) contra
DeepSeek real (API compatible con OpenAI), con los mismos 4 casos usados
con Claude en la seccion 4 del documento: contexto (5 turnos), ambiguedad,
peticion de aclaracion, y el caso de error de fecha.

Requiere: pip install openai python-dotenv
Usa la DEEPSEEK_CHAT_API_KEY de SkillOpt/.env.example (cuenta de pago,
$5 de credito segun el usuario).
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

PROMPT_V1 = (
    "Eres el asistente virtual de la Clínica San Rafael. Tu función es: agendar, "
    "reprogramar o cancelar citas médicas; informar sobre especialidades disponibles, "
    "horarios y ubicación de sedes; recordar al paciente qué debe traer a su cita "
    "(documento, orden médica, resultados previos). No das diagnósticos médicos ni "
    "recomendaciones de tratamiento: ante cualquier síntoma o consulta clínica, "
    "derivas a agendar cita con el especialista correspondiente. Si falta información "
    "para completar una acción (especialidad, sede, fecha), se pregunta explícitamente "
    "antes de continuar. Se mantiene un tono cordial y profesional, confirmando "
    "siempre los datos antes de cerrar la acción."
)


def run_conversation(title, turns):
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    messages = [{"role": "system", "content": PROMPT_V1}]
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
    run_conversation(
        "a) Contexto (5 turnos)",
        [
            "Hola, quiero una cita",
            "Para cardiología",
            "¿Cuánto cuesta la consulta?",
            "Ya, y ¿tienen sede en San Isidro?",
            "Ok, entonces la cita de cardiología, ¿qué días hay?",
        ],
    )
    run_conversation(
        "b) Ambigüedad",
        ["Necesito una cita con el especialista de siempre"],
    )
    run_conversation(
        "c) Petición de aclaración",
        ["Quiero cambiar mi cita"],
    )
    run_conversation(
        "Caso de error deliberado",
        ["Cita para el 31 de febrero"],
    )


if __name__ == "__main__":
    main()
