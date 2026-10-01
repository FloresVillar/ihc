# CC451 — Discusiones Éticas en Computación Afectiva — Parte 1

**Alumno:** Esaú Flores Villar
**Curso:** CC451 Interacción Humano Computadora — 2026-2
**Docente:** Ciro Núñez Iturri

**Tema asignado (3):** Supongamos que fuera posible crear una tecnología que se pudiera usar de forma encubierta (como una cámara espía) que lee si la persona frente a ti está teniendo o no la respuesta autonómica de "luchar o huir" asociada con la acción de mentir.

**Postura que defiendo:** **NO apoyemos que se construya.**

---

## 1. Qué es lo que realmente mediría el dispositivo

Antes de argumentar conviene precisar qué hace la tecnología, porque el enunciado ya trae una trampa en la redacción: el aparato no lee "la mentira", lee la respuesta de lucha o huida *asociada* a mentir. En la Lección 5 vimos que las tecnologías de detección de emociones miden señales periféricas: respuesta galvánica de la piel (GSR), expresiones faciales, gestos, movimiento corporal (diap. 29), y que la codificación facial clasifica el rostro en seis expresiones básicas a partir de una webcam (diap. 30-31). Una versión encubierta de esto sería, en la práctica, un polígrafo sin cables: cámara térmica o RGB que estima pulso, microexpresiones, sudoración y respiración a distancia.

El problema es que la respuesta de estrés no es específica de la mentira. La activa el miedo, la vergüenza, la ansiedad social, el estar frente a una autoridad, la cafeína, una condición médica o simplemente saber que te están evaluando. Lo que el dispositivo detecta es "esta persona está activada", y la inferencia "entonces miente" la pone el que lo usa. Toda mi posición se apoya en que ese salto no se puede cerrar con mejor ingeniería, y en que hacerlo de forma encubierta agrava cada uno de los daños.

## 2. Argumento 1 — No funciona como promete, y a escala se equivoca sobre todo con inocentes

La evidencia sobre el polígrafo, que mide exactamente lo mismo pero en condiciones controladas y con consentimiento, es mala. El informe del National Research Council de EE. UU. (2003), *The Polygraph and Lie Detection*, concluyó que su precisión está por encima del azar pero lejos de ser confiable, y que es especialmente inadecuado para cribado masivo. Paul Ekman, el mismo investigador detrás de la codificación facial de emociones básicas, describió el "error de Otelo": el inocente que teme no ser creído muestra la misma activación que el culpable. Y la revisión de Barrett et al. (2019) mostró que inferir estados internos a partir de movimientos faciales es mucho menos confiable de lo que asumen los sistemas comerciales; el mismo gesto significa cosas distintas según la persona, la cultura y el contexto.

Pero aunque el sensor fuera bastante bueno, la aritmética juega en contra cuando se usa sobre mucha gente. Supongamos un dispositivo optimista con 90 % de sensibilidad y 80 % de especificidad, aplicado a 1 000 personas de las cuales 50 (5 %) mienten sobre algo relevante:

- Detecta correctamente a 45 de los 50 mentirosos.
- Pero marca como "mintiendo" a 190 de los 950 que dicen la verdad (el 20 % de falsos positivos).
- De las 235 personas señaladas, **190 son inocentes: el 81 %.**

Esto es la falacia de la tasa base, y no se arregla subiendo un poco la precisión: mientras la mentira relevante sea rara en la población observada, la mayoría de las alertas serán falsas. Un aparato encubierto está pensado justamente para usarse sobre gente que no sabe que es evaluada, en entrevistas, ventas, citas o controles, es decir, en contextos de tasa base baja. El resultado es una máquina de generar sospechas injustas con apariencia de objetividad técnica.

## 3. Argumento 2 — Lo encubierto elimina el consentimiento y viola la privacidad mental

El enunciado subraya "de forma encubierta", y ahí está el núcleo ético. Una cámara normal registra lo que hago; este dispositivo pretende registrar lo que me pasa por dentro, sin que lo sepa y sin poder negarme. Las respuestas autonómicas son, por definición, involuntarias: no puedo decidir no sudar ni no acelerar el pulso. Es información que la persona no eligió expresar, extraída sin su conocimiento, y eso la convierte en el caso más extremo de lo que la lección llama detección indirecta de emociones (diap. 40), donde ya vimos, con el caso Cambridge Analytica, cómo la inferencia de rasgos psicológicos sin consentimiento real terminó usándose para manipular decisiones políticas.

El marco regulatorio va en la misma dirección. El Reglamento Europeo de IA (Reglamento (UE) 2024/1689) prohíbe los sistemas que infieren emociones en el trabajo y en centros educativos (art. 5.1.f), clasifica el reconocimiento de emociones como de alto riesgo en otros contextos y obliga a informar a las personas expuestas a él (art. 50.3). Un dispositivo cuyo diseño es no informar contradice esa obligación por construcción. En el Perú, la Ley 29733 de Protección de Datos Personales trata los datos biométricos como datos sensibles que requieren consentimiento expreso, algo imposible en un uso encubierto. Chile fue más lejos en 2021 al reconocer constitucionalmente la protección de la actividad cerebral y la información derivada de ella (neuroderechos). La tendencia es clara: la privacidad mental se está volviendo un derecho explícito, y este aparato existe para saltársela.

## 4. Argumento 3 — Destruye la confianza que la interacción social necesita

En la lección vimos que la interacción emocional con la tecnología se construye sobre la confianza y la credibilidad (diap. 50, 56), y que el phishing funciona precisamente porque explota esa confianza. Este dispositivo produce el efecto inverso a escala social: si cualquiera puede estar leyendo mi fisiología en secreto, cualquier conversación, sea con mi jefe, un vendedor, un policía o una pareja, pasa a ser un interrogatorio potencial. La reacción racional es la autocensura y la ansiedad, que irónicamente es lo que el aparato interpreta como "mentira". Se genera un círculo: la vigilancia produce estrés, el estrés produce falsos positivos, los falsos positivos justifican más vigilancia.

Además, la asimetría de poder es obvia. Quien tiene el dispositivo es el empleador, el interrogador, el prestamista o el agente de fronteras; quien es leído es la parte débil. Ya hay un precedente concreto: el proyecto europeo iBorderCtrl probó un avatar "detector de mentiras" en controles fronterizos y recibió fuertes críticas por falta de base científica y de transparencia, al punto de llegar a litigio en la justicia europea por el acceso a su documentación. Y los errores no se reparten al azar: la línea base de activación varía con la cultura, la neurodivergencia (por ejemplo personas autistas o con ansiedad), el idioma y la situación migratoria, de modo que los grupos más vulnerables serían los más señalados.

## 5. Argumento 4 — El diseño encubierto no tiene un uso legítimo que lo justifique

Se podría decir que la tecnología es neutral y que el problema está en su uso. Pero aquí el rasgo que define al producto *es* el uso: la capacidad de operar sin que el otro lo sepa. Los usos defendibles de la medición fisiológica, como investigación con consentimiento informado, biofeedback terapéutico o monitoreo de fatiga en conductores que saben que están siendo medidos, no necesitan ser encubiertos. Si quito lo encubierto, ya no estoy hablando de este dispositivo. Por eso no basta con "regular su uso": lo que se pide es construir una herramienta cuya ventaja diferencial es precisamente la que no deberíamos permitir.

## 6. Contraargumentos previsibles y respuesta

**"Ayudaría a detectar criminales, terroristas o fraudes."** Por la tasa base (sección 2), en esos escenarios casi todas las alertas serían falsas, y un terrorista entrenado o un psicópata con baja reactividad autonómica pasaría sin problema mientras el pasajero ansioso es detenido. Además, existen métodos con respaldo empírico y garantías procesales, como la entrevista cognitiva o la evidencia documental, que no requieren leer el cuerpo de nadie en secreto.

**"Si no mientes, no tienes nada que temer."** El argumento falla justo por el error de Otelo: el inocente que teme ser juzgado es el que más se activa. Y la privacidad no protege solo a quien oculta algo malo; protege la posibilidad de tener vida interior sin rendir cuentas de ella.

**"Si no lo construimos nosotros, lo hará otro."** Eso es un argumento para prohibirlo y fiscalizar, no para acelerarlo. Con las armas químicas o la clonación humana reproductiva, la comunidad técnica eligió no normalizar su desarrollo aunque fuera factible, y la prohibición europea de ciertos usos de reconocimiento emocional muestra que esa elección sigue siendo posible hoy.

**"Mejorará con más datos y mejores modelos."** Más datos refinan la medición de la activación, pero no resuelven que la activación no es específica de la mentira. Es un problema de validez del constructo, no de precisión del sensor.

## 7. Conclusión

Mi posición es que no se debe construir, por cuatro razones que se refuerzan entre sí. Primero, mide estrés y no mentira, y a escala la mayoría de sus acusaciones recaerían sobre inocentes. Segundo, su carácter encubierto anula el consentimiento sobre datos biométricos que la persona ni siquiera controla. Tercero, erosiona la confianza social y concentra el daño en quienes ya tienen menos poder. Cuarto, lo que lo distingue de otras tecnologías legítimas de medición fisiológica es justamente lo encubierto. Desde el diseño emocional que vimos en la lección, el objetivo de la computación afectiva es lograr interacciones más empáticas entre personas y máquinas (diap. 59). Un detector de mentiras secreto usa las mismas técnicas para lo contrario: convierte la emoción del otro en evidencia en su contra sin que lo sepa.

Una cosa que dejo abierta y que no resuelvo del todo: la frontera con usos consentidos, por ejemplo un sistema declarado de monitoreo de estrés en una entrevista policial grabada, con abogado presente. Ese caso ya no es el del enunciado porque deja de ser encubierto, pero sigue teniendo el problema de validez del argumento 1, y creo que merecería su propia discusión.

---

## Referencias

- Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., & Pollak, S. D. (2019). Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements. *Psychological Science in the Public Interest*, 20(1), 1–68.
- Ekman, P. (1985). *Telling Lies: Clues to Deceit in the Marketplace, Politics, and Marriage*. W. W. Norton.
- National Research Council (2003). *The Polygraph and Lie Detection*. The National Academies Press.
- Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo (Ley de Inteligencia Artificial), arts. 5.1.f y 50.3.
- Ley N.° 29733, Ley de Protección de Datos Personales (Perú).
- Núñez Iturri, C. (2026). *Lección 5 — Interacción Emocional*. CC451, UNI. Diapositivas 29–31, 40, 50, 56, 59.
