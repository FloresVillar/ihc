"""
laboratorio_prompts.py — CC451 Lab 05, Bloques 1 a 3

Ejecuta los experimentos del laboratorio con Gemma y guarda las respuestas
que alimentan las matrices de evaluación del reporte:

    temperatura  Bloque 1: guía turístico con T = 0.0 y T = 1.0 (3 corridas c/u)
    mesero       Bloque 2: Prompt 1 y Prompt 2, base vs optimizado
    invidente    Bloque 3: Prompt 3, base vs optimizado

Uso:
    export GEMINI_API_KEY="..."
    python laboratorio_prompts.py temperatura
    python laboratorio_prompts.py mesero invidente
    python laboratorio_prompts.py todo --backend ollama

Las imágenes se leen de imagenes/{guia,mesas,comensales,entornos}/ y los
resultados se escriben en resultados/ (JSON crudo + matriz en Markdown con las
columnas de calificación y justificación listas para completar).
"""

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

from asistente_invidente import (RAIZ, cargar_prompt, consultar_modelo,
                                 contar_palabras, obtener_indicacion)

PROMPTS = RAIZ.parent / "Prompts"
IMAGENES = RAIZ / "imagenes"
RESULTADOS = RAIZ / "resultados"
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp"}

GUIA_SYSTEM = ("Actúa como un guía turístico experto. Identifica el lugar y explica "
               "brevemente su valor arquitectónico e histórico.")
GUIA_PREGUNTA = "¿Qué lugar es este?"
GUIA_TEMPERATURAS = (0.0, 1.0)
GUIA_REPETICIONES = 3


def imagenes_de(carpeta: str) -> list[Path]:
    return sorted(p for p in (IMAGENES / carpeta).glob("*") if p.suffix.lower() in EXTENSIONES)


def parsear_json(texto: str):
    """Devuelve el objeto JSON de la respuesta, tolerando bloques ```json."""
    limpio = texto.strip().removeprefix("```json").removeprefix("```").removesuffix("```")
    try:
        return json.loads(limpio)
    except json.JSONDecodeError:
        inicio, fin = limpio.find("{"), limpio.rfind("}")
        if inicio != -1 and fin > inicio:
            try:
                return json.loads(limpio[inicio:fin + 1])
            except json.JSONDecodeError:
                pass
    return None


def similitud_jaccard(a: str, b: str) -> float:
    """Proporción de palabras compartidas: 1.0 = misma respuesta, 0.0 = nada en común."""
    pa, pb = set(a.lower().split()), set(b.lower().split())
    return round(len(pa & pb) / len(pa | pb), 2) if pa | pb else 1.0


def resumir(texto: str, limite: int = 180) -> str:
    texto = " ".join(texto.split()).replace("|", "/")
    return texto if len(texto) <= limite else texto[:limite].rstrip() + "…"


def guardar(nombre: str, datos, markdown: str) -> None:
    RESULTADOS.mkdir(exist_ok=True)
    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    (RESULTADOS / f"{nombre}_{marca}.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    (RESULTADOS / f"{nombre}_{marca}.md").write_text(markdown, encoding="utf-8")
    print(f"  -> resultados/{nombre}_{marca}.json y .md")


# ============================================================
# BLOQUE 1 — TEMPERATURA
# ============================================================
def experimento_temperatura(backend, modelo):
    imagenes = imagenes_de("guia")
    if not imagenes:
        print("[omitido] temperatura: agrega una foto en imagenes/guia/")
        return
    datos, filas = [], []
    for img in imagenes:
        for t in GUIA_TEMPERATURAS:
            corridas = []
            for _ in range(GUIA_REPETICIONES):
                corridas.append(consultar_modelo(img, GUIA_SYSTEM, GUIA_PREGUNTA,
                                                 backend=backend, modelo=modelo, temperatura=t))
            pares = [(i, j) for i in range(len(corridas)) for j in range(i + 1, len(corridas))]
            sim = round(sum(similitud_jaccard(corridas[i], corridas[j]) for i, j in pares)
                        / len(pares), 2)
            datos.append({"imagen": img.name, "temperatura": t,
                          "similitud_media": sim, "respuestas": corridas})
            filas.append(f"| {img.name} | {t} | {sim} | "
                         f"{round(sum(map(contar_palabras, corridas)) / len(corridas))} | "
                         f"{resumir(corridas[0])} |")
            print(f"  {img.name} T={t}: similitud entre corridas {sim}")

    md = ["# Bloque 1 — Temperatura", "",
          f"System instruction: _{GUIA_SYSTEM}_", "",
          "| Imagen | Temperatura | Similitud entre corridas (Jaccard) | Palabras promedio | Respuesta (corrida 1) |",
          "|---|---|---|---|---|", *filas]
    guardar("temperatura", datos, "\n".join(md) + "\n")


# ============================================================
# BLOQUES 2 Y 3 — BASE VS OPTIMIZADO
# ============================================================
def comparar_prompt(archivo: str, carpeta: str, backend, modelo, es_json: bool):
    prompt = cargar_prompt(PROMPTS / archivo)
    imagenes = imagenes_de(carpeta)
    if not imagenes:
        print(f"[omitido] {prompt['id']}: no hay imágenes en imagenes/{carpeta}/")
        return None
    t = prompt["run_settings"]["temperature"]
    esquema = prompt.get("response_json_schema") if es_json else None
    filas = []

    for img in imagenes:
        # Base: solo la pregunta ingenua, sin system instruction, a la misma
        # temperatura para aislar el efecto del diseño del prompt.
        inicio = time.perf_counter()
        base = consultar_modelo(img, None, prompt["prompt_base"],
                                backend=backend, modelo=modelo, temperatura=t)
        lat_base = round(time.perf_counter() - inicio, 2)

        if prompt["id"] == "P3":
            r = obtener_indicacion(img, prompt, backend=backend, modelo=modelo, temperatura=t)
            optimizado, lat_opt = r["texto"], r["latencia_s"]
            metricas = {"palabras": r["palabras"], "cumple_25": r["palabras"] <= 25,
                        "reintento": r["reintento"], "recortado": r["recortado"]}
        else:
            inicio = time.perf_counter()
            optimizado = consultar_modelo(img, prompt["system_instruction"],
                                          prompt["prompt_usuario"], backend=backend,
                                          modelo=modelo, temperatura=t, json_schema=esquema)
            lat_opt = round(time.perf_counter() - inicio, 2)
            obj = parsear_json(optimizado)
            faltantes = [k for k in esquema["required"] if not obj or k not in obj]
            metricas = {"json_valido": obj is not None, "claves_faltantes": faltantes}
            if obj:
                optimizado = obj

        filas.append({"imagen": img.name,
                      "base": {"respuesta": base, "palabras": contar_palabras(base),
                               "latencia_s": lat_base},
                      "optimizado": {"respuesta": optimizado, "latencia_s": lat_opt, **metricas}})
        print(f"  {prompt['id']} {img.name}: {metricas}")
    return prompt, filas


def matriz_markdown(prompt: dict, filas: list) -> str:
    md = [f"# {prompt['id']} — {prompt['nombre']}", "",
          f"Prompt base: _\"{prompt['prompt_base']}\"_", "",
          "| Imagen | Prompt base | Prompt optimizado | Métricas | Calificación (1-5) | Justificación (HCI/UX) |",
          "|---|---|---|---|---|---|"]
    for f in filas:
        opt = f["optimizado"]
        resp = opt["respuesta"]
        if isinstance(resp, dict):   # P1/P2: se muestran los campos que decide el sistema
            claves = ["estado_mesa", "intervenir", "momento", "situacion",
                      "accion_robot", "frase_robot", "justificacion"]
            resp = "; ".join(f"{k}: {resp[k]}" for k in claves if k in resp)
        metricas = {k: v for k, v in opt.items() if k not in ("respuesta",)}
        md.append(f"| {f['imagen']} | {resumir(f['base']['respuesta'])} "
                  f"({f['base']['palabras']} palabras) | {resumir(str(resp), 260)} | "
                  f"{resumir(json.dumps(metricas, ensure_ascii=False), 200)} |  |  |")
    return "\n".join(md) + "\n"


def experimento_prompts(nombre, casos, backend, modelo):
    datos, md = {}, []
    for archivo, carpeta, es_json in casos:
        salida = comparar_prompt(archivo, carpeta, backend, modelo, es_json)
        if salida:
            prompt, filas = salida
            datos[prompt["id"]] = filas
            md.append(matriz_markdown(prompt, filas))
    if datos:
        guardar(nombre, datos, "\n".join(md))


EXPERIMENTOS = {
    "temperatura": lambda b, m: experimento_temperatura(b, m),
    "mesero": lambda b, m: experimento_prompts("mesero", [
        ("Prompt1_Mesero_Estructurado.json", "mesas", True),
        ("Prompt2_Emociones_JSON.json", "comensales", True),
    ], b, m),
    "invidente": lambda b, m: experimento_prompts("invidente", [
        ("Prompt3_Asistente_Visión.json", "entornos", False),
    ], b, m),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Experimentos del Lab 05")
    parser.add_argument("experimentos", nargs="+", choices=[*EXPERIMENTOS, "todo"])
    parser.add_argument("--backend", choices=["gemini", "ollama"], default="gemini")
    parser.add_argument("--modelo", help="Sobrescribe el modelo por defecto del backend")
    args = parser.parse_args()

    elegidos = list(EXPERIMENTOS) if "todo" in args.experimentos else args.experimentos
    for nombre in elegidos:
        print(f"== {nombre}")
        try:
            EXPERIMENTOS[nombre](args.backend, args.modelo)
        except Exception as e:
            print(f"[ERROR] {nombre}: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
