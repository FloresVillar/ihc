"""
asistente_invidente.py — CC451 Lab 05, Bloque 3 (Assistive Vision)

Recibe una o más imágenes (cuadros de la cámara de unas gafas inteligentes),
consulta un modelo multimodal Gemma con el Prompt 3, valida que la respuesta
cumpla las reglas de interfaz por voz y la reproduce con TTS.

Uso:
    export GEMINI_API_KEY="..."
    python asistente_invidente.py imagenes/entornos/cruce_obstaculo.png
    python asistente_invidente.py imagenes/entornos/*.png --sin-audio
    python asistente_invidente.py foto.jpg --backend ollama      # Gemma local

Dependencias: pip install google-genai gTTS   (opcional: pyttsx3, ollama)
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from functools import lru_cache
from pathlib import Path

# ============================================================
# CONFIGURACIÓN
# ============================================================
RAIZ = Path(__file__).resolve().parent
RUTA_PROMPT = RAIZ.parent / "Prompts" / "Prompt3_Asistente_Visión.json"

MODELO_GEMINI = "gemma-4-26b-a4b-it"   # Gemini API (Google AI Studio)
MODELO_OLLAMA = "gemma4:26b"           # mismo modelo servido por Ollama
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://10.20.4.3:11434")

MAX_PALABRAS = 25
REINTENTOS_SERVIDOR = 3     # errores 5xx y 429 de la API son transitorios
RESPUESTA_IMAGEN_NO_CLARA = "Imagen poco clara, detente un momento."

MIME_POR_EXTENSION = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}


# ============================================================
# PROMPT
# ============================================================
def cargar_prompt(ruta: Path = RUTA_PROMPT) -> dict:
    """Lee un prompt exportado (JSON) y une la system instruction en un texto."""
    datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    instruccion = datos["system_instruction"]
    if isinstance(instruccion, list):
        datos["system_instruction"] = "\n".join(instruccion)
    return datos


# ============================================================
# CONSULTA AL MODELO
# ============================================================
@lru_cache(maxsize=1)
def _cliente_gemini():
    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Falta GEMINI_API_KEY. Créala en aistudio.google.com/apikey y ejecuta: "
            'export GEMINI_API_KEY="tu_clave"'
        )
    return genai.Client(api_key=api_key)


def _generar_con_reintentos(cliente, **kwargs):
    """generate_content con espera creciente ante errores transitorios (5xx, 429)."""
    from google.genai import errors

    for intento in range(REINTENTOS_SERVIDOR + 1):
        try:
            return cliente.models.generate_content(**kwargs)
        except errors.APIError as e:
            transitorio = isinstance(e, errors.ServerError) or e.code == 429
            if not transitorio or intento == REINTENTOS_SERVIDOR:
                raise
            espera = 2 ** intento * 3
            print(f"[aviso] API respondió {e.code}; reintento {intento + 1} en {espera} s.",
                  file=sys.stderr)
            time.sleep(espera)


def _consultar_gemini(ruta_imagen, system_instruction, pregunta, modelo,
                      temperatura, json_schema=None) -> str:
    from google.genai import errors, types

    cliente = _cliente_gemini()
    # La imagen va en línea (bytes) en vez de client.files.upload(): para un
    # flujo de cuadros continuos evita una subida previa por cada cuadro.
    mime = MIME_POR_EXTENSION.get(Path(ruta_imagen).suffix.lower(), "image/jpeg")
    imagen = types.Part.from_bytes(data=Path(ruta_imagen).read_bytes(), mime_type=mime)

    extra = {}
    if json_schema:
        extra = {"response_mime_type": "application/json",
                 "response_json_schema": json_schema}

    try:
        respuesta = _generar_con_reintentos(
            cliente,
            model=modelo,
            contents=[imagen, pregunta],
            config=types.GenerateContentConfig(
                system_instruction=system_instruction or None,
                temperature=temperatura,
                **extra,
            ),
        )
    except errors.ClientError as e:
        if e.code != 400 or not (system_instruction or json_schema):
            raise
        # Algunos modelos Gemma en la Gemini API no aceptan system_instruction
        # ni modo JSON. Se reintenta con las reglas al inicio del mensaje; el
        # formato JSON queda garantizado por la propia instrucción.
        print(f"[aviso] {modelo} rechazó la configuración ({e.message}); "
              "reintentando con las reglas dentro del mensaje.", file=sys.stderr)
        texto = f"{system_instruction}\n\n{pregunta}" if system_instruction else pregunta
        respuesta = _generar_con_reintentos(
            cliente,
            model=modelo,
            contents=[imagen, texto],
            config=types.GenerateContentConfig(temperature=temperatura),
        )
    return respuesta.text or ""


def _consultar_ollama(ruta_imagen, system_instruction, pregunta, modelo,
                      temperatura, json_schema=None) -> str:
    import ollama

    mensajes = []
    if system_instruction:
        mensajes.append({"role": "system", "content": system_instruction})
    mensajes.append({"role": "user", "content": pregunta, "images": [str(ruta_imagen)]})

    respuesta = ollama.Client(host=OLLAMA_HOST).chat(
        model=modelo,
        messages=mensajes,
        format=json_schema,
        options={"temperature": temperatura},
    )
    return respuesta["message"]["content"]


def consultar_modelo(ruta_imagen, system_instruction, pregunta, *, backend="gemini",
                     modelo=None, temperatura=0.2, json_schema=None) -> str:
    """Envía imagen + prompt al backend elegido y devuelve el texto de respuesta."""
    if not Path(ruta_imagen).is_file():
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")
    if backend == "gemini":
        return _consultar_gemini(ruta_imagen, system_instruction, pregunta,
                                 modelo or MODELO_GEMINI, temperatura, json_schema)
    if backend == "ollama":
        return _consultar_ollama(ruta_imagen, system_instruction, pregunta,
                                 modelo or MODELO_OLLAMA, temperatura, json_schema)
    raise ValueError(f"Backend desconocido: {backend}")


# ============================================================
# REGLAS DE INTERFAZ POR VOZ
# ============================================================
def contar_palabras(texto: str) -> int:
    return len(re.findall(r"\w+", texto))


def limpiar_para_voz(texto: str) -> str:
    """Quita markdown, viñetas y emojis que el TTS leería como ruido."""
    texto = re.sub(r"[*_#`>|~]", "", texto)
    texto = re.sub(r"^\s*[-•]\s*", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"[^\w\s.,;:¿?¡!()'\"-]", "", texto)
    return re.sub(r"\s+", " ", texto).strip()


def recortar(texto: str, maximo: int = MAX_PALABRAS) -> str:
    """Recorta a `maximo` palabras, cerrando en la última frase o cláusula completa."""
    if contar_palabras(texto) <= maximo:
        return texto
    corte = " ".join(texto.split()[:maximo])
    for separadores in (".!?", ",;:"):
        fin = max(corte.rfind(s) for s in separadores)
        if fin > len(corte) // 3:
            return corte[:fin].rstrip() + "."
    return corte + "."


def obtener_indicacion(ruta_imagen, prompt: dict, *, backend="gemini", modelo=None,
                       temperatura=0.2) -> dict:
    """Consulta el modelo y aplica las reglas del Prompt 3 a la respuesta.

    Si la respuesta supera MAX_PALABRAS se pide una reescritura una sola vez
    (cada reintento suma latencia) y, si sigue larga, se recorta.
    """
    inicio = time.perf_counter()
    crudo = consultar_modelo(ruta_imagen, prompt["system_instruction"],
                             prompt["prompt_usuario"], backend=backend,
                             modelo=modelo, temperatura=temperatura)
    texto = limpiar_para_voz(crudo)
    reintento = False

    if contar_palabras(texto) > MAX_PALABRAS:
        reintento = True
        pregunta = (f"{prompt['prompt_usuario']}\n\nTu respuesta anterior tuvo "
                    f"{contar_palabras(texto)} palabras: \"{texto}\". Reescríbela en "
                    f"máximo {MAX_PALABRAS} palabras, empezando por el riesgo.")
        texto = limpiar_para_voz(consultar_modelo(
            ruta_imagen, prompt["system_instruction"], pregunta, backend=backend,
            modelo=modelo, temperatura=temperatura))

    recortado = contar_palabras(texto) > MAX_PALABRAS
    texto = recortar(texto) if recortado else texto
    if not texto:
        texto = RESPUESTA_IMAGEN_NO_CLARA

    return {
        "imagen": str(ruta_imagen),
        "texto": texto,
        "palabras": contar_palabras(texto),
        "reintento": reintento,
        "recortado": recortado,
        "latencia_s": round(time.perf_counter() - inicio, 2),
        "respuesta_cruda": crudo,
    }


# ============================================================
# SALIDA DE AUDIO (TTS)
# ============================================================
def _reproducir(ruta_audio: Path) -> bool:
    reproductores = [
        ["mpg123", "-q"],
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet"],
        ["afplay"],                      # macOS
    ]
    for comando in reproductores:
        if shutil.which(comando[0]):
            subprocess.run(comando + [str(ruta_audio)], check=False)
            return True
    if sys.platform.startswith("win"):
        os.startfile(ruta_audio)         # noqa: S606 — reproductor por defecto
        return True
    return False


def hablar(texto: str, ruta_salida: Path, reproducir: bool = True) -> Path | None:
    """Convierte el texto a voz: gTTS (en línea, voz natural) o pyttsx3 (sin red)."""
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    try:
        from gtts import gTTS

        mp3 = ruta_salida.with_suffix(".mp3")
        gTTS(texto, lang="es", tld="com.mx").save(str(mp3))
        if reproducir and not _reproducir(mp3):
            print(f"[aviso] No hay reproductor de audio; audio guardado en {mp3}",
                  file=sys.stderr)
        return mp3
    except Exception as e:  # sin gTTS o sin red: se usa el motor local
        print(f"[aviso] gTTS no disponible ({e}); usando pyttsx3.", file=sys.stderr)

    try:
        import pyttsx3

        motor = pyttsx3.init()
        motor.setProperty("rate", 175)
        wav = ruta_salida.with_suffix(".wav")
        motor.save_to_file(texto, str(wav))
        if reproducir:
            motor.say(texto)
        motor.runAndWait()
        return wav
    except Exception as e:
        print(f"[aviso] Sin motor TTS disponible ({e}); solo salida de texto.",
              file=sys.stderr)
        return None


# ============================================================
# EJECUCIÓN
# ============================================================
def main() -> int:
    parser = argparse.ArgumentParser(description="Asistente de navegación por voz")
    parser.add_argument("imagenes", nargs="+", type=Path, help="Imagen(es) a analizar")
    parser.add_argument("--backend", choices=["gemini", "ollama"], default="gemini")
    parser.add_argument("--modelo", help="Sobrescribe el modelo por defecto del backend")
    parser.add_argument("--temperatura", type=float, default=None,
                        help="Por defecto, la del Prompt 3 (0.2)")
    parser.add_argument("--sin-audio", action="store_true", help="No genera ni reproduce voz")
    parser.add_argument("--no-reproducir", action="store_true",
                        help="Genera el audio pero no lo reproduce")
    parser.add_argument("--carpeta-audio", type=Path, default=RAIZ / "audio")
    parser.add_argument("--json", type=Path, help="Guarda los resultados en este archivo")
    args = parser.parse_args()

    prompt = cargar_prompt()
    temperatura = (args.temperatura if args.temperatura is not None
                   else prompt["run_settings"]["temperature"])
    resultados = []

    for ruta in args.imagenes:
        try:
            r = obtener_indicacion(ruta, prompt, backend=args.backend,
                                   modelo=args.modelo, temperatura=temperatura)
        except Exception as e:
            print(f"[ERROR] {ruta}: {e}", file=sys.stderr)
            continue

        marca = " (reintento)" if r["reintento"] else ""
        marca += " (recortado)" if r["recortado"] else ""
        print(f"{ruta.name} | {r['palabras']} palabras | {r['latencia_s']} s{marca}")
        print(f"  >> {r['texto']}")

        if not args.sin_audio:
            audio = hablar(r["texto"], args.carpeta_audio / ruta.stem,
                           reproducir=not args.no_reproducir)
            r["audio"] = str(audio) if audio else None
        resultados.append(r)

    if args.json:
        args.json.write_text(json.dumps(resultados, ensure_ascii=False, indent=2),
                             encoding="utf-8")
    return 0 if resultados else 1


if __name__ == "__main__":
    sys.exit(main())
