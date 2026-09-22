# Tutoriales de Figma — Pasos exactos de UI

> Nota metodológica: esta es una referencia de consulta rápida (cheat-sheet) con los pasos exactos de la interfaz de Figma mostrados en cada video del curso "Diseño de Figma para principiantes" (playlist `PLXDU_eVOJTx5IuSrbtanZHnDuPB3Hx0hq`). No es una transcripción del audio: son los nombres reales de menús, paneles, botones y atajos de teclado, en orden y agrupados por tarea, para ejecutar la acción sin tener que volver a ver el video.

## Índice

1. [Descripción del curso](#1-descripción-del-curso)
2. [Configura tu cuenta de Figma](#2-configura-tu-cuenta-de-figma)
3. [Navegar por los archivos de diseño de Figma](#3-navegar-por-los-archivos-de-diseño-de-figma)
4. [Crea el héroe de la landing page](#4-crea-el-héroe-de-la-landing-page)
5. [Crear la página de estudio de caso](#5-crear-la-página-de-estudio-de-caso)
6. [Crea el botón](#6-crea-el-botón)
7. [Fundamentos de componentes](#7-fundamentos-de-componentes)
8. [Crea el sistema de tarjetas y contenedores](#8-crea-el-sistema-de-tarjetas-y-contenedores)
9. [Crea la barra de navegación y el pie de página](#9-crea-la-barra-de-navegación-y-el-pie-de-página)
10. [Crea la lista de habilidades](#10-crea-la-lista-de-habilidades)
11. [Armar las páginas del portafolio](#11-armar-las-páginas-del-portafolio)
12. [Añadir conexiones de prototipos](#12-añadir-conexiones-de-prototipos)
13. [Resumen del curso](#13-resumen-del-curso)

---

## 1. Descripción del curso

**Video:** [zzhSFobLkYw](https://www.youtube.com/watch?v=zzhSFobLkYw)

Video introductorio, sin pasos de UI. El curso construye un sitio de portafolio desde cero: capas básicas (formas, texto, frames) hasta un layout responsivo e interactivo (auto layout, componentes, prototipado). Todo funciona en el plan gratuito de Figma.

[⬆ Volver al índice](#índice)

---

## 2. Configura tu cuenta de Figma

**Video:** [O3gwSmExW1Q](https://www.youtube.com/watch?v=O3gwSmExW1Q)

**Crear cuenta**
1. Ir a `figma.com/signup`.
2. Ingresar correo y contraseña, o usar la cuenta de Google.
3. Verificar el correo y seguir los pasos en pantalla.

**Volver al navegador de archivos (file browser)**
1. Abrir el menú principal (ícono de Figma, esquina superior izquierda) → "Back to files", o clic en el botón "Home" en la app de escritorio.

**Personalizar el perfil**
1. Clic en el avatar (esquina superior izquierda) → "Settings".
2. Clic en "Edit" bajo el avatar → elegir una imagen del computador.
3. Editar el nombre en el mismo panel.

**Crear el primer archivo de diseño**
1. Seleccionar el espacio "Drafts" en la barra lateral.
2. Clic en "Create new" → "Design file".

[⬆ Volver al índice](#índice)

---

## 3. Navegar por los archivos de diseño de Figma

**Video:** [zt-Zr57Vfzs](https://www.youtube.com/watch?v=zt-Zr57Vfzs)

**Renombrar el archivo**
1. Abrir el "File menu" (barra lateral izquierda) → "Rename", o doble clic sobre el nombre del archivo en la barra lateral y escribir el nuevo nombre.

**Moverse por el canvas**
1. Seleccionar la herramienta "Move" en la barra de herramientas, o presionar `V`.
2. Mantener presionada la barra espaciadora + clic y arrastrar para desplazarse, o deslizar dos dedos en el trackpad.
3. Presionar `H` para activar la herramienta "Hand" y moverse sin seleccionar nada.
4. Para zoom: pellizcar con dos dedos en el trackpad, o mantener el atajo de zoom + rueda del mouse.

**Agregar y renombrar páginas**
1. Clic en el botón "+" de la sección "Pages" (barra lateral izquierda).
2. Doble clic sobre el nombre de cada página para renombrarla (ej. "Explorations", "Designs", "Components").

**Activar etiquetas de propiedades (property labels)**
1. Abrir el menú principal en la barra lateral izquierda.
2. Ir a "View" → activar "Property labels".

[⬆ Volver al índice](#índice)

---

## 4. Crea el héroe de la landing page

**Video:** [q3RM7W2PjUs](https://www.youtube.com/watch?v=q3RM7W2PjUs)

**Crear la forma del avatar (elipse)**
1. Seleccionar la herramienta "Ellipse", o presionar `O`.
2. Clic en el canvas para colocarla.
3. En el panel derecho, sección "Layout", ajustar ancho y alto (ej. 90×90) y presionar Enter.

**Rellenar la forma con una imagen**
1. Con la forma seleccionada, ir a "Fill" (panel derecho) → clic en la muestra de color.
2. Elegir "Image" en la parte superior → "Upload from computer" → seleccionar archivo → "Open".
3. Para reencuadrar: clic en "Crop image" (parte superior del panel derecho), arrastrar la imagen para reposicionarla, o arrastrar las esquinas de la imagen (mantener Shift para conservar proporción).

**Crear y estilizar texto**
1. Seleccionar la herramienta "Text", o presionar `T`.
2. Clic en el canvas (ancho automático) o clic y arrastrar (tamaño fijo) para crear la caja de texto.
3. En "Typography" (panel derecho): elegir fuente, tamaño, peso (weight), interlineado (line height) y alineación.
4. Abrir "Type settings" para más opciones (estilos de lista, espaciado de párrafo, mayúsculas/minúsculas).
5. En "Layout", cambiar la propiedad "resizing" del texto entre "Fixed size", "Auto width" o "Auto height".

**Alinear capas**
1. Seleccionar varias capas (clic y arrastrar sobre ellas).
2. En el panel derecho, usar los botones de alineación (ej. "Align left").

**Reposicionar con precisión (nudge)**
1. Flechas del teclado = mover 1 px ("small nudge").
2. Shift + flechas = mover 10 px ("big nudge").
3. Para cambiar esos valores: menú principal de Figma → "Preferences" → "Nudge amount".

**Agrupar elementos en un frame**
1. Seleccionar la herramienta "Frame", o presionar `F`.
2. Clic y arrastrar alrededor de los elementos.
3. Verificar en el panel de capas que todo quedó anidado dentro del frame.
4. Doble clic sobre el nombre del frame (panel de capas) para renombrarlo.

[⬆ Volver al índice](#índice)

---

## 5. Crear la página de estudio de caso

**Video:** [G9ojik2MEeQ](https://www.youtube.com/watch?v=G9ojik2MEeQ)

**Crear un frame con preset de tamaño**
1. Seleccionar la herramienta "Frame".
2. En el panel derecho, abrir una categoría de preset (ej. "Desktop") y elegir el tamaño.
3. Renombrar el frame resultante.

**Redimensionar un frame manualmente**
1. Seleccionar el frame.
2. Clic y arrastrar el borde inferior (u otro borde) para alargarlo/acortarlo.

**Crear texto anidado directamente en un frame**
1. Seleccionar la herramienta "Text" y hacer clic dentro del frame (queda anidado automáticamente).

**Crear un frame a partir de una capa ya existente**
1. Seleccionar la capa (ej. el texto de título).
2. Clic derecho → "Frame selection".

**Configurar restricciones (constraints)**
1. Seleccionar la capa hija (su frame padre no debe tener auto layout).
2. En "Position" (panel derecho), ajustar constraint horizontal (Left/Right/Center/Scale) y vertical (Top/Bottom/Center/Scale).

**Centrar capas**
1. Seleccionar la capa.
2. En "Position", clic en "Align horizontal center" y/o "Align vertical center".

**Distribuir espaciado y usar Smart Selection**
1. Seleccionar el frame padre y presionar `Enter` para seleccionar todos los hijos.
2. Clic en "Align horizontal centers".
3. Abrir el menú "···" (more actions) en "Position" → "Distribute vertical spacing" (o usar "Tidy up").
4. Con los objetos distribuidos uniformemente, pasar el cursor sobre la selección: aparecen círculos y manijas rosados (Smart Selection). Arrastrar los círculos para reordenar; arrastrar las manijas (o usar los campos "Space between") para ajustar el espacio.

[⬆ Volver al índice](#índice)

---

## 6. Crea el botón

**Video:** [PZaBmmI0s4M](https://www.youtube.com/watch?v=PZaBmmI0s4M)

**Convertir una capa de texto en frame con auto layout**
1. Seleccionar la capa de texto.
2. Presionar `Shift + A` (Figma crea un frame con auto layout alrededor).
3. Doble clic en el nombre del frame para renombrarlo (ej. "Button").

**Cambiar el fill con atajo de un solo carácter**
1. Seleccionar la capa.
2. En "Fill", escribir en el campo junto a la muestra un solo carácter hex (ej. `F` → blanco `FFFFFF`, `0` → negro `000000`) y presionar Enter.

**Redondear esquinas**
1. Con el frame seleccionado, en "Appearance" (panel derecho), ajustar "Corner radius".

**Configurar auto layout (resizing, dirección, gap, alineación, padding)**
1. Seleccionar el frame con auto layout.
2. En "Auto layout" (panel derecho): elegir "Hug contents", "Fixed" o "Fill container" para ancho/alto.
3. Ajustar "Gap" (espacio entre capas hijas).
4. Ajustar "Padding" (o usar padding independiente por lado).

**Convertir en componente principal**
1. Seleccionar el frame terminado.
2. Clic en "Create component" (ícono de diamante) en el panel derecho.

[⬆ Volver al índice](#índice)

---

## 7. Fundamentos de componentes

**Video:** [7dJBDU8HBeQ](https://www.youtube.com/watch?v=7dJBDU8HBeQ)

**Crear un componente principal**
1. Seleccionar la(s) capa(s).
2. Clic en "Create component" (panel derecho), o clic derecho → "Create component".
3. Para varias a la vez: seleccionar dos o más objetos → "Create multiple components".

**Añadir una instancia**
1. Duplicar el componente principal en el canvas (`Ctrl/Cmd + D`), o
2. Ir a la pestaña "Assets" (barra lateral izquierda), ubicar el componente y arrastrarlo al canvas.

**Modificar y resetear una instancia**
1. Seleccionar la instancia y cambiar propiedades permitidas (texto, fill, stroke, tamaño).
2. Para revertir: clic derecho sobre la instancia → "Reset changes".
3. Para llevar el cambio al componente principal: menú de la instancia → "Push changes".

**Separar una instancia de su componente**
1. Clic derecho sobre la instancia → "Detach instance" (acción irreversible; deshacer de inmediato con `Ctrl/Cmd + Z` si fue un error).

[⬆ Volver al índice](#índice)

---

## 8. Crea el sistema de tarjetas y contenedores

**Video:** [9La952nT1_8](https://www.youtube.com/watch?v=9La952nT1_8)

**Construir la tarjeta (card)**
1. Crear texto "Project title" (Inter, tamaño 25, line height 38, peso semibold, alineación izquierda).
2. Duplicar esa capa para la descripción (peso medium, tamaño 20, line height 38).
3. Agregar una instancia del componente "Button" debajo de la descripción.
4. Agregar un rectángulo a la izquierda (alto 350), aplicarle fill tipo "Image" como placeholder, renombrarlo "thumbnail".

**Anidar auto layout en varias direcciones**
1. Seleccionar texto + botón → `Shift + A` → renombrar el frame "Description"; fijar "gap" vertical a 16.
2. Seleccionar "Description" + "thumbnail" → `Shift + A` → renombrar "Content"; fijar "gap" horizontal a 32; alineación "Top left".
3. En "Auto layout", abrir el desplegable de resizing de ancho → "Add max width" → ingresar el valor (ej. 1000).
4. Cambiar "width resizing" de capas internas a "Fill container" para que se ajusten al contenedor.

**Envolver en un frame contenedor (container system)**
1. Seleccionar la herramienta "Frame" y dibujarlo alrededor del elemento ya construido.
2. Renombrar (ej. "Project card").
3. `Shift + A` para aplicar auto layout; ajustar alineación, padding horizontal y vertical.

**Crear varios componentes a la vez**
1. Seleccionar todos los elementos terminados.
2. Clic en la flecha junto a "Create component" → "Create multiple components".

**Mover componentes a otra página**
1. Seleccionar los componentes → clic derecho → "Move to page" → elegir el destino (ej. "Components").

[⬆ Volver al índice](#índice)

---

## 9. Crea la barra de navegación y el pie de página

**Video:** [zo7FVhjOq68](https://www.youtube.com/watch?v=zo7FVhjOq68)

**Crear la base del navbar**
1. Crear un frame de 1440×80; renombrarlo "Navigation".
2. Agregar una capa de texto (wordmark) dentro del frame; ajustar peso (ej. black) y tamaño (ej. 20).

**Duplicar objetos**
1. Mantener `Alt`/`Option` y arrastrar para duplicar en una posición específica, o
2. `Ctrl/Cmd + D` para duplicar en el mismo lugar (Figma repite el patrón de distancia/rotación de la última duplicación).

**Agrupar enlaces de menú**
1. Alinear los textos con "Align vertical centers".
2. Seleccionarlos y presionar `Shift + A`; renombrar el frame "Links"; ajustar "gap" horizontal (ej. 24).

**Ocultar una capa sin eliminarla**
1. Clic en el ícono de ojo (visibility) de la capa, en el panel de capas.

**Insertar una instancia desde Assets**
1. Pestaña "Assets" → sección "Created in this file" → arrastrar el componente al frame.

**Ajustar ancho máximo y gap automático**
1. Seleccionar wordmark + frame de contenido extra → `Shift + A` → renombrar "Content"; fijar "Max width" (ej. 1000); cambiar el "gap" horizontal a "Auto".

**Aplicar auto layout al frame completo de navegación**
1. Seleccionar "Navigation" → `Shift + A`.
2. Fijar "height resizing" a "Fixed" (ej. 80); padding horizontal (ej. 24) y vertical (0); alineación "Center".

**Crear el footer a partir del navbar**
1. Duplicar el frame "Navigation"; renombrarlo "Footer".
2. Eliminar la capa del botón.
3. Clic derecho sobre el frame de contenido extra → "Ungroup".
4. Editar los textos de enlaces/contacto según corresponda.

**Crear ambos componentes juntos**
1. Seleccionar "Navigation" y "Footer" → clic en la flecha junto a "Create component" → "Create multiple components" → moverlos a la página "Components".

[⬆ Volver al índice](#índice)

---

## 10. Crea la lista de habilidades

**Video:** [9g04XTM_clE](https://www.youtube.com/watch?v=9g04XTM_clE)

**Crear formas con boolean operations**
1. Crear un frame (ej. 48×48), renombrarlo "Shape 1"; duplicarlo (Figma autonumera "Shape 2", "Shape 3"...).
2. Dibujar las formas base (rectángulos, elipses) dentro de cada frame.
3. Seleccionar dos o más capas → menú "Boolean operations" (barra de herramientas o clic derecho) → elegir "Union", "Subtract", "Intersect" o "Exclude".
4. Para deshacer: clic derecho sobre el grupo resultante → "Ungroup".

**Editar en modo vector**
1. Seleccionar la forma y presionar `Enter` (o doble clic) para entrar a "Vector edit mode".
2. Pasar el cursor sobre un borde para ver el punto nuevo; clic para agregarlo.
3. Con el nodo seleccionado, editar su posición escribiendo valores (con signo +/-) en los campos X/Y del panel derecho.
4. `Enter` (o doble clic fuera de la forma) para salir del modo de edición vectorial.

**Modificar propiedades de arco de una elipse**
1. Seleccionar la elipse y pasar el cursor sobre su borde hasta ver la manija de arco.
2. Arrastrarla para ajustar el "sweep"; aparecen además las manijas "start" y "ratio".
3. También editable numéricamente en el panel derecho: "Start", "Sweep", "Ratio".

**Aplanar una capa (flatten)**
1. Clic derecho sobre la capa → "Flatten" (irreversible; deshacer con `Ctrl/Cmd + Z` si fue un error).

**Intercambiar una instancia (swap instance)**
1. Seleccionar la instancia.
2. En el panel derecho, abrir "Swap instance" y elegir el componente de reemplazo.

**Cambiar colores de una selección múltiple**
1. Seleccionar varias capas con distintos fills.
2. Usar "Selection colors" (panel derecho) para cambiar todos los fills coincidentes a la vez.

**Ensamblar la lista final**
1. Agrupar texto + forma repetidos con `Shift + A` en un frame "Content"; fijar "Max width" (ej. 1000).
2. Si el contenido ya está en filas, "Direction" puede quedar en "Wrap"; ajustar "gap" horizontal/vertical y padding.
3. Envolver todo en un frame contenedor final, aplicar auto layout, quitar el fill, y convertir en componente principal.

[⬆ Volver al índice](#índice)

---

## 11. Armar las páginas del portafolio

**Video:** [Dv8tr65KIWA](https://www.youtube.com/watch?v=Dv8tr65KIWA)

**Organizar componentes con secciones**
1. Seleccionar la herramienta "Section".
2. Clic y arrastrar en el canvas para crearla; doble clic en el campo de título para renombrarla.
3. Arrastrar componentes dentro, o seleccionarlos y usar clic derecho → "Wrap in new section".
4. Cambiar el color de fondo de la sección desde el panel derecho.

**Ensamblar páginas con instancias**
1. Pestaña "Assets" → arrastrar instancias (navbar, skills list, footer, etc.) al canvas de la página "Designs".
2. Seleccionarlas y `Shift + A` para envolverlas en un frame con auto layout; ancho fijo (ej. 1440), alto "Hug contents", gap y padding en 0.
3. Duplicar ese frame para la segunda página (ej. "Home" y "Case study").

**Forzar que el contenido llene el ancho**
1. Seleccionar el frame de la página y presionar `Enter` para seleccionar todas las capas hijas.
2. Cambiar su "width resizing" a "Fill container".

**Editar desde el componente principal**
1. Clic derecho sobre una instancia → "Go to main component".
2. Clic en "Return to instance" para volver.
3. Si una instancia no refleja el cambio: menú de la instancia (···) → "Reset all changes".

**Editar contenido de una instancia**
1. Doble clic sobre un texto para editarlo, o mantener `Ctrl/Cmd` + clic para "deep select" la capa exacta bajo el cursor.
2. Doble clic en un placeholder de imagen para reemplazarlo.
3. Para copiar una captura de otro archivo de Figma: clic derecho en el elemento de origen → "Copy as PNG", luego pegar en el destino.

[⬆ Volver al índice](#índice)

---

## 12. Añadir conexiones de prototipos

**Video:** [ScsAc99PT_w](https://www.youtube.com/watch?v=ScsAc99PT_w)

**Crear una conexión de prototipo**
1. Seleccionar el objeto de origen y abrir la pestaña "Prototype" (panel derecho).
2. Pasar el cursor sobre el objeto hasta ver el círculo azul en el borde; arrastrar desde ahí (se vuelve un ícono "+") hasta el frame de destino.
3. En el menú de interacción, ajustar "Trigger" (ej. "On click"), "Action" (ej. "Navigate to", "Open link", "Scroll to", "Open overlay", "Change to", "Back") y el destino.
4. Para eliminar: seleccionar la conexión y presionar `Delete`, o arrastrarla a un espacio vacío del canvas.

**Abrir un enlace externo o de correo**
1. En "Action" elegir "Open link"; escribir la URL, o usar el prefijo `mailto:` seguido de la dirección de correo.

**Copiar una interacción a otro componente**
1. Seleccionar la conexión ya creada → `Ctrl/Cmd + C`.
2. Ir al componente principal correspondiente → `Ctrl/Cmd + V`.

**Previsualizar el prototipo**
1. Clic en el ícono "Preview" junto al punto de inicio del flujo (pestaña Prototype).
2. Usar las flechas de la ventana de vista previa para navegar; `R` reinicia el flujo.
3. Clic en "Present" (panel derecho) para la vista de presentación en pestaña nueva; `Z` alterna modos de ajuste de pantalla dentro de la vista previa.

**Fijar la barra de navegación al hacer scroll**
1. Seleccionar el componente de navegación.
2. En el panel derecho, cambiar su comportamiento de scroll de "Scrolls with parent" a "Sticky".

**Controlar el orden de apilado en auto layout**
1. Seleccionar el frame con auto layout.
2. En "Auto layout", cambiar "Canvas stacking" entre "Last on top" (por defecto) y "First on top".

**Crear un botón flotante fijo ("back to top")**
1. Duplicar el componente principal del botón y "Detach instance" para usarlo como base independiente.
2. Editar su estilo (ej. intercambiar fill/stroke, cambiar color del texto).
3. Convertirlo en un nuevo componente (ej. "button/secondary").
4. Insertar una instancia en la página; sobre ella, activar "Ignore auto layout" para posicionarla libremente dentro del frame.
5. En la pestaña Design, cambiar su posición a "Fixed" y fijar sus constraints (ej. "Bottom" y "Right").
6. En la pestaña Prototype, agregar interacción: Trigger "On click", Action "Scroll to" (destino el frame/sección superior), Animation "Animate" con curva "Ease out" y duración (ej. 400 ms).

**Crear varias conexiones iguales a la vez**
1. Seleccionar una capa repetida en un frame → "Select matching layers" (o su atajo) para seleccionar la misma capa en otros frames.
2. Desde la pestaña Prototype, arrastrar una sola conexión desde el símbolo "+": se crean las conexiones equivalentes para todas las capas seleccionadas.

[⬆ Volver al índice](#índice)

---

## 13. Resumen del curso

**Video:** [p37EopqBmIo](https://www.youtube.com/watch?v=p37EopqBmIo)

Video de cierre, sin pasos de UI. Referencia recursos adicionales del Figma Help Center, el foro de Figma y el canal de YouTube de Figma para seguir aprendiendo.

[⬆ Volver al índice](#índice)
