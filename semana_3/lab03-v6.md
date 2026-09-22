# C451 – Interacción Humano Computadora — Lab 03

## Uso de IA Generativa en el Desarrollo de Especificaciones para Diseño de Aplicaciones

**Modalidad:** Grupos de 3 estudiantes
**Entregables:** Documento de especificación + Prototipo interactivo + Validación con usuarios

## 1. Objetivos de aprendizaje

Al finalizar el laboratorio, el estudiante será capaz de:

- Utilizar IA generativa como herramienta de análisis (no reemplazo) para la identificación de stakeholders y contextos complejos.
- Sintetizar datos cualitativos en arquetipos de usuario (*User personas*) validados mediante heurísticas de IA.
- Generar especificaciones de diseño accesibles (WCAG 2.2) mediante prompting estructurado.
- Evaluar soluciones mediante inspección asistida por IA.

**Ej. Proveedores de IA:**

- https://www.perplexity.ai/
- https://chat.deepseek.com/
- https://claude.ai/
- https://aistudio.google.com/
- https://groq.com/

### Consideraciones éticas y advertencias

Sobre el uso de IA en este laboratorio:

1. **La IA es tu "co-piloto", no tu piloto:** Todo output de IA debe ser validado con al menos 2 fuentes académicas o primarias (entrevistas).
2. **Detección de alucinaciones:** Verifica específicamente que las "tendencias" mencionadas por la IA existan realmente (búsqueda web cruzada).
3. **Sesgos en personas:** Si la IA genera solo personas de cierto género/edad/etnia, corrige explícitamente el prompt.
4. **Derechos de autor:** Los prompts son herramientas metodológicas; el análisis crítico y las conclusiones deben ser **propias y originales**.

### Checklist de entrega final

- [ ] Documento PDF con las 4 fases completadas
- [ ] Prototipo navegable (Figma, o similar) con al menos 5 flujos críticos
- [ ] Análisis de impacto ético (1 página): ¿Cómo podría esta app dañar si se usa mal?

## 2. Estructura del laboratorio

### FASE 1: Mapeo del ecosistema y stakeholders

**Objetivo:** Definir el contexto sociotécnico antes de escribir código.

**Paso 1.1: Análisis del dominio mediante IA**

Prompt Engineering para Contexto:

> Actúa como un antropólogo digital especializado en [dominio del tema]. Identifica los actores principales, regulaciones clave, tensiones culturales y tecnologías disruptivas actuales en [tema específico].
> Estructura tu respuesta en:
> 1. Mapa de actores directos/indirectos
> 2. Factores regulatorios y éticos
> 3. Fricciones tecnológicas actuales
> 4. Oportunidades de intervención digital
>
> Restricción: Enfócate en el contexto latinoamericano/urbano.

Ejemplo de resultado esperado (Tema: Coordinación de resiliencia climática comunitaria):

> - Primarios: Líderes comunales, bomberos voluntarios, adultos mayores
> - Secundarios: Proveedores IoT de sensores climáticos, aseguradoras, municipalidades
> - Invisibilizados: Trabajadores informales sin acceso a smartphones premium
> - Tensión ética: Privacidad vs. geolocalización en tiempo real durante emergencias

**Paso 1.2: Matriz de poder-influencia**

Utilizar la IA para generar escenarios hipotéticos de conflicto:

> Dada la siguiente lista de stakeholders [pegar lista], genera 3 escenarios de conflicto de intereses realistas que podrían surgir durante el desarrollo de la app. Para cada uno, propón mecanismos de mediación tecnológica.

### FASE 2: Modelado de usuarios y requerimientos

**Objetivo:** Transformar datos abstractos en especificaciones funcionales tangibles.

**Paso 2.1: Generación asistida de personas (Anti-Bias Protocol)**

Estructura del prompt:

> Crea 3 arquetipos de usuario para una app sobre [tema] considerando:
> - Diversidad neurocognitiva (no solo edad/género)
> - Limitaciones socioeconómicas digitales (datos limitados, batería baja)
> - Contextos de uso extremos (multitarea, estrés, fatiga)

Formato de salida para cada persona:

| Nombre | Perfil demográfico mínimo | Motivaciones ocultas | Puntos de dolor sistémicos | Tecnología disponible | Frustración actual con soluciones existentes |
|---|---|---|---|---|---|

**Advertencia:** Evita estereotipos edadistas. Incluye al menos un usuario con discapacidad cognitiva o situacional (ej. manos ocupadas).

Ejemplo de resultado esperado — Persona 3: "Marina" (micro-trabajadora gig, 34 años):

> - Contexto: Realiza deliveries en bicicleta, estudia en intervalos de 15 minutos
> - Motivación oculta: Necesita validación social de sus habilidades, no solo ingresos
> - Punto de dolor: Las apps actuales asumen conectividad constante; ella opera en modo offline frecuente
> - Requerimiento funcional clave: Sincronización asíncrona con gamificación que funcione sin datos móviles

**Paso 2.2: De personas a historias de usuario técnicas**

Prompt de traducción:

> Convierte las siguientes necesidades de [Nombre Persona] en historias de usuario siguiendo el formato: "Como [rol], quiero [capacidad], para que [beneficio medible]".
>
> Añade para cada una:
> - Criterios de aceptación con métricas de accesibilidad (WCAG)
> - Dependencias técnicas (APIs, sensores hardware)
> - Nivel de esfuerzo estimado (S/M/L)
> - Riesgo de sesgo algorítmico

### FASE 3: Especificación de diseño

**Objetivo:** Documentar arquitecturas de información y flujos críticos.

**Paso 3.1: Arquitectura de información asistida**

Prompt para sitemap:

> Genera una arquitectura de información para [tema] con máximo 3 niveles de profundidad.
> Restricciones:
> - Principio de "progressive disclosure" (no mostrar todo al inicio)
> - Navegación compatible con switch access (para usuarios con motricidad limitada)
> - Estados vacíos diseñados (empty states) con acciones sugeridas
>
> Formato: Esquema jerárquico con notas sobre el contenido específico de cada nodo.

**Paso 3.2: Especificación de interacciones críticas**

Prompt para micro-interacciones:

> Describe el flujo de interacción para [tarea específica crítica] considerando:
> 1. Feedback háptico y sonoro (no solo visual)
> 2. Mecanismos de "deshacer" para acciones irreversibles
> 3. Adaptación contextual (ej. modo manos libres, modo alta distracción)
> 4. Textos de error que no culpabilicen al usuario
>
> Entrega: Lista numerada de pasos con especificaciones técnicas de implementación.

Ejemplo de resultado esperado — Flujo: Reporte de emergencia climática en 2 toques:

> 1. Trigger: Gestura de sacudida del dispositivo (detectada por acelerómetro)
> 2. Confirmación: Vibración en patrón SOS + "Mantén presionado para confirmar emergencia"
> 3. Feedback: Audio "Alerta enviada a 3 contactos cercanos" (sin necesidad de mirar pantalla)
> 4. Recuperación: Opción de cancelación durante 10 segundos con gesto de deslizamiento

### FASE 4: Evaluación

**Objetivo:** Verificar usabilidad, accesibilidad y ausencia de sesgos algorítmicos — la posibilidad de que un algoritmo de IA tome decisiones injustas, discriminatorias o sesgadas.

**Paso 4.1: Heurística asistida por IA (automatización crítica)**

Prompt de inspección:

> Evalúa el siguiente flujo de diseño [describir/detallar] según las 10 heurísticas de Nielsen y las pautas WCAG 2.2 nivel AA.
>
> Identifica específicamente:
> - Violaciones de consistencia
> - Problemas de contraste de color (simulación de daltonismo)
> - Carga cognitiva excesiva (número de elementos por pantalla)
> - Sesgos potenciales en el lenguaje utilizado
>
> Formato: Tabla con [Problema] | [Severidad 1-5] | [Recomendación técnica específica]

## 3. Rúbrica de evaluación del laboratorio

| Criterio | Insuficiente (0-3) | Aceptable (4-6) | Sobresaliente (7-10) |
|---|---|---|---|
| Uso crítico de IA | Copia prompts sin cuestionar | Usa IA para expandir ideas pero valida con fuentes | Demuestra "prompt engineering" avanzado y detecta alucinaciones del modelo |
| Stakeholders | Lista genérica sin contexto | Identifica actores pero omite tensiones éticas | Mapea relaciones de poder y propone mediaciones tecnológicas |
| Personas | Estereotipos demográficos | Perfiles realistas pero superficiales | Personas inclusivas con consideraciones socioeconómicas y neurodiversas innovadoras |
| Especificaciones | Wireframes sin justificación | Diseños funcionales pero estándar | Especificaciones técnicas detalladas con consideraciones de accesibilidad avanzada |

## 4. Temas propuestos

Nota: Todos los temas incluyen un componente de IA generativa e interfaces no tradicionales.

Ver documento adjunto de temas propuestos (`lab03-v6-temas.md`).
