# Historial 2026-09-30: Lab 05 (semana_5), pendientes

## Estado

La entrega está armada en `semana_5/CC451_Lab05_20151445F_Esau_Flores/` y comprimida en `semana_5/CC451_Lab05_20151445F_Esau_Flores.zip` (57 archivos, 12 MB). Ya contiene:

- los 3 prompts en `Prompts/`;
- los scripts `asistente_invidente.py` (con TTS gTTS/pyttsx3 y reintentos ante errores 5xx) y `laboratorio_prompts.py`;
- imágenes con sus créditos, resultados y audios en `Scripts/`;
- `Reporte_HCI.pdf`;
- en `Capturas/`: las capturas por API de todas las pruebas y las de AI Studio de Mesero 1 a 3, más `REGISTRO_CAPTURAS.md`.

El reporte también está en Google Docs (cuenta uni): [Lab05 - FLORES VILLAR - Reporte HCI](https://docs.google.com/document/d/1afNu1bduSdhwSTInYg6nxsk5B_h2TIQxI4saBvhr6ok/edit). El fuente es `semana_5/lab05_FLORES_VILLAR_Reporte_HCI.md`.

## Lo que falta

1. **Capturas de AI Studio que faltan** (las toma el usuario con efloresv@uni.pe, en un chat nuevo por prompt, modelo gemma-4-26b-a4b-it). Los textos para pegar están en `semana_5/aistudio_pegar/`.

   | Captura | Prompt | Temperatura | Imagen (en `Scripts/imagenes/`) |
   |---|---|---|---|
   | AIStudio_Pruebas_Mesero_4 | P2 | 0.3 | `comensales/comensal_mano_levantada.jpg` |
   | AIStudio_Pruebas_Mesero_5 | P2 | 0.3 | `comensales/comensal_indeciso_carta.jpg` |
   | AIStudio_Pruebas_Mesero_6 | P2 | 0.3 | `comensales/grupo_celebrando.jpg` |
   | AIStudio_Pruebas_Invidente_1 | P3 | 0.2 | `entornos/cruce_obstaculo.png` |
   | AIStudio_Pruebas_Invidente_2 | P3 | 0.2 | `entornos/anden_metro.jpg` |
   | AIStudio_Pruebas_Invidente_3 | P3 | 0.2 | `entornos/pasillo_supermercado.jpg` |

   Opcional: 2 capturas de la Catedral (`guia/catedral_lima.jpg`, prompt P0 guía) a temperatura 0.0 y 1.0 para el Bloque 1.

2. **Cuando lleguen las capturas** (tarea del agente):
   - copiarlas a `Capturas/` como `AIStudio_Pruebas_<caso>_<n>a_entrada.png` / `..._<n>b_respuesta.png`;
   - agregar cada prueba a `Capturas/REGISTRO_CAPTURAS.md` con configuración, respuesta transcrita y comparación con la API;
   - actualizar las matrices de P2 y P3 del reporte con lo de AI Studio, en el `.md`, en el Google Doc (mismo doc, mismo enlace) y en el `Reporte_HCI.pdf`;
   - volver a armar el zip y revisar que no incluya la API key.

3. **Entrega:** subir el zip en la plataforma del curso. El PDF del lab no dice dónde; confirmar con el profesor.

## Pendientes menores

- La API key usada viene de `~/matching_pipeline/.env` y no se sabe de qué cuenta es. Se sugirió crear una propia en `aistudio.google.com/apikey` con la cuenta uni.
- En AI Studio el "Grounding with Google Search" queda activo para Gemma y no se puede apagar. Está anotado en el reporte como diferencia frente a la API.
- Mejora propuesta en el reporte, no implementada: hacer el Prompt 3 en dos pasos (primero lista de obstáculos en JSON, después la frase de voz), porque el prompt optimizado pierde obstáculos que el base sí detecta (roca del cruce, exhibidor del supermercado).
