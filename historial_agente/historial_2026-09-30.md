# Historial 2026-09-30: Lab 05 (semana_5), pendientes

## Estado

La entrega está en `semana_5/CC451_Lab05_20151445F_Esau_Flores/`, y el zip es `semana_5/CC451_Lab05_20151445F_Esau_Flores.zip` (64 archivos, 15 MB, sin API key). El zip se armó a las 20:29 y **no incluye los cambios posteriores del Doc**.

El reporte está en Google Docs (cuenta uni): [Lab05 - FLORES VILLAR - Reporte HCI](https://docs.google.com/document/d/1afNu1bduSdhwSTInYg6nxsk5B_h2TIQxI4saBvhr6ok/edit). **El Doc es ahora la fuente.** El usuario le cambió el estilo (Times New Roman, viñetas). `semana_5/lab05_FLORES_VILLAR_Reporte_HCI.md` y `Reporte_HCI.pdf` quedaron desactualizados respecto del Doc. No hay que volver a generar el Doc desde el `.md`, porque se perdería el estilo del usuario.

### Capturas de AI Studio (todas en `Capturas/`, registradas en `REGISTRO_CAPTURAS.md`)

- Mesero 1 a 3: Prompt 1, con capturas a/b.
- Mesero 4 a 7: Prompt 2, una captura cada una (mano levantada, carta, cumpleaños y grupo conversando).
- Invidente 1 a 3: Prompt 3, una captura cada una (cruce, andén y pasillo).
- Un primer intento de Mesero 4 a 6 se hizo con la system instruction del P1 por error. Quedó aparte en `semana_5/aistudio_p1_sobre_comensales/`, fuera del zip.
- Todas las pruebas se corrieron en el mismo chat, así que el contexto se fue acumulando. Está anotado en el registro.

### Lo que pide realmente el enunciado (`CC451_Lab05_v2.pdf`)

- Bloques 1 y 2 y los prompts del Bloque 3 **en AI Studio**, con capturas `AIStudio_Pruebas_*`.
- **Script Python con API y TTS** (`asistente_invidente.py`, 6 pts), a partir de "Get Code". El script está hecho y probado, y los audios están en `Scripts/audio/`.
- **No pide** repetir las pruebas por API para comparar. Las capturas `API_Pruebas_*` y las notas "Por API" son un extra nuestro.
- Los prompts base y el Bloque 1 se corrieron **solo por script**, no en AI Studio.
- El reporte debe tener: tabla de evaluación de prompts, análisis de entornos y justificación de usabilidad.

### Cambios ya hechos en el Doc

- El enfoque se invirtió: las matrices salen de AI Studio, y la API se anota como "Por API: …".
- Las celdas de P1, P2 y P3 se reescribieron. La nota del andén pasó a 1 → 5.
- El mapa de entornos ahora cita las respuestas de AI Studio.
- El usuario pegó la nueva versión de "Cómo se hicieron las pruebas".

## Pendientes

1. **Correcciones a mano en el Doc** (el usuario prefiere hacerlas para ahorrar tokens):
   - Tabla del P3, fila del cruce: cambiar `1 → 2` por `1 → 3`.
   - Bajo la tabla del P3: "pero en dos de tres casos se llevó el dato de seguridad." → "pero en el pasillo se llevó el dato de seguridad en las dos vías, y en el cruce por API."
   - "En AI Studio (AIStudio_Pruebas_Invidente_1 a 3) las frases salieron más cortas… hacia la roca." → "Las frases de AI Studio (AIStudio_Pruebas_Invidente_1 a 3) salieron más cortas que por API, de 6 a 12 palabras, y en el andén y el cruce fueron más seguras."
   - "Lo que no queda resuelto": "En el cruce y en el supermercado el modelo detectó el obstáculo…" → "En el supermercado el modelo detectó el exhibidor con el prompt base y lo perdió con el optimizado en las dos vías, y en el cruce le pasó lo mismo con la roca por API".
   - Error al pegar: "(mruce_obstaculo)" → "(mesa_derrame, mesa_ordenada, cruce_obstaculo)", y "deWikimedia" → "de Wikimedia".
2. **Título del reporte:** solo nombra los bloques 2 y 3. Propuestas: el título del enunciado ("Prototipado e inferencia multimodal de experiencias de usuario con Google AI Studio y Gemini API") o "temperatura, mesero robótico y asistente de navegación con Gemma en AI Studio".
3. **Sección "Cómo se hicieron las pruebas":** el enunciado no la pide. Falta que el usuario elija entre moverla al final como anexo (lo recomendado) o dejarla en una sola línea.
4. **Bloque 1 en AI Studio:** dos capturas de la Catedral (`guia/catedral_lima.jpg`, P0 guía, temperatura 0.0 y 1.0). El enunciado pide hacerlo en AI Studio.
5. **Captura de "Get Code"** del chat del P3 (`AIStudio_GetCode_Invidente.png`), como evidencia de que el script parte de ahí.
6. Opcional: agregar a `asistente_invidente.py` una función `analizar_entorno_asistivo()` que siga la estructura de la plantilla.
7. Opcional: decidir si se quitan las capturas `API_Pruebas_*` del zip. No se deben quitar los scripts ni `resultados/`, porque respaldan los prompts base y el Bloque 1.
8. **Al cerrar:** descargar el Doc como PDF y reemplazar `Reporte_HCI.pdf`, volver a armar el zip (sin `*Zone.Identifier`) y revisar que no lleve la API key. Si se quiere, sincronizar el `.md` desde el Doc.
9. **Entrega:** subir el zip en la plataforma del curso. Confirmar con el profesor dónde se entrega.

## Pendientes menores

- La API key viene de `~/matching_pipeline/.env` y no se sabe de qué cuenta es. Conviene crear una propia con la cuenta uni.
- En AI Studio el grounding con Google Search queda activo para Gemma y no se puede apagar.
- La mejora propuesta para el Prompt 3 en dos pasos (primero lista de obstáculos en JSON, después la frase) no está implementada. El falso "Camino libre" en el pasillo se repite en AI Studio y por API.
- `frase_robot` vacía cuando el robot no debe hablar: el P2 no define qué poner (`null`).
