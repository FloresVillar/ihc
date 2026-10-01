# Registro de pruebas en Google AI Studio

Cuenta: efloresv@uni.pe · Fecha: 2026-09-30 · Modelo: gemma-4-26b-a4b-it

Las capturas `API_Pruebas_*` son las mismas pruebas ejecutadas por la Gemini API desde `Scripts/laboratorio_prompts.py`; sirven para comparar la salida de AI Studio con la del script.

## AIStudio_Pruebas_Mesero_1 — Prompt 1, mesas/mesa_derrame.png

- **Capturas:** `AIStudio_Pruebas_Mesero_1a_entrada.png` (imagen, mensaje y system instruction cargados; modelo pensando) y `AIStudio_Pruebas_Mesero_1b_respuesta.png` (respuesta).
- **Configuración:** temperature 0.2 · Thinking level High · Structured outputs desactivado · Grounding with Google Search activo (AI Studio lo mantiene para Gemma: "To access without Search grounding, please use the API directly").
- **Hora:** 3:33 p. m. · 2 580 tokens en total · título asignado por AI Studio: "Evaluación de Mesa con Incidencia".
- **Respuesta:**

```json
{
  "razonamiento": {
    "inventario": ["vasos", "vasos de papel", "platos", "restos de comida", "servilletas", "derrames"],
    "estado_consumo": "Platos con restos de comida y vasos con hielo o restos de líquido indican que el consumo ha terminado.",
    "senales_humanas": "No se observan comensales en la imagen.",
    "incidencias": "Derrame de líquido sobre la superficie de la mesa."
  },
  "estado_mesa": "incidencia",
  "intervenir": "Sí",
  "urgencia": "media",
  "accion": "limpiar derrame y retirar vajilla",
  "momento": "ahora",
  "justificacion": "Se ha detectado un derrame de líquido en la mesa y la vajilla se encuentra terminada.",
  "confianza": 0.9
}
```

- **Observaciones:**
  - JSON válido y con todas las claves del esquema, sin usar Structured outputs: la instrucción de formato basta.
  - La decisión coincide con la ejecución por API (`API_Pruebas_Mesero_P1_2.png`): incidencia, intervenir Sí, momento ahora, confianza 0.9. Solo cambia la redacción de los campos de texto, lo esperable con temperature 0.2.
  - Detecta las dos condiciones de intervención del paso 6 a la vez: incidencia (a) y vajilla terminada (b).
  - La system instruction se pegó en su forma de lista JSON (`["Eres…", "Recibes…"]`) y el modelo la interpretó igual.

## AIStudio_Pruebas_Mesero_2 — Prompt 1, mesas/mesa_ordenada.png

- **Capturas:** `AIStudio_Pruebas_Mesero_2a_entrada.png` y `AIStudio_Pruebas_Mesero_2b_respuesta.png`.
- **Configuración:** igual que Mesero 1 (temperature 0.2 · Thinking High · sin Structured outputs · Grounding activo).
- **Hora:** 3:39 p. m. · 4 440 tokens acumulados. Se ejecutó en el mismo chat de la prueba 1 ("Evaluación de Mesa con Incidencia"), así que la imagen y la respuesta anteriores estaban en el contexto.
- **Respuesta:**

```json
{
  "razonamiento": {
    "inventario": ["platos", "copas de vino", "vasos de agua", "cubiertos", "servilletas", "flores"],
    "estado_consumo": "Los platos contienen comida y las copas tienen vino y agua; la mesa está en proceso de consumo.",
    "senales_humanas": "No se observan comensales en la imagen.",
    "incidencias": "ninguna"
  },
  "estado_mesa": "en_consumo",
  "intervenir": "No",
  "urgencia": "ninguna",
  "accion": "ninguna",
  "momento": "siguiente_ronda",
  "justificacion": "La mesa se encuentra en proceso de consumo con comida y bebidas presentes, y no se detectan incidencias ni señales de llamada.",
  "confianza": 0.95
}
```

- **Observaciones:**
  - JSON válido y completo. Misma decisión que la API (`API_Pruebas_Mesero_P1_3.png`): en_consumo, intervenir No, siguiente_ronda. La confianza sube de 0.9 a 0.95.
  - La mesa está servida y sin comensales; lo correcto es no acercarse, y el modelo no confunde "hay vajilla" con "hay que retirar vajilla".
  - Pese a compartir chat con la prueba 1, la respuesta no arrastra nada de la mesa anterior (no menciona derrames).
  - Matiz: clasifica como en_consumo, aunque la comida parece recién servida y sin tocar. La decisión es la misma, pero "limpia_preparada" o una categoría "servida" describiría mejor la escena; es un posible ajuste de las categorías del paso 5.

## AIStudio_Pruebas_Mesero_3 — Prompt 1, mesas/mesa_comensales_conversando.jpg

- **Capturas:** `AIStudio_Pruebas_Mesero_3a_entrada.png` y `AIStudio_Pruebas_Mesero_3b_respuesta.png`.
- **Configuración:** igual que Mesero 1 y 2.
- **Hora:** 3:42 p. m. · 6 595 tokens acumulados, en el mismo chat de las pruebas 1 y 2.
- **Respuesta:**

```json
{
  "razonamiento": {
    "inventario": ["platos", "copas de vino", "vasos", "botella de agua", "cesta de pan", "cubiertos", "servilletas"],
    "estado_consumo": "Hay platos vacíos, pero las copas de vino aún contienen líquido, indicando que la mesa sigue en uso.",
    "senales_humanas": "Los comensales están conversando y celebrando de forma animada; no hay señales de llamada al personal.",
    "incidencias": "ninguna"
  },
  "estado_mesa": "en_consumo",
  "intervenir": "No",
  "urgencia": "ninguna",
  "accion": "retirar vajilla",
  "momento": "diferido",
  "justificacion": "Los comensales están en medio de una celebración/conversación sin señales de llamada, por lo que no se debe interrumpir aunque haya platos terminados.",
  "confianza": 0.95
}
```

- **Observaciones:**
  - Es el caso que justifica el Chain-of-Thought: hay platos vacíos (condición b del paso 6), pero el paso 3 detecta conversación activa y el modelo aplica la regla de no interrumpir. Sin esa regla, un criterio solo visual ("platos vacíos → retirar") habría hecho que el robot interrumpa.
  - Separa el qué del cuándo tal como se diseñó: `intervenir: No` ahora, pero deja `accion: retirar vajilla` con `momento: diferido` para cuando termine la conversación.
  - La justificación cita casi textualmente la regla del prompt ("no se debe interrumpir aunque haya platos terminados"): el razonamiento es trazable a la instrucción.
  - Coincide con la API (`API_Pruebas_Mesero_P1_1.png`: en_consumo, No, diferido, 0.9). En la API `accion` fue "ninguna"; aquí el modelo anticipa la acción diferida, que es más útil para el robot.
