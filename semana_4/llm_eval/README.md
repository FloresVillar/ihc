# llm_eval — automatización propuesta en la sección 8

Implementa los 5 puntos de la propuesta de automatización (Parte 2, sección 8
del documento de la tarea), generalizando lo que antes eran 4 scripts de un
solo uso en `../evidencia_manual/`:

1. **Parametrizar modelo/API key por proveedor, correr en un solo lote** →
   `providers.py` (un adaptador por vendor, interfaz común `.chat()`) +
   `run_eval.py --providers deepseek gemini claude openai`.
2. **Guardar cada respuesta con modelo, conversación y turno como llaves** →
   `storage.py`, escribe a `data/runs.csv` (una fila por turno).
3. **Clasificar automáticamente cada turno para TCR/EHR** → `metrics.py`,
   por patrones de texto (sin releer transcripciones a mano).
4. **LLM "juez" para detectar eventos de CRR** → `judge.py` (ver su
   docstring: es un proxy, no una medición real de confusión del usuario,
   porque nuestros "usuarios" de prueba están guionizados).
5. **Graficar TCR/CRR/ADL/EHR por proveedor** → `charts.py`, un PNG por
   indicador en `charts/`.

## Uso

```bash
make install          # dependencias
make run-deepseek     # el único proveedor con credenciales probadas end-to-end
make run              # deepseek + gemini (gemini puede fallar si su cuota gratuita está agotada)
make charts           # regenera los PNG a partir de data/runs.csv sin re-correr las conversaciones
make clean
```

Añadir Claude o ChatGPT: exportar `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` en el
entorno y agregar `claude` / `openai` a `--providers`. Los adaptadores ya
están escritos en `providers.py`; no se han probado por falta de esas keys.

## Qué NO hace (limitaciones honestas)

- El TCR aquí se mide **por escenario** (4 escenarios de tarea), no por las
  "5 tareas asignadas" que se cuentan a mano en el documento — son números
  relacionados pero no idénticos (ver docstring de `metrics.py`).
- El CRR es un proxy de un juez LLM leyendo solo la respuesta del asistente,
  no una reacción real de un usuario confundido.
- Las respuestas adaptativas (`answer_bank` en `scenarios.py`) son un banco
  fijo de valores; si un proveedor pide un dato no contemplado ahí, el
  script simplemente se detiene en ese turno (igual que en las corridas
  manuales, pero ahora es un límite documentado del pipeline, no un bug
  descubierto a mitad de una corrida).
