# CURSO: CC451

## Laboratorio Dirigido 01

## 1. Introducción

**Objetivo general:**

Introducción al prototipado de aplicaciones para dispositivos móviles.
En este laboratorio crearemos el prototipo de una aplicación móvil con un esquema de interacción simple.

## 2. Recursos Informáticos

1. FIGMA web site: <https://www.figma.com/>
2. FIGMA Channel: <https://www.youtube.com/channel/UCQsVmhSa4X-G3lHlUtejzLA>
3. FIGMA Curso para principiantes: <https://www.youtube.com/watch?v=zzhSFobLkYw&list=PLXDU_eVOJTx5IuSrbtanZHnDuPB3Hx0hq&index=1>
4. FIGMA Diseño de Figma para principiantes: <https://www.youtube.com/watch?v=zt-Zr57Vfzs&list=PLXDU_eVOJTx5IuSrbtanZHnDuPB3Hx0hq&index=4>

## 3. DESARROLLO

Al final entregara un archivo con el nombre **CC451_Lab01_<Nombre_apellido>.zip** con los archivos generados por usted en el laboratorio. Los Prototipos Escogidos de modelos en papel, deben ser reproducidos en la herramienta FIGMA.

## 4. Ejercicio

**Tarea:** realizar un prototipo de una aplicación móvil para implementar una de las aplicaciones propuestas en el anexo.

*(Ej: Fig.1)*
```mermaid
flowchart LR
    A["Mobile app feedback example"]
    B["Login"]
    C["Registro (wireframe)"]
    D["Alerts"]
    E["Groups"]
    F["Feed"]
    H["Menú: Feed / Like / Favorites /
Comments / Timeline / Profile /
Settings / Stats"]
    G["Comments"]
    I["Timeline"]
    J["Profile"]
    K["Stats"]
    L["Timeline (placeholder)"]

    A --> B
    B --> C
    C --> B
    B --> D
    D --> E
    E --> D
    E --> F
    F --> H
    H --> F
    F --> G
    H --> I
    H --> J
    H --> K
    I --> L

    linkStyle 0 stroke:#7B2FF7,stroke-width:2px
    linkStyle 1 stroke:#E6007A,stroke-width:2px
    linkStyle 2 stroke:#2ecc71,stroke-width:2px
    linkStyle 3 stroke:#E6007A,stroke-width:2px
    linkStyle 4 stroke:#f39c12,stroke-width:2px
    linkStyle 5 stroke:#f39c12,stroke-width:2px
    linkStyle 6 stroke:#E6007A,stroke-width:2px
    linkStyle 7 stroke:#E6007A,stroke-width:2px
    linkStyle 8 stroke:#E6007A,stroke-width:2px
    linkStyle 9 stroke:#E6007A,stroke-width:2px
    linkStyle 10 stroke:#E6007A,stroke-width:2px
    linkStyle 11 stroke:#E6007A,stroke-width:2px
    linkStyle 12 stroke:#E6007A,stroke-width:2px
    linkStyle 13 stroke:#E6007A,stroke-width:2px
```
Para ello:

### 4.1. Diseño inicial de un wireframe

*(tiempo: 30 min)*

1. Escoja y anote el tema a desarrollar del anexo. A partir de la funcionalidad definida, agregue los detalles y funcionalidad necesarias para que la aplicación sea util y funcional. Describa por lo menos 10 tareas o funciones que deberán implementarse

*(funciones: p. ej. autenticación y registro de usuarios, inscripción de mascotas, catalogo de artículos, descripción de los servicios, interacción con otros usuarios, etc.)*

Crear un Archivo (**CC451_Lab01_<Nombre_apellido>.doc**) con sus respuestas.

2. Diseñar por lo menos 8-10 pantallas (30 min) y un esquema adicional de interacciones entre ellas. (Debe ser un wireframe en papel) Deberá adjuntar las fotos de su diseño a su documento.

### 4.2. Definir un Grupo temporal de 1-2 personas para discutir su diseño con su compañero de grupo

*(tiempo: 30 min.)*

3.1. Registre las ideas adicionales que surgen de la discusión.

### 4.3. Actualice su diseño con las sugerencias aceptadas

*(tiempo: 1:30 hrs.)*

Actualice su diseño y esquema de interacciones, a un diseño "En Limpio", utilizando FIGMA.

Ver: <https://www.youtube.com/watch?v=zt-Zr57Vfzs&list=PLXDU_eVOJTx5IuSrbtanZHnDuPB3Hx0hq&index=4>

```mermaid
flowchart TB
    subgraph browser["Chrome — figma.com/files/team/1561462095980731818/recents-and-sharing?fuid=971803862975552822"]
        subgraph bookmarks["Barra de marcadores"]
            direction LR
            bm1["Importar marcadores..."]
            bm2["Getting Started"]
            bm3["TUTORIA 2023-1 - Goo..."]
            bm4["Plan Curricular 2021"]
            bm5["* Plan Curricular 2021"]
            bm6["Microsoft OneDrive"]
            bm7["Lovable"]
            bm8["Graphviz"]
            bm9["Migo: El asistente de i..."]
            bm1 ~~~ bm2 ~~~ bm3 ~~~ bm4 ~~~ bm5 ~~~ bm6 ~~~ bm7 ~~~ bm8 ~~~ bm9
        end

        subgraph topnav["Barra superior Figma"]
            direction LR
            ws["Ciro ▾ (workspace)"]
            search["🔍 Buscar"]
            navd(["Design"])
            navf["FigJam"]
            navs["Slides"]
            navb["Buzz"]
            navsite["Site"]
            navm["Make"]
            navmore["⋯"]
            ws ~~~ search ~~~ navd ~~~ navf ~~~ navs ~~~ navb ~~~ navsite ~~~ navm ~~~ navmore
        end

        subgraph body["Contenido"]
            direction LR
            subgraph sidebar["Barra lateral"]
                direction TB
                sb_search["Search"]
                sb_recents(["Recents"])
                sb_community["Community"]
                sb_team["Ciro's Starter team ▾  Free"]
                sb_drafts["Drafts"]
                sb_allprojects["All projects"]
                sb_resources["Resources"]
                sb_trash["Trash"]
                sb_promo["Ready to go beyond this free plan? Upgrade for premium features."]
                sb_viewplans(["View plans"])
                sb_search ~~~ sb_recents ~~~ sb_community ~~~ sb_team ~~~ sb_drafts ~~~ sb_allprojects ~~~ sb_resources ~~~ sb_trash ~~~ sb_promo ~~~ sb_viewplans
            end

            subgraph main["Panel principal"]
                direction TB
                titulo["Recents"]
                subgraph banner["Describe your idea and make it come to life  (AI)"]
                    direction LR
                    banner_input["Make a Spanish language practice app with au"]
                    banner_btn(["Make it →"])
                    banner_close["✕"]
                    banner_input ~~~ banner_btn ~~~ banner_close
                end
                subgraph tabsrow["Pestañas y filtros"]
                    direction LR
                    tv(["Recently viewed"])
                    tf["Shared files"]
                    tp["Shared projects"]
                    f1["All organizations ▾"]
                    f2["All files ▾"]
                    f3["Last viewed ▾"]
                    f4["▦ / ☰"]
                    tv ~~~ tf ~~~ tp ~~~ f1 ~~~ f2 ~~~ f3 ~~~ f4
                end
                subgraph cards["Tarjetas de archivos recientes"]
                    direction LR
                    c1["Traductor de Señas — Edited 5 months ago"]
                    c2["Mindfulness Completion Screen — Edited 5 months ago"]
                    c3["Parcial IHC - Page 1 — Edited 5 months ago"]
                    c4["Prototipo ConnectSigns — Edited 5 months ago"]
                    c1 ~~~ c2 ~~~ c3 ~~~ c4
                end
                titulo ~~~ banner ~~~ tabsrow ~~~ cards
            end
            sidebar ~~~ main
        end
        bookmarks ~~~ topnav ~~~ body
    end

    nota["Utilice la opción 'Design' para este Lab."]
    nota -.-> navd
```
### 4.4. Compartir su diseño

Cree un archivo DOC. Individual

1. Incluya tareas definidas
2. Incluya Wireframes de baja fidelidad que usted ha diseñado en papel.
3. Comente su Diseño justifique las decisiones. Indique cuales fueron las sugerencias aceptadas y por que.
4. Indique y justifique cuales fueron sus sugerencias al diseño de su compañero de grupo.
5. Muestre las Pantallas generadas y modificadas con FIGMA
6. Describa el proceso los pasos que utilizo para crear el prototipo final
7. Incluya el enlace para acceder al prototipo.
8. Comprima los archivos resultantes y suba el archivo comprimido (**CC451_Lab01_<Nombre_apellido>.zip**) al repositorio del curso en **MS Teams**

---

Ver: https://www.youtube.com/watch?v=zt-Zr57Vfzs&list=PLXDU_eVOJTx5IuSrbtanZHnDuPB3Hx0hq&index=4

a) Cree una cuenta en https://www.figma.com/ y cree un archivo Nuevo

*Fig 2.1 Crear Nuevo archivo de diseño*
```mermaid
flowchart TB
    subgraph panel["Figma — panel lateral y contenido"]
        subgraph topbar["Barra superior"]
            direction LR
            ws["🔵 Ciro ▾"]
            bell["🔔"]
            ws ~~~ bell
        end

        subgraph sidebar["Barra lateral"]
            direction TB
            sb_search["🔍 Search for anything"]
            sb_recents(["Recents"])
            sb_drafts["Drafts to move"]
            sb_drafts_flag["⚠"]
            sb_team["🟢 CC451A ▾"]
            sb_team_plan["Free"]
            sb_search ~~~ sb_recents ~~~ sb_drafts ~~~ sb_team
            sb_drafts ~~~ sb_drafts_flag
            sb_team ~~~ sb_team_plan
        end

        subgraph main["Panel principal"]
            direction TB
            titulo["Recents"]
            subgraph cards["Tarjetas"]
                direction LR
                c1(["New design file"])
                c2["New Fig... (New FigJam file)"]
                c1 ~~~ c2
            end
            titulo ~~~ cards
        end
        topbar ~~~ sidebar
        sidebar ~~~ main
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    classDef figpurple fill:#A259FF,stroke:#A259FF,color:#ffffff
    classDef figgreen fill:#0FA958,stroke:#0FA958,color:#ffffff
    classDef figwarn fill:#FFCC00,stroke:#E8B900,color:#3D2B00
    class ws figblue
    class sb_recents figbluelt
    class sb_drafts_flag figwarn
    class sb_team figgreen
    class c1 figblue
    class c2 figpurple
```
para que aparezca el panel de la Fig 2.2

*Fig 2.2: Panel de FIGMA.*

```mermaid
flowchart TB
    subgraph browser["Chrome — figma.com/design/JJOSnA4qCc9Wz61mBOPM8t/Untitled?node-id=0-1&t=kAaK..."]
        subgraph editor["Editor de Figma"]
            direction LR

            subgraph leftpanel["Panel izquierdo"]
                direction TB
                fig_logo["🔷 ▾"]
                collapse["▭"]
                filename["Untitled ▾"]
                filestatus["Drafts   Free"]
                subgraph filetabs["Tabs"]
                    direction LR
                    ft1(["File"])
                    ft2["Assets"]
                    ft_search["🔍"]
                    ft1 ~~~ ft2 ~~~ ft_search
                end
                subgraph pages["Pages"]
                    direction TB
                    pages_add["+"]
                    page1(["Page 1"])
                end
                layers["> Layers"]
                fig_logo ~~~ collapse
                filename ~~~ filestatus ~~~ filetabs ~~~ pages ~~~ layers
            end

            canvas["Lienzo (vacío, con reglas -400..450)"]

            subgraph rightpanel["Panel derecho"]
                direction TB
                subgraph rp_top["Barra superior derecha"]
                    direction LR
                    rp_user["🔵 ▾"]
                    rp_play["▷ ▾"]
                    rp_share(["Share"])
                    rp_user ~~~ rp_play ~~~ rp_share
                end
                subgraph rp_tabs["Design / Prototype"]
                    direction LR
                    rp_design(["Design"])
                    rp_proto["Prototype"]
                    rp_zoom["100% ▾"]
                    rp_design ~~~ rp_proto ~~~ rp_zoom
                end
                rp_frame["Frame"]
                subgraph rp_phone["▾ Phone"]
                    direction TB
                    ph1["iPhone 14 & 15 Pro Max — 430×932"]
                    ph2["iPhone 14 & 15 Pro — 393×852"]
                    ph3["iPhone 13 & 14 — 390×844"]
                    ph4["iPhone 14 Plus — 428×926"]
                    ph5["iPhone 13 mini — 375×812"]
                    ph6["iPhone SE — 320×568"]
                    ph7["iPhone 8 Plus — 41...x..."]
                    ph1 ~~~ ph2 ~~~ ph3 ~~~ ph4 ~~~ ph5 ~~~ ph6 ~~~ ph7
                end
                rp_top ~~~ rp_tabs ~~~ rp_frame ~~~ rp_phone
            end

            leftpanel ~~~ canvas ~~~ rightpanel
        end

        subgraph toast["Aviso flotante"]
            direction LR
            toast_msg["We're working to move your drafts"]
            toast_link(["Learn more"])
            toast_close["✕"]
            toast_msg ~~~ toast_link ~~~ toast_close
        end
        classDef modal stroke:#888,stroke-width:1px,stroke-dasharray: 3 3,fill:#fafafa
        class toast modal

        subgraph toolbar["Barra de herramientas (flotante, abajo)"]
            direction LR
            tool_move["▽ ▾"]
            tool_frame(["⊞ ▾"])
            tool_rect["☐ ▾"]
            tool_pen["✎ ▾"]
            tool_text["T"]
            tool_ellipse["○"]
            tool_comp["⊞+"]
            tool_code["</>"]
            tool_move ~~~ tool_frame ~~~ tool_rect ~~~ tool_pen ~~~ tool_text ~~~ tool_ellipse ~~~ tool_comp ~~~ tool_code
        end

        help["❓ (ayuda)"]

        editor ~~~ toast ~~~ toolbar
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    class rp_share figblue
    class rp_design figbluelt
    class tool_frame figblue
```

b) En una página puede insertar varios paneles ▦ que representarán las pantallas de su aplicación (Fig.3) por ejemplo pueden ser paneles tipo "Android compact" (Fig.4).
 
```mermaid
flowchart LR
    subgraph fig3["Fig. 3 — Barra de herramientas (Frame seleccionado)"]
        direction LR
        t3_move["▽ ▾"]
        t3_frame(["⊞ ▾"])
        t3_rect["☐ ▾"]
        t3_pen["✎ ▾"]
        t3_text["T"]
        t3_ellipse["○"]
        t3_comp["⊞+"]
        t3_code["</>"]
        t3_move ~~~ t3_frame ~~~ t3_rect ~~~ t3_pen ~~~ t3_text ~~~ t3_ellipse ~~~ t3_comp ~~~ t3_code
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    class t3_frame figblue
```
```mermaid
flowchart LR
    subgraph fig5["Fig. 5 — Barra de herramientas (Rectángulo seleccionado, sobre lienzo con frame)"]
        direction TB
        canvas5["Lienzo — frame de dispositivo (contorno)"]
        subgraph toolbar5["Barra flotante"]
            direction LR
            t5_move["▽ ▾"]
            t5_frame["⊞ ▾"]
            t5_rect(["☐ ▾"])
            t5_pen["✎ ▾"]
            t5_text["T"]
            t5_ellipse["○"]
            t5_comp["⊞+"]
            t5_code["</>"]
            t5_move ~~~ t5_frame ~~~ t5_rect ~~~ t5_pen ~~~ t5_text ~~~ t5_ellipse ~~~ t5_comp ~~~ t5_code
        end
        canvas5 ~~~ toolbar5
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    class t5_rect figblue
```
```mermaid
flowchart TB
    subgraph fig4["Fig. 4 — Panel derecho de Figma"]
        direction TB
        subgraph f4_top["Barra superior"]
            direction LR
            f4_user["🔵 ▾"]
            f4_play["▷ ▾"]
            f4_share(["Share"])
            f4_user ~~~ f4_play ~~~ f4_share
        end
        subgraph f4_tabs["Design / Prototype"]
            direction LR
            f4_design(["Design"])
            f4_proto["Prototype"]
            f4_zoom["59% ▾"]
            f4_design ~~~ f4_proto ~~~ f4_zoom
        end
        f4_frame["Frame"]
        subgraph f4_phone["▾ Phone"]
            direction TB
            fp1(["Android Compact — 412×917"])
            fp2["Android Medium — 700×840"]
            fp3["iPhone 16 — 393×852"]
            fp4["iPhone 16 Pro — 402×874"]
            fp5["iPhone 16 Pro Max — 440×956"]
            fp6["iPhone 16 Plus — 430×932"]
            fp7["iPhone 14 & 15 Pro Max — 430×932"]
            fp8["iPhone 14 & 15 Pro — 393×852"]
            fp9["iPhone 13 & 14 — 390×844"]
            fp10["iPhone 14 Plus — 428×926"]
            fp11["iPhone 13 mini — 375×812"]
            fp12["iPhone SE — 320×568"]
            fp1 ~~~ fp2 ~~~ fp3 ~~~ fp4 ~~~ fp5 ~~~ fp6 ~~~ fp7 ~~~ fp8 ~~~ fp9 ~~~ fp10 ~~~ fp11 ~~~ fp12
        end
        f4_tablet["> Tablet"]
        f4_desktop["> Desktop"]
        f4_presentation["> Presentation"]
        f4_help["❓"]
        f4_top ~~~ f4_tabs ~~~ f4_frame ~~~ f4_phone ~~~ f4_tablet ~~~ f4_desktop ~~~ f4_presentation
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    class f4_share figblue
    class f4_design figbluelt
    class fp1 figbluelt
```

Buscamos Librerias de componentes: en back la barra de herramientas: ⊞

```mermaid
flowchart TB
    subgraph fig51["Fig 5.1 — Buscador de Plugins & widgets"]
        direction TB
        search["🔍 Search"]
        subgraph tabs["Tabs"]
            direction LR
            t_all["All"]
            t_assets["Assets"]
            t_plugins(["Plugins & widgets"])
            t_filter["All ▾"]
            t_all ~~~ t_assets ~~~ t_plugins ~~~ t_filter
        end
        suggested["Suggested"]
        subgraph r1["Process Mapper"]
            direction TB
            r1_desc["Who, what, when where, how? Align your team by mapping yo..."]
            r1_meta["Widget · 👤 51.4k users · ♡ 450 · In-app purchases"]
            r1_desc ~~~ r1_meta
        end
        subgraph r2["✓ Checklist"]
            direction TB
            r2_desc["Simple Checklists for Figma – Track and Complete Tasks Easily!"]
            r2_meta["Widget · 👤 211 users · ♡ 4"]
            r2_desc ~~~ r2_meta
        end
        subgraph r3["Wireframe Designer"]
            direction TB
            r3_desc["Effortlessly generate wireframe designs using AI"]
            r3_meta["Plugin · 👤 399k users · ♡ 3.7k · In-app purchases"]
            r3_desc ~~~ r3_meta
        end
        subgraph r4["Notas de Handoff | Cogna"]
            direction TB
            r4_desc["Entregas eficientes com anotações inteligentes"]
        end
        search ~~~ tabs ~~~ suggested ~~~ r1 ~~~ r2 ~~~ r3 ~~~ r4
    end

    subgraph toolbar51["Barra flotante (abajo)"]
        direction LR
        tb_move(["▽ ▾"])
        tb_frame["⊞ ▾"]
        tb_rect["☐ ▾"]
        tb_pen["✎ ▾"]
        tb_text["T"]
        tb_ellipse["○"]
        tb_comp(["⊞+"])
        tb_code["</>"]
        tb_move ~~~ tb_frame ~~~ tb_rect ~~~ tb_pen ~~~ tb_text ~~~ tb_ellipse ~~~ tb_comp ~~~ tb_code
    end

    tb_comp -.-> fig51

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figgray fill:#E9E9E9,stroke:#B3B3B3,color:#333333
    class tb_comp figblue
    class t_plugins figgray
```

en el campo de búsqueda podemos buscar en la sección Plugins & widgets

c) **En cada panel** puede agregar los componentes que crea necesarios (Fig. 5). Puede encontrar componentes en diseños compartidos por la comunidad de figma.

P.ej. Puede buscar p. ej. Ink Wireframe. En la pantalla desplegada (Fig. 5.2) encontrará componentes (p. Ej. Device) que puede agregar a su panel

```mermaid
flowchart TB
    subgraph fig52["Fig. 5.2 — Panel del plugin Ink Wireframe"]
        direction TB
        subgraph header["Encabezado"]
            direction LR
            h_icon["🔷"]
            h_title["Ink Wireframe"]
            h_close["✕"]
            h_icon ~~~ h_title ~~~ h_close
        end
        subgraph searchbar["Buscador"]
            direction LR
            s_search["🔍 Search"]
            s_list["☰"]
            s_search ~~~ s_list
        end
        subgraph grid["Grid de componentes"]
            direction TB
            subgraph row1["Fila 1"]
                direction LR
                g1_labels["○ Label · ○ Label · ○ Label"]
                g1_btn1["BUTTON (claro)"]
                g1_btn2["BUTTON (oscuro)"]
                g1_labels ~~~ g1_btn1 ~~~ g1_btn2
            end
            subgraph row2["Fila 2"]
                direction LR
                g2_image["Imagen (placeholder + texto)"]
                g2_card["Card (imagen + texto)"]
                g2_check(["☑ Label"])
                g2_image ~~~ g2_card ~~~ g2_check
            end
            subgraph row3["Fila 3"]
                direction LR
                g3_label["Label (input)"]
                g3_calendar["Calendario (Mon,Nov 29)"]
                g3_device["Device (marco de teléfono)"]
                g3_label ~~~ g3_calendar ~~~ g3_device
            end
            subgraph row4["Fila 4"]
                direction LR
                g4_card["Card (header + texto + botones)"]
                g4_divider["Línea divisoria"]
                g4_dropdown["Label ▾ (dropdown)"]
                g4_card ~~~ g4_divider ~~~ g4_dropdown
            end
            subgraph row5["Fila 5"]
                direction LR
                g5_list["Label / Label / Label (lista)"]
                g5_btn(["+ Button"])
                g5_fab(["●  (FAB +)"])
                g5_list ~~~ g5_btn ~~~ g5_fab
            end
            row1 ~~~ row2 ~~~ row3 ~~~ row4 ~~~ row5
        end
        header ~~~ searchbar ~~~ grid
    end
    classDef modal stroke:#888,stroke-width:1px,stroke-dasharray: 3 3,fill:#fafafa
    class fig52 modal

    arrow["◀ (flecha señalando el panel)"]
    arrow -.-> fig52

    classDef figblack fill:#000000,stroke:#000000,color:#ffffff
    classDef figred fill:#F24E1E,stroke:#F24E1E,color:#ffffff
    class g1_btn2 figblack
    class g5_btn figblack
    class g5_fab figblack
    class arrow figred
```

El resultado de agregar device al panel se ve en la fig. 5.3

```mermaid
flowchart TB
    subgraph fig53["Fig. 5.3 — Editor de Figma con Device agregado"]
        direction LR

        subgraph leftpanel["Panel izquierdo"]
            direction TB
            filename["Untitled ▾"]
            filestatus["Drafts   Free"]
            subgraph filetabs["Tabs"]
                direction LR
                ft1(["File"])
                ft2["Assets"]
                ft_search["🔍"]
                ft1 ~~~ ft2 ~~~ ft_search
            end
            subgraph pages["Pages"]
                direction LR
                pages_label["Pages"]
                pages_add["+"]
                pages_label ~~~ pages_add
            end
            subgraph layers["Layers"]
                direction TB
                l_device(["◇ Device"])
                l_navbar["◇ Navigation Bar"]
                l_statusbar["◇ Status Bar"]
                l_device --> l_navbar
                l_device --> l_statusbar
            end
            filename ~~~ filestatus ~~~ filetabs ~~~ pages ~~~ layers
        end

        canvas["Lienzo — Device (marco de teléfono con status bar 12:30 y navigation bar ◁ ○ □)"]

        subgraph rightpanel["Panel derecho"]
            direction TB
            subgraph rp_tabs["Design / Prototype"]
                direction LR
                rp_design(["Design"])
                rp_proto["Prototype"]
                rp_zoom["59% ▾"]
                rp_design ~~~ rp_proto ~~~ rp_zoom
            end
            subgraph rp_page["Page"]
                direction TB
                rp_color["☐ F5F5F5"]
                rp_opacity["100 %"]
                rp_eye["👁"]
                rp_color ~~~ rp_opacity ~~~ rp_eye
            end
            rp_vars["Local variables"]
            rp_styles["Local styles"]
            rp_export["Export"]
            rp_tabs ~~~ rp_page ~~~ rp_vars ~~~ rp_styles ~~~ rp_export
        end

        leftpanel ~~~ canvas ~~~ rightpanel
    end

    subgraph toolbar53["Barra flotante (abajo)"]
        direction LR
        t_move(["▽ ▾"])
        t_frame["⊞ ▾"]
        t_rect["☐ ▾"]
        t_pen["✎ ▾"]
        t_text["T"]
        t_ellipse["○"]
        t_comp["⊞+"]
        t_code["</>"]
        t_move ~~~ t_frame ~~~ t_rect ~~~ t_pen ~~~ t_text ~~~ t_ellipse ~~~ t_comp ~~~ t_code
    end

    help["❓"]

    fig53 ~~~ toolbar53

    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    classDef figpurple fill:#A259FF,stroke:#A259FF,color:#ffffff
    classDef figgray fill:#F5F5F5,stroke:#B3B3B3,color:#333333
    class rp_design figbluelt
    class l_device figpurple
    class rp_color figgray
```

d) Las interacciones (transiciones) entre componentes y pantallas se pueden definir en el panel derecho, en el TAB "PROTOTYPE". Para que se pueda modelar las interacciones **los componentes siempre deben estar dentro de un panel.** (Fig.6)

```mermaid
flowchart TB
    subgraph fig6["Fig. 6 — Insertando interacciones"]
        direction LR

        subgraph browser6["Chrome — figma.com/design/QWNosP04x5MaUnPHvZmizO/Untitled?node-id=0-1..."]
            direction LR

            subgraph leftpanel6["Panel izquierdo"]
                direction TB
                filename6["Untitled ▾"]
                filestatus6["Drafts   Free"]
                subgraph filetabs6["Tabs"]
                    direction LR
                    ft6_1(["File"])
                    ft6_2["Assets"]
                    ft6_search["🔍"]
                    ft6_1 ~~~ ft6_2 ~~~ ft6_search
                end
                subgraph pages6["Pages"]
                    direction LR
                    pages6_label["Pages"]
                    pages6_add["+"]
                    pages6_label ~~~ pages6_add
                end
                page6_1(["Page 1"])
                subgraph layers6["Layers"]
                    direction TB
                    ly_cardsmall["◇ Card - Small"]
                    ly_frame1["  Frame"]
                    ly_frame2["  Frame"]
                    ly_cardlarge["◇ Card - Large"]
                    ly_image["  Image"]
                    ly_vector["    Vector"]
                    ly_base["    Base"]
                    ly_frame3["  Frame"]
                    ly_frame4["  Frame"]
                    ly_frame5["  Frame"]
                    ly_btnsmall1["    ◇ Button - Small"]
                    ly_frame6["      Frame"]
                    ly_minwidth["      Min Width 64"]
                    ly_btnsmall2["    ◇ Button - Small"]
                    ly_device["◇ Device"]
                    ly_navbar["  Navigation Bar"]
                    ly_statusbar["  Status Bar"]
                    ly_cardsmall --> ly_frame1
                    ly_cardsmall --> ly_frame2
                    ly_cardlarge --> ly_image --> ly_vector
                    ly_image --> ly_base
                    ly_cardlarge --> ly_frame3
                    ly_cardlarge --> ly_frame4
                    ly_cardlarge --> ly_frame5
                    ly_frame5 --> ly_btnsmall1 --> ly_frame6
                    ly_btnsmall1 --> ly_minwidth
                    ly_frame5 --> ly_btnsmall2
                    ly_device --> ly_navbar
                    ly_device --> ly_statusbar
                end
                filename6 ~~~ filestatus6 ~~~ filetabs6 ~~~ pages6 ~~~ page6_1 ~~~ layers6
            end

            subgraph canvas6["Lienzo — dos frames Android Compact"]
                direction LR
                subgraph frameA["Frame A — 'Title' (Card grande)"]
                    direction TB
                    fa_status["12:30                ▼◀▮"]
                    fa_title["✕  Title        ↺ ↻ ⋮"]
                    subgraph fa_card1["Card"]
                        direction TB
                        fa_icon["☁ (icono)"]
                        fa_cardtitle["Title / Subtitle"]
                        fa_desc["Supporting or descriptive text for the card goes here like a pro."]
                        fa_btns["BUTTON   BUTTON ⏺"]
                        fa_icon ~~~ fa_cardtitle ~~~ fa_desc ~~~ fa_btns
                    end
                    subgraph fa_card2["Overline card"]
                        direction TB
                        fa2_over["OVERLINE"]
                        fa2_title["Title"]
                        fa2_desc["Supporting or descriptive text for the card goes here."]
                        fa2_icon["☁ (icono)"]
                        fa2_btns["BUTTON   BUTTON"]
                        fa2_over ~~~ fa2_title ~~~ fa2_desc ~~~ fa2_icon ~~~ fa2_btns
                    end
                    fa_nav["◁  ○  □"]
                    fa_status ~~~ fa_title ~~~ fa_card1 ~~~ fa_card2 ~~~ fa_nav
                end

                subgraph frameB["Frame B — 'Title' (Video + placeholder)"]
                    direction TB
                    fb_status["12:30                ▼◀▮"]
                    fb_title["✕  Title        ↺ ↻ ⋮"]
                    fb_video["▷ (reproductor de video)"]
                    fb_placeholder["☒ (placeholder de imagen)"]
                    fb_btns["BUTTON   BUTTON"]
                    fb_nav["◁  ○  □"]
                    fb_status ~~~ fb_title ~~~ fb_video ~~~ fb_placeholder ~~~ fb_btns ~~~ fb_nav
                end

                flowlabel(["Flow 1 ⧉"])
                frameA -- "interacción (Flow 1)" --> frameB
                flowlabel -.-> frameA
            end

            subgraph rightpanel6["Panel derecho"]
                direction TB
                subgraph rp6_top["Barra superior"]
                    direction LR
                    rp6_user["🔵 ▾"]
                    rp6_play["▷ ▾"]
                    rp6_share(["Share"])
                    rp6_user ~~~ rp6_play ~~~ rp6_share
                end
                subgraph rp6_tabs["Design / Prototype"]
                    direction LR
                    rp6_design["Design"]
                    rp6_proto(["Prototype"])
                    rp6_zoom["59% ▾"]
                    rp6_design ~~~ rp6_proto ~~~ rp6_zoom
                end
                rp6_settingslabel["Prototype settings"]
                rp6_device["Android Compact ▾"]
                subgraph rp6_bgrow["Fondo"]
                    direction LR
                    rp6_black["Black ▾"]
                    rp6_orient1["▯"]
                    rp6_orient2["▭"]
                    rp6_black ~~~ rp6_orient1 ~~~ rp6_orient2
                end
                rp6_color["■ 000000"]
                rp6_preview["(vista previa negra con marco de teléfono)"]
                rp6_flowslabel["Flows"]
                rp6_flow1["Flow 1"]
                subgraph rp6_note1["Removing a connection ✕"]
                    direction TB
                    rp6_note1_text["⌐× To delete a connection, click and drag on either end."]
                end
                subgraph rp6_note2["Running your prototype ✕"]
                    direction TB
                    rp6_note2_text["▷ Use the play button in the toolbar to play your prototype. If there are no connections, the play button can be used to play a presentation of your frames."]
                end
                rp6_top ~~~ rp6_tabs ~~~ rp6_settingslabel ~~~ rp6_device ~~~ rp6_bgrow ~~~ rp6_color ~~~ rp6_preview ~~~ rp6_flowslabel ~~~ rp6_flow1 ~~~ rp6_note1 ~~~ rp6_note2
            end

            leftpanel6 ~~~ canvas6 ~~~ rightpanel6
        end

        subgraph toolbar6["Barra flotante (abajo)"]
            direction LR
            t6_move(["▽ ▾"])
            t6_frame["⊞ ▾"]
            t6_rect["☐ ▾"]
            t6_pen["✎ ▾"]
            t6_text["T"]
            t6_ellipse["○"]
            t6_comp["⊞+"]
            t6_code["</>"]
            t6_move ~~~ t6_frame ~~~ t6_rect ~~~ t6_pen ~~~ t6_text ~~~ t6_ellipse ~~~ t6_comp ~~~ t6_code
        end

        help6["❓"]

        browser6 ~~~ toolbar6
    end

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    classDef figpurple fill:#A259FF,stroke:#A259FF,color:#ffffff
    classDef figblack fill:#000000,stroke:#000000,color:#ffffff
    class rp6_share figblue
    class rp6_proto figbluelt
    class flowlabel figbluelt
    class rp6_color figblack
    class rp6_preview figblack
    class ly_cardsmall figpurple
    class ly_cardlarge figpurple
    class ly_device figpurple
    class fa_btns figblack
    class fa2_btns figblack
    class fb_btns figblack
```

Luego puede simular las interacciones con el boton **play**

```mermaid
flowchart TB
    subgraph playcallout["Botón play (callout)"]
        direction LR
        pc_user["🔵 ▾"]
        pc_play(["▷ ▾"])
        pc_share["Share"]
        pc_user ~~~ pc_play ~~~ pc_share
    end
    subgraph playcallout_tabs["Design / Prototype"]
        direction LR
        pc_design["Design"]
        pc_proto(["Prototype"])
        pc_zoom["100% ▾"]
        pc_design ~~~ pc_proto ~~~ pc_zoom
    end
    arrow["🔴 (flecha roja señalando)"]
    playcallout ~~~ playcallout_tabs
    arrow --> pc_play

    classDef figblue fill:#0D99FF,stroke:#0D99FF,color:#ffffff
    classDef figred fill:#F24E1E,stroke:#F24E1E,color:#ffffff
    classDef figbluelt fill:#E5F4FF,stroke:#0D99FF,color:#0D99FF
    class pc_share figblue
    class pc_proto figbluelt
    class arrow figred
    linkStyle 5 stroke:#F24E1E,stroke-width:2px
```

E) Incorpore el texto necesario para cada pantalla donde se indique su propósito. Y otro texto de ayuda. Incluya un texto con su nombre, el titulo de su aplicacion, el Nombre del curso y Numero de Laboratorio.

---

## ANEXO: Temas sugeridos

### 1. Educación Inicial (3 a 6 años)

*Aplicaciones móviles con interfaces táctiles grandes, feedback visual/auditivo y modos para padres/educadores.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Mi Primer Diario" | Registro emocional diario mediante selección de caras y dibujo libre. | Pantalla principal con calendario visual. Cada día, el niño elige entre 5 emociones representadas por monstruos de colores. Pantalla de dibujo con trazo simple (dedo) que se guarda en una galería. Modo padres con resumen semanal de tendencias emocionales. |
| b) "Rutinas que Juegan" | Recordatorio interactivo de rutinas (lavarse los dientes, vestirse) usando historias cortas. | Pantalla de "aventura del día" con personaje que guía pasos. Botones gigantes para "comenzar" y "terminar". Cada rutina completada desbloquea una pegatina en un álbum. Notificaciones push suaves (con sonidos amigables) solo en horarios configurables por el adulto. |
| c) "Trazo Mágico" | Aprendizaje de grafomotricidad y letras con seguimiento del dedo. | Pantalla a pantalla completa sin bordes; el niño repasa formas y letras con el dedo. Feedback visual: el trazo se ilumina de verde si sigue el camino. Pantalla de resultados con estrellas y opción de repetir. Sección de progreso para adultos con métricas de precisión. |
| d) "Sonidos Escondidos" | Juego de memoria auditiva y asociación objeto-sonido. | Parrilla de tarjetas con dibujos. Al tocar cada tarjeta, suena un sonido (animal, instrumento). Pantalla de parejas: deben emparejar sonido con imagen. Interfaz sin texto, solo iconos grandes y coloridos. Control parental para ajustar dificultad. |
| e) "Cuéntame un Cuento" | Creación colaborativa de cuentos con grabación de voz del adulto y del niño. | Pantalla de creación: el adulto graba una página (voz) y el niño elige stickers para ilustrar. Luego se reproduce como un "cuento animado" con las voces grabadas. Biblioteca de cuentos en pantalla principal. Modo noche con fondo oscuro y sonidos relajantes. |

### 2. Medicina Veterinaria

*Apps móviles para dueños de mascotas, profesionales y estudiantes, con énfasis en gestión, telemedicina básica y educación.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "VetAssistant" | Guía de primeros auxilios y síntomas por reconocimiento visual. | Pantalla de inicio con selector de especie (perro/gato/conejo). Cámara integrada para tomar foto de síntoma (herida, ojo irritado) y devolver sugerencias de cuidado. Pantalla de resultados con lista de pasos a seguir y botón de "llamar al vet" con ubicación de clínicas cercanas. |
| b) "Dosis Justa" | Calculadora de medicamentos y recordatorio de tratamientos. | Pantalla de perfil de mascota (peso, edad, condición). Al escanear el envase del medicamento (código de barras), calcula dosis automáticamente. Calendario interactivo con alarmas programadas. Pantalla de historial de tratamientos con gráfico de cumplimiento. |
| c) "Mi Mascota al Día" | Registro de hábitos (alimentación, ejercicio, síntomas) con análisis simple. | Pantalla tipo "feed" donde se registran eventos con un toque (comió, bebió, hizo popó, vomitó). Vista de calendario y gráficos de barras simples. Pantalla de resumen semanal para compartir con el veterinario vía PDF. Notificaciones para recordar vacunas o desparasitaciones. |
| d) "Lenguaje Animal" | Traductor de sonidos y posturas mediante base de datos visual. | Pantalla con reproductor de sonidos típicos (ladrido, maullido) y descripción de su significado. Módulo de "posturas" con ilustraciones y texto explicativo. Quiz interactivo para aprender a interpretar señales. Diseño limpio, con pestañas (sonidos/posturas/aprende). |
| e) "VetConnect" | Teleconsulta asíncrona con envío de videos y chat estructurado. | Pantalla de inicio con lista de veterinarios disponibles. Chat plantillas para describir síntomas (dolor, ubicación, duración). Permite grabar video corto desde la app. Pantalla de historial de consultas con archivos adjuntos. Notificaciones de respuesta del profesional. |

### 3. Seguridad Ciudadana

*Apps móviles enfocadas en prevención, denuncia ágil, mapas colaborativos y educación, sin necesidad de hardware externo.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Ruta Segura" | Navegación peatonal que evita zonas con alta incidencia delictiva. | Pantalla de mapa con capas de calor (incidencias recientes). Al ingresar destino, muestra rutas alternativas con indicadores de seguridad (color verde a rojo). Pantalla de reporte: el usuario puede marcar rápidamente un incidente (robo, acoso) con categorías por iconos. Datos anónimos. |
| b) "Denuncia Rápida" | Formulario simplificado para denuncias no urgentes con evidencia multimedia. | Pantalla paso a paso: 1. Categoría (ruidos, abandono, alumbrado), 2. Tomar foto/video, 3. Ubicación automática, 4. Enviar. Interfaz minimalista con botones grandes. Pantalla de seguimiento con estado de la denuncia (recibida, en proceso, resuelta). |
| c) "Cuidado Mayor" | Aplicación para adultos mayores con botón de ayuda y verificación diaria. | Pantalla principal con un solo botón "Estoy bien" que deben pulsar cada mañana. Si no lo hacen, se envía alerta a familiar. Pantalla de contactos de confianza con foto grande. Modo de letra gigante y comandos por voz para leer mensajes. |
| d) "Escuela Segura" | Canal de comunicación entre padres y escuela sobre incidentes y protocolos. | Pantalla de inicio con notificaciones de simulacros o novedades. Módulo de "registro de salida" donde los padres confirman quién recoge al niño. Pantalla de reporte de incidentes (caídas, conflictos) con sello de tiempo. Diseño con perfiles separados para padres y personal escolar. |

### 4. Bienestar Emocional

*Apps móviles para manejo de estrés, seguimiento de ánimo, terapia asistida y comunidades de apoyo, con interfaces calmadas.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Ánimo Diario" | Registro de estado de ánimo con journaling guiado y análisis de patrones. | Pantalla de bienvenida con un selector visual de emociones (rueda de colores). Luego, pantalla para escribir libremente o responder preguntas suaves. Vista de calendario con colores que representan el ánimo. Gráficos de tendencia y sugerencias de actividades según el estado. |
| b) "Respiro" | Ejercicios de respiración y relajación con animaciones y sonidos. | Pantalla principal con lista de ejercicios (ansiedad, energía, dormir). Cada ejercicio muestra una animación que guía la respiración (un círculo que se expande y contrae). Temporizador visual. Pantalla de estadísticas con días de práctica consecutivos y sensación antes/después. |
| c) "Apoyo Mutuo" | Comunidad anónima para compartir experiencias y recibir apoyo. | Pantalla de inicio con feed de publicaciones breves (sin foto de perfil para anonimato). El usuario puede reaccionar con "me siento igual" o "gracias". Pantalla de categorías (ansiedad, duelo, estrés laboral). Módulo de recursos con líneas de ayuda y artículos. |
| d) "Mindful Kids" | Mindfulness para niños con cuentos interactivos y ejercicios de atención. | Pantalla de cuentos ilustrados que incluyen pausas para respirar o escuchar. Interfaz con personajes amigables. Pantalla de progreso con pegatinas desbloqueadas. Modo para padres con recomendaciones según la edad. |
| e) "Terapeuta Virtual" | Diario conversacional basado en terapia cognitivo-conductual (TCC). | Pantalla de chat con un asistente que formula preguntas estructuradas ("¿Qué pensamiento te causó malestar hoy?"). Ofrece ejercicios de reestructuración cognitiva en tarjetas. Pantalla de resumen semanal con insights y opción de compartir con terapeuta real. |

### 5. Servicios Municipales

*Apps móviles para interactuar con el gobierno local: reportes, trámites, participación ciudadana y cultura.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Reporta tu Barrio" | Denuncia de problemas urbanos (baches, basura, alumbrado) con geolocalización. | Pantalla de inicio con mapa interactivo. Botón grande "Nuevo reporte" que activa cámara y ubicación. Formulario en una sola pantalla con categorías por iconos. Pantalla de seguimiento con lista de reportes y estado (recibido, en proceso, resuelto). Notificaciones push de avances. |
| b) "Trámite Simple" | Guía paso a paso para realizar trámites municipales (licencias, impuestos). | Pantalla de buscador con palabras clave sencillas. Cada trámite se despliega en tarjetas con requisitos, costos y un botón "Iniciar" que lleva a una lista de pasos (con checklists). Integración con calendario para recordar fechas de vencimiento. |
| c) "Presupuesto Abierto" | Visualización del presupuesto municipal y votación de proyectos participativos. | Pantalla de inicio con gráficos circulares simples del gasto. Sección "Propuestas" con proyectos en votación. Cada proyecto tiene ficha con impacto estimado y botón de "apoyar". Pantalla de resultados con seguimiento de propuestas ganadoras. |
| d) "Mi Recolección" | Calendario de recolección de residuos con alertas y separación de materiales. | Pantalla principal con calendario mensual que muestra días de recolección por tipo (orgánico, reciclable). Configuración de dirección para personalizar. Pantalla de "¿Qué va en cada bolsa?" con infografías sencillas. Notificaciones recordatorio un día antes. |
| e) "Cultura Activa" | Agenda cultural local con registro de asistencia y gamificación. | Pantalla de inicio con lista de eventos cercanos (conciertos, talleres, ferias). Cada evento tiene ficha con mapa, horario y botón "me interesa". Al asistir, el usuario escanea un código QR en el lugar y acumula puntos canjeables por descuentos. Pantalla de perfil con logros. |

### 6. Monitoreo de Riesgos Naturales

*Aplicaciones centradas en la detección colaborativa de inundaciones, deslizamientos o sequías.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Alerta Inundación" | Monitoreo colaborativo de niveles de agua en ríos y quebradas mediante fotos referenciales. | Pantalla de mapa con puntos de reporte (verde: seguro, naranja: crecida, rojo: desborde). Al reportar, se abre un asistente para tomar foto de un "medidor natural" (escalera, poste) y geolocalizarlo. Pantalla de historial de niveles por zona. |
| b) "Suelo Firme" | Reporte de grietas, hundimientos o movimientos de tierra en laderas urbanas. | Pantalla con checklist visual (fotos de ejemplo de grietas leves, moderadas y graves). El usuario toma 2 fotos (general y detalle) y el app calcula la inclinación del terreno usando el giroscopio. Pantalla de alerta vecinal: notifica a residentes cercanos en radio de 500m. |

### 7. Calidad del Aire y Salud

*Apps que miden la contaminación atmosférica y recomiendan acciones preventivas.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Respira Bien" | Estimación de calidad del aire basada en datos satelitales y densidad de reportes de usuarios (olfato, niebla). | Pantalla principal con índice de calidad del aire (ICA) en colores (verde a morado). Módulo de "síntomas": el usuario registra irritación de ojos, tos o fatiga, y el app correlaciona con zonas de alto riesgo. Pantalla de recomendación: sugiere usar mascarilla o evitar horarios de alto tráfico. |
| b) "Polen Alert" | Monitoreo de concentración de polen y esporas de hongos (alérgenos) vinculado al cambio climático. | Pantalla con calendario estacional y mapa de calor de polen por distrito. El usuario registra su nivel de alergia diario (leve, moderado, grave) y el app genera una "previsión de riesgo" para los próximos 3 días. Configuración de alertas push cuando el polen supera umbral personalizado. |

### 8. Gestión del Agua y Sequía

*Herramientas para medir el estrés hídrico y fomentar el ahorro.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Gotero" | Registro colaborativo de cortes de agua, baja presión y calidad del suministro. | Pantalla de reporte rápido con 3 iconos grandes: "Sin agua", "Baja presión", "Agua turbia". Al enviar, adjunta ubicación y hora automática. Pantalla de tendencias: gráfico de barras que muestra la frecuencia de cortes por barrio, útil para exigir políticas hídricas. |
| b) "Huella Hídrica" | Calculadora de consumo de agua en actividades diarias (ducha, riego, lavado) y metas de ahorro. | Pantalla principal con un medidor animado que gira de rojo a verde según el consumo semanal. Módulo de "desafíos": ej. "Reducir 2 min de ducha" con temporizador integrado. Pantalla de comparación social (anónima) para motivar a la comunidad a ahorrar agua. |

### 9. Energía y Huella de Carbono

*Apps que miden y reducen la huella de carbono personal o vecinal.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Carbono Diario" | Calculadora de huella de carbono basada en transporte, alimentación y electricidad. | Pantalla de "registro rápido" con botones deslizantes: ¿usaste carro? ¿comiste carne? ¿dejaste luces encendidas?. Al final del día, muestra un "termómetro de carbono" con meta diaria. Pantalla de "compensación": sugiere árboles a plantar (o donaciones a proyectos locales) según el exceso de emisiones. |
| b) "Solar Vecino" | Monitoreo colaborativo de techos con potencial solar y reporte de sombras o árboles que bloquean luz. | Pantalla con cámara en realidad aumentada (RA): el usuario apunta al techo y el app estima la radiación solar incidente (usando sensor de luz y GPS). Mapa comunitario donde se ven casas con paneles solares y el ahorro estimado. Foro de preguntas entre vecinos sobre instalación. |

### 10. Educación, Árboles y Refugios Climáticos

*Apps que fomentan la adaptación y el cuidado de la vegetación urbana.*

| Aplicación | Funcionalidad Principal | Características de Pantallas (UI/UX Móvil) |
|---|---|---|
| a) "Árbol Amigo" | Inventario participativo de árboles urbanos, su salud y beneficios (sombra, CO2). | Pantalla de mapa con íconos de árboles (verde=sano, amarillo=estresado, rojo=caído). Al agregar un árbol, el app guía para tomar foto del tronco, copa y suelo. Pantalla de "riego colaborativo": los vecinos se apuntan para regar árboles jóvenes en época de sequía, con recordatorios por zona. |
| b) "Refugio Climático" | Mapa de espacios frescos (parques, centros comerciales, bibliotecas) y rutas seguras ante olas de calor. | Pantalla principal con mapa de "islas de calor" generado por reportes de temperatura (el usuario puede reportar sensación térmica). Al ingresar "buscar refugio", muestra el lugar más fresco cercano con sombra y agua potable. Pantalla de "alerta calor": notifica cuando la sensación térmica supera los 38°C y sugiere vestimenta e hidratación. |

```mermaid
    flowchart TB
    Splash((Splash))
    Login[Login]
    Registro[Registro]
    Home[["Home — Mapa de calor"]]
    Reportar[Reportar sensación]
    Resultados[Refugios cercanos]
    Detalle[Detalle de refugio]
    Ruta[Ruta segura]
    Alerta[Alerta de calor]
    Perfil[Perfil]

    Splash --> Login
    Splash --> Registro
    Login --> Splash
    Login --> Home
    Login --> Registro
    Registro --> Login
    Registro --> Home

    Home --> Reportar
    Reportar --> Home
    Home --> Resultados
    Resultados --> Detalle
    Detalle --> Ruta
    Ruta --> Home
    Detalle --> Resultados
    Ruta --> Detalle

    Home <--> Resultados
    Home <--> Alerta
    Home <--> Perfil
    Resultados <--> Alerta
    Resultados <--> Perfil
    Alerta <--> Perfil
    Alerta --> Resultados

    Perfil --> Splash

    linkStyle 0 stroke:#7B2FF7,stroke-width:2px
    linkStyle 1 stroke:#7B2FF7,stroke-width:2px
    linkStyle 2 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 3 stroke:#FF7A45,stroke-width:2px
    linkStyle 4 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 5 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 6 stroke:#FF7A45,stroke-width:2px
    linkStyle 7 stroke:#FF7A45,stroke-width:2px
    linkStyle 8 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 9 stroke:#2F80ED,stroke-width:2px
    linkStyle 10 stroke:#2F80ED,stroke-width:2px
    linkStyle 11 stroke:#2F80ED,stroke-width:2px
    linkStyle 12 stroke:#2F80ED,stroke-width:2px
    linkStyle 13 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 14 stroke:#A8A29E,stroke-width:1.5px
    linkStyle 15 stroke:#E5484D,stroke-width:2px
    linkStyle 16 stroke:#E5484D,stroke-width:2px
    linkStyle 17 stroke:#E5484D,stroke-width:2px
    linkStyle 18 stroke:#E5484D,stroke-width:2px
    linkStyle 19 stroke:#E5484D,stroke-width:2px
    linkStyle 20 stroke:#E85D2A,stroke-width:2px
    linkStyle 21 stroke:#A8A29E,stroke-width:1.5px
```