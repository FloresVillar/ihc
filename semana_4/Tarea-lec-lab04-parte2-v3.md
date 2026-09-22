# Tarea LEC-LAB04 - Parte 2.

1. Conforme un grupo de 2-3 personas. Y escoja cada persona un proveedor de Inferencia LLM (Claude, ChatGPT, Gemini, DeepSeek)
2. Cada grupo escogerá un escenario de interacción: (Asistente virtual especializado en alguno de los siguientes contextos: servicio al cliente (clinica, restaurante, hotel), tutor de aprendizaje, mesa de ayuda) cada grupo escogerá 2-3 proveedores de LLM (dependiendo del numero de miembros del grupo)
3. Diseñe un prompt para configurar su asistente. (debe ser el mismo para cada LLM)
4. Analizar como se maneja:
   a) El Contexto,
   b) Las ambiguedades y
   c) Las peticiones de aclaración.

   Para ello diseñe el prompt mas adecuado por cada item y compare las respuestas de los 2 o 3 LLMs.

   Tomando como base la actividad de clase.
   - Mejore el prompt para configurar su asistente. – Cuales han sido las mejoras con respecto a la actividad anterior? (El Prompt debe ser el mismo para cada LLM y obtener el mejor resultado posible)
   - Completar la evaluacion de las conversaciones (5 conversaciones por modelo como minimo) de manera mas objetiva, incorporando las metricas propuestas.

(A continuación se muestran ejemplos de un Chatbot asistente de una clinica)

## Métricas cuantitativas y cualitativas

### 1. Eficiencia para Cumplir la Tarea

- **Métrica Objetiva:** Tasa de éxito de la tarea (Task Completion Rate - TCR)
- **Método de Evaluación:**
  1. Define una lista de tareas específicas que el chatbot debe ser capaz de realizar (ej. agendar una cita, proporcionar información sobre doctores). Especifique las tareas completamente.
  2. Pruebe el chatbot con un grupo de usuarios o evaluadores simulados, asignándoles tareas específicas.
     (Puede simular diferentes tipos de usuario – por ejemplo 4 tipos de usuario – para que la LLM genere consultas o peticiones según el tipo de usuario. Dichas consultas o peticiones deben probarse con el chatbot diseñado. – puede generar peticiones erroneas para verificar como las maneja el chatbot diseñado)
  3. Mide cuántas tareas se completan correctamente en relación con el total de intentos.
- **Fórmula:**

  $$TCR = \left(\frac{\text{Número de tareas completadas exitosamente}}{\text{Número total de tareas asignadas}}\right) \times 100$$

- **Umbral de evaluación:** Un TCR superior al 85% puede considerarse eficiente.

### 2. Claridad en la Conversación

- **Métrica Objetiva:** Tasa de aclaración (Clarification Request Rate - CRR)
- **Método de Evaluación:**
  1. Recolecta interacciones en las que los usuarios pidieron aclaraciones o repitieron preguntas debido a la confusión.
  2. Simule usuarios que no comprenden la respuesta. Configure otra sesión con el LLM, dando las características del usuario (P. ej. Usuario de la tercera edad, Usuario con discapacidad auditiva, o visual). Este chatbot recibirá las respuestas generadas por el asistente.
  3. Cuenta el número de veces que el chatbot recibe una solicitud de aclaración (por ejemplo, "¿Puedes repetir?" o "No entiendo").
  4. Divide ese número entre el total de interacciones.
- **Fórmula:**

  $$CRR = \left(\frac{\text{Número de solicitudes de aclaración}}{\text{Número total de interacciones}}\right) \times 100$$

- **Umbral de evaluación:** Un CRR inferior al 10% indica que el chatbot es claro en sus respuestas.

### 3. Capacidad de Gestionar Diálogos Complejos

- **Métrica Objetiva:** Longitud media de diálogo exitoso (Average Dialogue Length - ADL)
- **Método de Evaluación:**
  1. Diseña escenarios de conversación que requieren múltiples turnos de interacción (por ejemplo, reservar una cita médica que involucre varias preguntas).
  2. Mide el número de turnos necesarios para completar una tarea compleja y compara con la longitud ideal o esperada de la interacción.
  3. Analiza la relación entre la longitud del diálogo y el éxito de la tarea.
- **Fórmula:**

  $$ADL = \frac{\text{Número total de turnos en diálogos exitosos}}{\text{Número total de interacciones exitosas}}$$

- **Umbral de evaluación:** Un ADL cercano al número mínimo de pasos para completar la tarea sugiere una buena gestión de diálogos complejos. Demasiados turnos pueden indicar falta de eficiencia.
- **Método Complementario:** Realiza un análisis de conversación para ver si el chatbot maneja bien las interrupciones, cambios de contexto o seguimientos.

### 4. Adaptabilidad ante Preguntas Imprevistas

- **Métrica Objetiva:** Tasa de manejo de excepciones (Exception Handling Rate - EHR)
- **Método de Evaluación:**
  1. Introduce preguntas que están fuera del alcance del chatbot o que no forman parte de las tareas predefinidas, simulando interacciones inesperadas o ambiguas.
  2. Evalúa cómo el chatbot maneja estas situaciones (por ejemplo, si redirige correctamente la pregunta, solicita aclaración o informa al usuario de forma adecuada).
  3. Mide el número de veces que el chatbot manejó correctamente las excepciones en comparación con las veces que falló.
- **Fórmula:**

  $$EHR = \left(\frac{\text{Número de excepciones correctamente manejadas}}{\text{Número total de preguntas imprevistas}}\right) \times 100$$

- **Umbral de evaluación:** Un EHR superior al 70% puede indicar una buena adaptabilidad, aunque este número puede variar según la complejidad del dominio.

## Resúmen de Evaluación

- **Eficiencia:** TCR (Task Completion Rate), éxito en el cumplimiento de la tarea asignada.
- **Claridad:** CRR (Clarification Request Rate), solicitudes de aclaración por parte del usuario.
- **Diálogos Complejos:** ADL (Average Dialogue Length), longitud de interacción hasta cumplir la tarea.
- **Adaptabilidad:** EHR (Exception Handling Rate), manejo de preguntas imprevistas o excepcionales.

1. Presente un grafico para cada indicador (eficiencia, claridad, dialogos complejos, Adaptabilidad) comparando los Modelos utilizados. Incluya sus conclusiones.
2. Proponga un método para automatizar la evaluacion e involucrar mas tipos de LLMs de manera práctica.
