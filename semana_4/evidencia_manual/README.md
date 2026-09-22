# Evidencia manual (Parte 1 sección 5, Parte 2 sección 6)

Scripts ad hoc usados para llenar las secciones del documento que piden una
conversación registrada con un segundo proveedor de LLM (Gemini y luego
DeepSeek, cuando Gemini agotó su cuota gratuita). Cada uno corre contra la
API real del proveedor, una sola vez, y su salida se copió a mano al `.txt`
correspondiente y al documento.

Estos scripts son de un solo uso (no hay dos iguales: cada uno tiene su
propio guion de conversación embebido). El pipeline reusable y automatizado
que sí generaliza esto a cualquier proveedor está en `../llm_eval/`.

| Script | Salida | Usado en |
|---|---|---|
| `gemini_test_fijo.py` | `gemini_output_guion_fijo.txt` | Parte 2, sección 6 (intento con guion fijo, reveló el problema de comparar así) |
| `gemini_test_adaptativo.py` | `gemini_output_adaptativo.txt` | Parte 2, sección 6 (reintento adaptativo, cuota agotada a medio camino) |
| `deepseek_test_parte1.py` | `deepseek_output_parte1.txt` | Parte 1, sección 5 |
| `deepseek_test_parte2.py` | `deepseek_output_parte2.txt` | Parte 2, sección 6 (versión final, sustituye a Gemini) |
