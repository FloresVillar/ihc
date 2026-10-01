"""Debate de la Parte 2 (Lab05) contra una IA, un turno a la vez.

Uso: python3 debate.py {gemini|deepseek} "mensaje del usuario"
Cada proveedor tiene su historial (historial_<proveedor>.json) y comparten
prompt_sistema.txt. Credenciales: las mismas de semana_4/llm_eval/providers.py.
"""
import json, sys
from pathlib import Path

from dotenv import dotenv_values

HERE = Path(__file__).parent
SYSTEM = (HERE / "prompt_sistema.txt").read_text()
GEMINI_MODELS = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-flash-lite-latest"]


def gemini(hist):
    from google import genai
    from google.genai import types, errors
    client = genai.Client(api_key=dotenv_values("/home/esau/ihc/matching_pipeline/.env")["GEMINI_API_KEY"])
    contents = [types.Content(role="user" if h["role"] == "user" else "model",
                              parts=[types.Part(text=h["content"])]) for h in hist]
    for model in GEMINI_MODELS:
        try:
            r = client.models.generate_content(model=model, contents=contents,
                config=types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0.7))
            return r.model_version or model, r.text
        except (errors.ServerError, errors.ClientError) as e:
            print(f"[{model}: {e.code}, probando el siguiente]", file=sys.stderr)
    raise SystemExit("Gemini no disponible")


def deepseek(hist):
    from openai import OpenAI
    env = dotenv_values("/home/esau/SkillOpt/.env.example")
    client = OpenAI(api_key=env["DEEPSEEK_CHAT_API_KEY"],
                    base_url=env.get("DEEPSEEK_CHAT_URL", "https://api.deepseek.com/v1"))
    r = client.chat.completions.create(model=env.get("DEEPSEEK_CHAT_MODEL", "deepseek-chat"),
        temperature=0.7, messages=[{"role": "system", "content": SYSTEM}, *hist])
    return r.model, r.choices[0].message.content


provider, msg = sys.argv[1], sys.argv[2]
path = HERE / f"historial_{provider}.json"
hist = json.loads(path.read_text()) if path.exists() else []
hist.append({"role": "user", "content": msg})
model, text = {"gemini": gemini, "deepseek": deepseek}[provider](hist)
hist.append({"role": "assistant", "content": text, "model": model})
path.write_text(json.dumps(hist, ensure_ascii=False, indent=2))
print(f"[{provider} / {model}]\n\n{text}")
