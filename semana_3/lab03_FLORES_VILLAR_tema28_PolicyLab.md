# Lab 03 — Resuelto: Tema 28 "PolicyLab"

**Curso:** C451 – Interacción Humano Computadora
**Ámbito:** Gobierno y servicios públicos
**Subtema:** Políticas públicas
**Problema real:** Análisis lento de documentos normativos y simulaciones de impacto.
**Propuesta:** **PolicyLab** — analiza normativas, simula impactos y redacta borradores de políticas públicas, con supervisión humana obligatoria en toda decisión.

---

## FASE 1: Mapeo del ecosistema y stakeholders

### 1.1 Análisis del dominio

**Mapa de actores**

| Tipo | Actores |
|---|---|
| Directos | Analistas de políticas públicas, asesores legislativos, comisiones/congreso, funcionarios de ministerios sectoriales |
| Indirectos | Ciudadanía afectada por la norma, ONGs y sociedad civil, sector privado regulado, academia y think tanks, medios de comunicación |
| Invisibilizados | Comunidades rurales/urbano-populares sin acceso o tiempo para participar en consultas públicas, personas con discapacidad (visual, cognitiva) que no pueden leer documentos legales en PDF no accesible, personas sin conectividad estable |

**Factores regulatorios y éticos**

- Normas de transparencia y datos abiertos del Estado (acceso a la información pública).
- Necesidad de **trazabilidad y auditoría** de cualquier análisis o borrador generado por IA que influya en una decisión pública.
- Riesgo de **sesgo político o ideológico** en el análisis automatizado de normativas.
- Marco de protección de datos personales al procesar comentarios ciudadanos en consultas.

**Fricciones tecnológicas actuales**

- Sistemas de gestión documental legados, sin búsqueda semántica.
- Formatos no estandarizados entre entidades (PDF escaneado, Word, sistemas propietarios).
- Baja interoperabilidad entre bases de datos de distintos ministerios/congreso.

**Oportunidades de intervención digital**

- Comparar automáticamente versiones/borradores de una norma y resaltar cambios.
- Simular impacto socioeconómico usando datos abiertos (INEI, presupuesto público, indicadores sectoriales).
- Generar resúmenes ejecutivos multinivel (técnico → ciudadano) de un mismo documento normativo.

### 1.2 Matriz de poder-influencia: escenarios de conflicto

| # | Conflicto | Mecanismo de mediación tecnológica |
|---|---|---|
| 1 | Legisladores quieren decisiones rápidas basadas en IA vs. técnicos que exigen validación rigurosa de fuentes | Panel de revisión híbrida humano-IA: todo output muestra sus fuentes y un estado "borrador IA — pendiente de validación humana" hasta ser aprobado |
| 2 | Sector privado regulado presiona por análisis de impacto que minimicen su costo de cumplimiento vs. sociedad civil que exige proteger derechos | Publicar el análisis de impacto de forma abierta y comparativa (costo-beneficio para cada grupo de stakeholders, no solo el regulado) |
| 3 | Ciudadanía desconfía de que una IA participe en redactar políticas (falta de transparencia algorítmica) vs. Estado que busca eficiencia | Sello visible "Asistido por IA — revisado por [nombre/cargo del funcionario]" + registro auditable del prompt y las fuentes usadas, accesible públicamente |

---

## FASE 2: Modelado de usuarios y requerimientos

### 2.1 Personas (Anti-Bias Protocol)

| | **Rosa Medina** | **Diego Salcedo** | **Marta Injante** |
|---|---|---|---|
| Perfil demográfico mínimo | 42 años, analista de políticas en un ministerio sectorial | 29 años, asesor legislativo en el congreso | 55 años, ciudadana con discapacidad visual, activista comunitaria |
| Motivación oculta | Quiere que su análisis sea citado y valorado; teme que la IA "le quite mérito" ante sus jefes | Necesita quedar bien ante su jefatura política con respuestas rápidas y defendibles en debate | Quiere que su opinión en consultas públicas realmente sea tomada en cuenta, no solo "registrada" |
| Punto de dolor sistémico | Recibe cientos de páginas de normativa comparada de otros países y no tiene tiempo de leerlas todas antes de una reunión | Debe resumir informes técnicos densos en minutos, antes de una sesión de comisión | Los documentos de consulta pública están en PDF escaneado, incompatibles con lector de pantalla |
| Tecnología disponible | Laptop de oficina, conexión estable, poca costumbre con IA generativa | Smartphone y laptop, alta fluidez digital, trabaja bajo presión de tiempo | Smartphone con lector de pantalla (TalkBack/VoiceOver), conectividad intermitente |
| Frustración actual con soluciones existentes | Buscadores de normativa devuelven resultados poco relevantes y sin contexto de impacto | Los resúmenes que le entregan los equipos técnicos llegan tarde o son demasiado extensos | Las plataformas de participación ciudadana no son accesibles ni dan retroalimentación sobre qué pasó con su comentario |

> Nota anti-sesgo: se incluyó deliberadamente una persona con discapacidad visual (Marta) y se evitó estereotipar la política pública como un dominio "solo técnico/joven", incluyendo un perfil de analista senior (Rosa) con baja fluidez en IA.

### 2.2 Historias de usuario

| Historia | Criterios de aceptación (incl. WCAG) | Dependencias técnicas | Esfuerzo | Riesgo de sesgo algorítmico |
|---|---|---|---|---|
| Como **analista de políticas (Rosa)**, quiero **comparar automáticamente una norma propuesta con normativa vigente y de países similares**, para que **pueda identificar vacíos y contradicciones sin leer todo el corpus manualmente**. | El resumen cita explícitamente artículo y fuente; contraste de texto AA (4.5:1); resultado exportable a PDF/Word accesible | LLM + base de datos de normativas indexada (RAG), OCR para documentos escaneados | M | Alto — el modelo puede "alucinar" artículos inexistentes; requiere verificación obligatoria con enlace a la fuente original |
| Como **asesor legislativo (Diego)**, quiero **generar un resumen ejecutivo de un informe técnico en distintos niveles de detalle (1 párrafo / 1 página / completo)**, para que **pueda prepararme para un debate en minutos**. | Navegable por teclado; tiempo de generación visible; opción de "ver fuente completa" siempre disponible | Modelo de resumen con control de longitud, versionado del documento fuente | S | Medio — el resumen puede omitir matices críticos; se marca siempre como "resumen, no sustituye el documento original" |
| Como **ciudadana con discapacidad visual (Marta)**, quiero **que los documentos de consulta pública sean legibles por lector de pantalla y se me explique en lenguaje simple qué propone la norma**, para que **pueda participar en igualdad de condiciones**. | Cumple WCAG 2.2 AA (texto alternativo, orden de lectura lógico, sin trampas de foco); lenguaje ciudadano generado además del técnico | OCR + texto a voz, modelo de simplificación de lenguaje (lectura fácil) | M | Medio — simplificar puede introducir imprecisión legal; se ofrece siempre el original como referencia |
| Como **cualquier stakeholder**, quiero **ver quién y qué analizó cada borrador generado (IA vs. humano) y con qué fuentes**, para que **pueda confiar en el proceso y auditar decisiones**. | Registro visible de: fecha, modelo usado, prompt resumido, fuentes citadas, estado de revisión humana | Sistema de logging/versionado, panel de trazabilidad | M | Bajo — mitigación directa del riesgo de opacidad algorítmica |

---

## FASE 3: Especificación de diseño

### 3.1 Arquitectura de información (máx. 3 niveles)

```
PolicyLab
├── Inicio
│   ├── Buscar normativa (comparación nacional/internacional)
│   └── Notificaciones (nuevos borradores, consultas abiertas)
├── Análisis de normativa
│   ├── Comparador de versiones
│   └── Resumen ejecutivo (multinivel)
├── Simulación de impacto
│   ├── Configurar escenario (variables socioeconómicas)
│   └── Resultado + explicación en lenguaje simple
├── Borradores de política
│   ├── Redacción asistida
│   └── Trazabilidad (IA vs. revisión humana)
└── Participación ciudadana
    ├── Consulta pública activa (versión accesible)
    └── Historial de comentarios y respuesta institucional
```

- **Progressive disclosure:** al entrar a un documento se muestra primero el resumen de 1 párrafo; el usuario decide expandir a "1 página" o "documento completo".
- **Navegación por switch access:** todos los flujos críticos alcanzables con orden de tabulación lineal, sin necesidad de gestos multi-touch.
- **Estados vacíos:** ej. "Aún no hay simulaciones para esta norma" → botón directo "Crear la primera simulación".

### 3.2 Especificación de interacción crítica

**Flujo: Generar una simulación de impacto de una norma (3 pasos)**

1. **Trigger:** el usuario selecciona una norma y pulsa "Simular impacto".
   - Feedback visual inmediato (spinner) + sonoro opcional (tono breve de confirmación) para usuarios con baja visión.
2. **Configuración:** el usuario ajusta 2-3 variables clave (ej. población afectada, costo estimado, plazo de implementación) mediante controles simples con valores por defecto razonables.
   - Adaptación contextual: modo "manos libres"/lectura por voz de cada campo si el usuario tiene lector de pantalla activo.
3. **Resultado:** PolicyLab entrega un resumen en lenguaje simple ("Esta norma afectaría a ~120,000 personas, con un costo estimado de S/ X, principalmente en la región Y") + gráfico accesible con texto alternativo.
   - **Deshacer:** opción de "Modificar variables" sin perder el resultado anterior (se guarda como versión comparativa).
   - **Texto de error no culpabilizante:** si faltan datos, el mensaje es "No encontramos datos suficientes para esta variable — puedes estimarla manualmente o dejarla en blanco", nunca "Error: dato inválido".

---

## FASE 4: Evaluación

### 4.1 Heurística asistida (Nielsen + WCAG 2.2 AA)

| Problema | Severidad (1-5) | Recomendación técnica |
|---|---|---|
| El resumen ejecutivo no siempre indica que es generado por IA, generando falsa sensación de autoridad legal | 5 | Etiqueta persistente "Generado por IA — no reemplaza el documento oficial" en cada resumen, con enlace directo a la fuente |
| Los controles de la simulación de impacto no tienen suficiente contraste (gris claro sobre blanco) | 4 | Ajustar a contraste mínimo 4.5:1 (WCAG 2.2 AA); usar tokens de color validados |
| El flujo de consulta pública requiere completar 6 campos en una sola pantalla | 3 | Dividir en pasos progresivos (progressive disclosure) y guardar avance automáticamente |
| El lenguaje del borrador de política mantiene tecnicismos legales incluso en la versión "ciudadana" | 3 | Pipeline de simplificación con validación de nivel de lectura (ej. escala de legibilidad en español) |
| No hay forma de deshacer una simulación configurada por error | 3 | Agregar historial de versiones de simulación con opción de volver atrás |
| El sistema no distingue visualmente entre borradores aprobados y pendientes de revisión humana | 4 | Estado con color + ícono + texto (no solo color, por accesibilidad para daltonismo) |

### 4.2 Análisis de impacto ético

**¿Cómo podría PolicyLab dañar si se usa mal?**

- **Legitimación falsa de decisiones automatizadas:** si un borrador generado por IA se aprueba sin revisión humana real, se podría promulgar una política con errores factuales o sesgos no detectados, afectando a poblaciones vulnerables.
- **Sesgo en la simulación de impacto:** si los datos de entrenamiento o las fuentes usadas subrepresentan a ciertas comunidades (rurales, indígenas, informales), las simulaciones subestimarán el impacto sobre ellas, perpetuando su invisibilización.
- **Alucinación de citas legales:** el modelo podría inventar artículos o jurisprudencia inexistente; si un asesor legislativo cita esto sin verificar, puede introducir errores graves en el debate público.
- **Concentración de poder narrativo:** un actor con acceso privilegiado al sistema podría usar los resúmenes generados para enmarcar una norma de forma sesgada antes de que otros stakeholders puedan revisarla.
- **Exclusión digital:** si la interfaz de participación ciudadana no es verdaderamente accesible (a pesar del diseño), las comunidades sin conectividad o alfabetización digital quedarían aún más excluidas del proceso, mientras el Estado asume que "ya hubo participación digital".

**Mitigaciones incorporadas en el diseño:** trazabilidad obligatoria IA-humano, verificación de fuentes citadas, versión ciudadana en lenguaje simple y accesible, y publicación abierta del análisis de impacto para todos los stakeholders (no solo el sector regulado).

---

## Checklist de entrega

- [x] Documento con las 4 fases completadas
- [ ] Prototipo navegable (Figma o similar) con al menos 5 flujos críticos — *pendiente de construir en Figma*
- [x] Análisis de impacto ético (sección 4.2)
