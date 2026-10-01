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

## AIStudio_Pruebas_Invidente_1 a 3 — Prompt 3 (Assistive Vision)

- **Capturas:** una por prueba, con la imagen, el mensaje y la respuesta en el mismo cuadro: `AIStudio_Pruebas_Invidente_1.png` (cruce con rocas), `AIStudio_Pruebas_Invidente_2.png` (andén) y `AIStudio_Pruebas_Invidente_3.png` (pasillo de supermercado).
- **Configuración:** system instruction del Prompt 3 · temperature 0.2 · Thinking level High · sin Structured outputs · Grounding with Google Search activo.
- **Mensaje:** "Cuadro actual de la cámara de las gafas. Dame la indicación de navegación urgente."
- **Contexto:** las tres se corrieron en el mismo chat que las pruebas anteriores ("Análisis de Mesa y Pedido"), cambiando la system instruction. Los tokens acumulados pasan de 11 933 a 14 727, así que el modelo tenía en el contexto las imágenes y respuestas previas. Ninguna respuesta arrastra nada de ellas.

| Prueba | Imagen | Hora | Respuesta AI Studio | Palabras | Respuesta API (`API_Pruebas_Invidente_*`) |
|---|---|---|---|---|---|
| 1 | `entornos/cruce_obstaculo.png` | 8:13 p. m. | "Alto. Rocas al frente a dos metros. Detente." | 8 | "Alto. Rocas grandes en el camino a tus 12 y a la derecha. Rodéalas por la izquierda." (17) |
| 2 | `entornos/anden_metro.jpg` | 8:14 p. m. | "Alto. Tren en movimiento a tus 9, a un metro. Aléjate del borde." | 12 | "Alto. Tren en movimiento a tu izquierda, muy cerca. Espera." (10) |
| 3 | `entornos/pasillo_supermercado.jpg` | 8:15 p. m. | "Camino libre. Pasillo despejado al frente." | 6 | "Camino libre. Pasillo de supermercado con estantes a tus 9 y a tus 3. Sigue recto." (16) |

- **Observaciones:**
  - Las tres cumplen el formato de voz: empiezan con la palabra de alerta o con "Camino libre", tienen entre 6 y 12 palabras (dentro del rango ideal de 8 a 15, salvo la 3) y no traen markdown.
  - **Cruce:** mejor que por API. No da una orientación equivocada ni propone rodear por un lado que también tiene piedras; da la distancia y una acción segura ("Detente"). Sigue sin decir por dónde pasar, pero ante la duda detenerse es lo correcto.
  - **Andén:** mejor que por API. Usa la notación horaria ("a tus 9"), da la distancia y añade "Aléjate del borde", que era justo lo que le faltaba a la corrida por API.
  - **Pasillo:** repite el falso "Camino libre". El exhibidor azul que está en el centro del pasillo, a pocos metros, no aparece, igual que por API. Confirma que el fallo no depende de la vía ni de la redacción: el prompt optimizado, al pedir brevedad y priorizar riesgos dinámicos, deja pasar obstáculos estáticos en medio del camino. Refuerza la propuesta de hacer el Prompt 3 en dos pasos (lista de obstáculos en JSON y después la frase).
  - Con temperatura 0.2 las frases cambian respecto de la API en las tres pruebas, pero la decisión de fondo (alerta o camino libre) es la misma.

## AIStudio_Pruebas_Mesero_4 a 7 — Prompt 2 (diagnóstico empático)

- **Capturas:** una por prueba, con imagen, mensaje y respuesta en el mismo cuadro: `AIStudio_Pruebas_Mesero_4.png` (mano levantada), `_5.png` (comensal con la carta), `_6.png` (cumpleaños) y `_7.png` (grupo conversando, prueba adicional).
- **Configuración:** system instruction del Prompt 2 ("Eres el módulo de interacción social…") · temperature 0.3 · Thinking level High · sin Structured outputs · Grounding with Google Search activo.
- **Mensaje:** "Fotografía de la mesa tomada por el robot. Analiza a los comensales y devuelve solo el JSON."
- **Contexto:** se corrieron en el mismo chat que las pruebas anteriores (17 122 a 22 446 tokens acumulados). Un primer intento con estas imágenes se hizo por error con la system instruction del Prompt 1 y no se usa en la matriz.

| Prueba | Imagen | Hora | situacion · accion_robot · urgencia · confianza | momento_oportuno | frase_robot | API |
|---|---|---|---|---|---|---|
| 4 | `comensales/comensal_mano_levantada.jpg` | 8:21 p. m. | buscando_atencion · acercarse_ahora · alta · 0.9 | "ahora" | "¿En qué puedo ayudarle?" | Igual: buscando_atencion · acercarse_ahora · alta · 0.9 |
| 5 | `comensales/comensal_indeciso_carta.jpg` | 8:20 p. m. | indeciso · **observar** · baja · **0.5** | "cuando la comensal levante la mirada" | "¿Le gustaría que le recomiende algún plato de la carta?" | indeciso · acercarse_pronto · baja · 0.7, frase copiada del few-shot |
| 6 | `comensales/grupo_celebrando.jpg` | 8:24 p. m. | celebrando · no_interrumpir · baja · 0.95 | "después de que soplen las velas o termine el momento central" | "¿Gusta que les tome una fotografía de este momento especial?" | Igual decisión (0.9); ofrecía café |
| 7 | `comensales/grupo_conversando.jpg` | 8:25 p. m. | **satisfecho_sin_necesidad** · no_interrumpir · baja · 0.9 | "cuando la interacción social disminuya o terminen su conversación" | "" (vacía) | celebrando · no_interrumpir · 0.9 |

- **Observaciones:**
  - Las cuatro respuestas son JSON válido con las 11 claves del esquema, sin Structured outputs.
  - **Mano levantada:** misma decisión que por API. La frase es más corta y sigue siendo neutra.
  - **Comensal con la carta:** AI Studio es más prudente que la API. Elige `observar` y espera el contacto visual, que es la primera opción del principio 5 ("espera a que haya contacto visual"), y baja la confianza a 0.5, por debajo del tope de 0.6 para señales ambiguas: no se ve la cara. La frase ya no es copia literal del ejemplo few-shot, aunque sigue muy cerca de él.
  - **Cumpleaños:** misma decisión. La sugerencia toma la idea del ejemplo few-shot (ofrecer la foto grupal) en vez del café de la API. Ofrecer la foto mientras están en el momento central sería interrumpir, pero el `momento_oportuno` la pospone.
  - **Grupo conversando:** corrige el error de la API. Clasifica `satisfecho_sin_necesidad`, la categoría que el reporte señalaba como la correcta, y deja `frase_robot` vacía, coherente con "si están satisfechos y conversando, no hagas nada". El prompt no dice qué poner en la frase cuando no hay que hablar; conviene definirlo (por ejemplo, `null`) para que el controlador no tenga que interpretar una cadena vacía.
  - Ninguna frase nombra la emoción inferida y ninguna respuesta menciona rasgos sensibles.
