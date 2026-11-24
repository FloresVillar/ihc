# Tarea Lec 14 – Evaluación automatizada de usabilidad y accesibilidad

**Sitio evaluado:** CyberDojo v0.3 (PWA de entrenamiento en ciberseguridad, CC451 grupo 15), servido en local con `npm start` en `http://localhost:8080/app/`.
**Repositorio:** https://github.com/FloresVillar/cc451-IHC-grupo15-cyberdojo
**Herramientas:** Lighthouse 12.2.1 (Chrome 151 headless, emulación móvil por defecto), axe-core 4.10.2 (reglas WCAG 2.0/2.1 A y AA más buenas prácticas), Chrome en viewport de escritorio (1280×900) y móvil (375×812).
**Alcance de axe:** las 16 pantallas del prototipo (P01 a P16 del selector «Ir a») en escritorio y en móvil, 32 escaneos en total.

## 1. Resultados

### Lighthouse (pantalla de ingreso)

| Categoría | Puntaje |
|---|---|
| Performance | **97** |
| Accessibility | **100** |
| Best Practices | **100** |

Métricas: FCP 2.0 s, LCP 2.1 s, TBT 0 ms, CLS 0.003, Speed Index 2.0 s.
Informe completo: `lighthouse.report.html` / `lighthouse.report.json`.

Oportunidades que marcó Lighthouse:

| Hallazgo | Ahorro potencial |
|---|---|
| Habilitar compresión de texto | 88 KiB |
| Reducir JavaScript sin usar | 57 KiB |
| Minificar JavaScript | 15 KiB |
| Reducir CSS sin usar | 10 KiB |

### axe-core (16 pantallas × 2 viewports)

- **0 violaciones de contraste de color** (`color-contrast`), **0 críticas o serias**, **0 problemas de ARIA** y **0 scroll horizontal en móvil**.
- 4 reglas con severidad *moderada*:

| Regla | Dónde | Pantallas afectadas |
|---|---|---|
| `heading-order` (niveles de encabezado saltan) | `h3` dentro de las tarjetas, sin `h2` previo | 16 de 32 |
| `region` (contenido fuera de landmarks) | `.presenter`, la barra de demo fuera del teléfono | 18 de 32 |
| `landmark-one-main` | P08 Llamada de vishing | 2 de 32 |
| `page-has-heading-one` | P08 Llamada de vishing | 2 de 32 |

### Pruebas cross-browser / móvil

- Chrome escritorio y Chrome emulando móvil 375×812: sin desbordes ni errores de maquetación detectados por script (no se revisó a ojo cada pantalla).
- **No se probó** en Firefox, Safari ni en un dispositivo físico (no disponibles en este entorno). Queda pendiente; la voz usa Web Speech API, que en Firefox no tiene STT, así que ahí aplicaría el respaldo de texto y botones.

## 2. Tres problemas críticos y su relación con principios UX

> En este prototipo no hay fallas graves. Se priorizan los 3 hallazgos con mayor efecto sobre usuarios reales, en especial lectores de pantalla, que son el público que el proyecto declara atender (discapacidad visual).

### Problema 1. La pantalla de llamada de vishing (P08) no tiene landmark `main` ni encabezado `h1`
- **Evidencia:** axe, reglas `landmark-one-main` y `page-has-heading-one`, en escritorio y móvil.
- **Principio violado:** *Visibilidad del estado del sistema* y *Consistencia y estándares* (Nielsen). Una persona con lector de pantalla no puede saber en qué pantalla está ni saltar al contenido principal, justo en la pantalla más inmersiva del entrenamiento.
- **Solución:** envolver la vista de llamada en `<main>` y añadir un `<h1>` (puede ser el nombre del atacante simulado o «Llamada en curso»). Se puede ocultar visualmente con la clase `sr` que ya existe en el proyecto.

### Problema 2. Saltos en la jerarquía de encabezados (h3 sin h2) en 16 de 32 escaneos
- **Evidencia:** axe, regla `heading-order`, en la mayoría de pantallas (P03, P05, P07 y otras).
- **Principio violado:** *Consistencia y estándares* y *Reconocimiento antes que recuerdo*. La navegación por encabezados, la forma habitual de los lectores de pantalla para recorrer una vista, entrega una estructura confusa.
- **Solución:** que cada vista tenga un `h1` (título de la pantalla), usar `h2` para las secciones y `h3` solo dentro de ellas. Es un cambio en las plantillas de `app/js/app.js`, sin impacto visual si se ajusta el CSS por clase.

### Problema 3. Rendimiento: sin compresión de texto y JavaScript pesado (≈170 KiB evitables)
- **Evidencia:** Lighthouse, FCP 2.0 s y LCP 2.1 s (los únicos puntos donde la performance baja de 100); `uses-text-compression` con puntaje 0 y `unused-javascript` con puntaje 0.
- **Principio violado:** *Eficiencia de uso* y *Visibilidad del estado*. El proyecto promete una PWA usable en celular y en redes de empresa; 2 s para el primer contenido es aceptable, pero se nota en 3G/4G débil, y el dojo es un entorno de interacción rápida.
- **Solución:** activar gzip/brotli en el servidor (`src/server/`), minificar `app.js` y `escenarios.js`, y cargar con `import()` dinámico las partes que no se usan al inicio (voz, torneos, administración).

### Hallazgo menor (sin riesgo para el usuario)
La barra de demo («Ir a», «Reiniciar demo») queda fuera de landmarks (`region`). Es andamiaje del prototipo; basta ponerla dentro de `<nav aria-label="Demo">` o quitarla en producción.

## 3. Propuesta de mejoras (resumen)

| # | Mejora | Esfuerzo | Efecto |
|---|---|---|---|
| 1 | `<main>` + `<h1>` en P08 | Bajo | Accesibilidad para lectores de pantalla |
| 2 | Jerarquía h1 → h2 → h3 en todas las vistas | Bajo | Navegación por encabezados |
| 3 | Compresión, minificado y carga diferida de JS | Medio | −170 KiB, mejor FCP/LCP |
| 4 | Barra de demo dentro de un landmark | Bajo | Limpia el informe de axe |
| 5 | Probar en Firefox/Safari y en un celular real | Medio | Cierra el cross-browser pendiente |

## 4. Limitaciones y pendientes

- **WAVE** (pedido en el Paso 2) **no se ejecutó**: es una extensión de navegador y no se pudo usar desde la terminal. Hay que correrla a mano en https://wave.webaim.org o con la extensión, sobre la URL local o desplegada, y pegar la captura.
- **Capturas de las herramientas:** se incluyen las del propio sitio (`captura-desktop-*.png`, `captura-movil-*.png`) y los informes de Lighthouse en HTML. Las capturas de las interfaces de Axe DevTools y WAVE las debes tomar tú para el entregable.
- Lighthouse solo audita una URL; la pantalla de ingreso (`/app/`) es la única que cargó directamente. El resto de pantallas se cubrió con axe vía el selector de la demo.
- Todo se midió en `localhost`; el rendimiento real depende del despliegue.

## 5. Archivos

- `lighthouse.report.html`, `lighthouse.report.json`: informe de Lighthouse.
- `axe.json`: violaciones de axe por pantalla y viewport.
- `captura-*.png`: capturas de la primera pantalla en escritorio y móvil.
