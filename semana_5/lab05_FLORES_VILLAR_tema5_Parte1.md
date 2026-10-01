# CC451 Discusiones Éticas en Computación Afectiva - Parte 1

**Tema (5):** Es posible que sea necesario formar los robots del futuro, que interactúen con muchas personas y hagan juicios sobre quién es "bueno" y quién "no es bueno". Debería permitirse en estos casos ocultar de las personas los sentimientos del robot.

**Postura defendida:** No, NO se debe permitir que se oculten las emociones de los robots.

## Qué es "la emoción del robot" en este caso

Primero hay que aterrizar qué se entiende por sentimientos de un robot, porque si no la discusión se va a la ciencia ficción. En computación afectiva la emoción de una máquina no es algo que el robot "sienta", es un estado interno (una variable de sospecha, agrado, alarma, etc.) que sube o baja según lo que percibe y que cambia lo que decide.

Esto se ve en el sistema de tutoría afectiva de la lección (diap. 60-61): el módulo de inferencia de afecto le pasa el estado del alumno al motor de reglas, y según ese estado el tutor decide si da una pista, felicita o recomienda un ejercicio más fácil. De modo que el estado afectivo es una entrada más del proceso de decisión, no un adorno de la interfaz.

Si llevamos eso al robot del enunciado (un robot de seguridad en un centro comercial, uno de control en un aeropuerto, uno que filtra postulantes) y ese robot tiene un estado de "desconfianza" hacia una persona que influye en si la clasifica como buena o no, entonces ocultar ese estado es ocultar parte de las razones del juicio. Eso es lo que defiendo que no se debe permitir. No digo que el robot tenga que mostrar en pantalla cada cambio de estado en tiempo real, sino que los estados que intervienen en una decisión sobre una persona tienen que ser accesibles para esa persona y para quien supervisa el sistema.

## Argumento 1: se ocultan las razones de un juicio

Cuando una persona o institución juzga a alguien se le pide que fundamente: un juez motiva su sentencia, un comité explica por qué rechazó una solicitud, y si hay indicios de animadversión personal se le puede recusar. Esto existe justamente porque el estado emocional afecta el juicio. La lección lo dice con el modelo de Norman: cuando estamos asustados o enojados nos enfocamos estrechamente y somos menos tolerantes (diap. 12). Si el robot tiene un equivalente de ese estado y lo usa para clasificar gente, aplica lo mismo, con la diferencia de que el robot repite el mismo sesgo con miles de personas.

Un precedente de qué pasa cuando un sistema automático decide "quién es riesgoso" sin mostrar sus razones es COMPAS, el algoritmo de riesgo de reincidencia usado en tribunales de EE. UU. ProPublica (2016) encontró que marcaba erróneamente como alto riesgo a acusados afroamericanos casi el doble de veces que a blancos, y el acusado no podía discutir los factores porque el modelo era propietario. Un robot que oculta su estado afectivo repite esa opacidad, y además ni siquiera se sabe que hay un componente emocional en el juicio.

En lo normativo ya hay algo en esa línea: el RGPD europeo (art. 22) reconoce el derecho a no ser sometido a decisiones solo automatizadas con efectos significativos y a recibir información sobre la lógica aplicada, y la Ley de IA de la UE (art. 50) obliga a informar a las personas cuando están expuestas a un sistema de reconocimiento de emociones. Un robot que juzga y oculta los estados que influyen en su juicio va en contra de las dos.

## Argumento 2: ocultar la emoción termina siendo mostrar una falsa

Un robot social tiene cara, voz y gestos, entonces si no muestra su estado real igual va a mostrar algo, lo más probable una expresión amable estándar. Es decir, la persona ve una cara amable mientras el sistema la está clasificando como sospechosa. Eso ya es una expresión emocional engañosa, y funciona igual que el phishing que vimos en la lección: se aprovecha la confianza para que la persona baje la guardia (diap. 50).

La lección también advierte que los agentes virtuales pueden dar una falsa sensación de confianza, al punto de que la gente les cuenta cosas personales a los chatbots (diap. 54). En un robot que juzga eso es peor, porque la persona que percibe amabilidad habla más y entrega información que no daría si supiera que la están evaluando con desconfianza. De modo que el robot saca ventaja justamente de tener su emoción oculta.

## Argumento 3: sin transparencia no hay credibilidad

Según la lección la credibilidad de un agente es el grado en que los usuarios creen en sus intenciones y su personalidad, y depende mucho del comportamiento: cómo se mueve, gesticula y muestra las emociones que tiene detrás (diap. 56). Esto es que la credibilidad depende de que lo que el agente muestra corresponda con lo que tiene "adentro". Si el robot oculta sus estados, la gente puede confiar en él un tiempo, pero es una confianza que no puede verificar.

La crítica al antropomorfismo va por el mismo lado (diap. 52): la retroalimentación personalizada se percibe como menos honesta y los usuarios reaccionan en contra. Si algún día se descubre que los robots que juzgaban a la gente tenían estados ocultos distintos a lo que mostraban, y en un sistema masivo eso termina saliendo, la desconfianza no se queda en ese robot sino que pasa a todos los sistemas de ese tipo, incluso los que funcionan bien.

## Argumento 4: un estado oculto no se puede auditar

El estado afectivo del robot sale de su entrenamiento y sus reglas. Si ese estado se dispara más con cierta forma de vestir, acento, color de piel o alguna discapacidad, eso es un sesgo, y solo se puede detectar si el estado queda registrado y es revisable. La lección muestra que la codificación facial reduce el rostro a seis expresiones básicas (diap. 30), y ese tipo de clasificación falla más con algunos grupos y culturas. Si el robot oculta cómo reaccionó con cada persona, el afectado no tiene cómo saber que lo trataron distinto y el auditor no tiene el dato para demostrarlo. Entonces la transparencia no es solo un derecho de la persona evaluada, también es lo que permite corregir el sistema.

## Contraargumentos y respuesta

1. "Si el robot muestra su desconfianza la gente aprenderá a engañarlo." Puede pasar, pero es el mismo riesgo de hacer público cualquier criterio, y con los sistemas humanos lo aceptamos porque la opacidad cuesta más. Además transparencia no significa tiempo real, el estado se puede registrar y comunicar junto con el juicio o cuando la persona lo pida. Lo que no se debe permitir es que nunca sea accesible.

2. "Mostrar emociones negativas puede intimidar o humillar." Eso es un problema de cómo se muestra, no de si se muestra. Se puede aplicar lo mismo que las pautas de Shneiderman para mensajes de error (diap. 23): evitar términos condenatorios, ser preciso y dar ayuda según el contexto. Algo como "no puedo aprobar su acceso, mi evaluación detectó X, puede pedir revisión de una persona" es transparente y no humilla.

3. "Los jueces y funcionarios también ocultan lo que sienten." Ocultan la expresión, pero tienen que motivar sus decisiones, se les puede recusar y sus fallos se apelan. El robot no trae esos contrapesos, y la transparencia de su estado es lo que los reemplaza. Además un juez ve casos uno por uno y el robot aplica el mismo criterio a miles.

4. "Las emociones del robot no son reales, así que no hay nada que ocultar." Si no influyeran en el juicio no habría razón para querer ocultarlas. Que se pida permiso para ocultarlas ya reconoce que importan.

## Conclusión

No se debe permitir que un robot que juzga personas oculte sus emociones porque (1) su estado afectivo es parte de las razones del juicio, (2) ocultarlo en un robot con cara y voz termina siendo mostrar una emoción falsa, (3) sin correspondencia entre lo que muestra y su estado interno no hay credibilidad real (diap. 56), y (4) lo que no se registra no se puede auditar ni corregir.

**Lo que no queda resuelto:** cuánto detalle mostrar y en qué momento. Mostrar todo en tiempo real puede ser contraproducente, y dejarlo solo en un registro para auditores puede no ser suficiente para el afectado. Lo que propongo es que el estado que influyó en el juicio se registre siempre, se le comunique a la persona junto con la decisión y quede disponible para revisión humana, pero el diseño concreto de esa interfaz es un problema de HCI que no está cerrado.

