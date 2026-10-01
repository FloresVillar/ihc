"""Genera los SVG del archivo Figma "tutorial figma", organizados por página.

Las medidas (posiciones, tamaños, colores, imágenes e iconos) salen de los
exports de Figma en ../figma_export/. Los textos se escriben como <text>
editable: la posición de cada línea se calcula con las métricas reales de la
fuente para que la tinta caiga donde estaba en el original.

Requiere cairosvg, numpy, pillow y las fuentes Inter/Asap instaladas por peso
(familias "Inter W400", "Asap W800", ...) solo para medir; el SVG final usa
font-family="Inter" + font-weight, que es lo que Figma entiende.
"""
import base64, functools, io, json, os, re
from xml.sax.saxutils import escape

import cairosvg
import numpy as np
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.join(AQUI, '..', 'figma_export')
IMG = os.path.join(AQUI, 'recursos')

# ---------------------------------------------------------------- estilos
# (familia, peso, tamaño, color, opacidad) ajustados contra los originales
ESTILOS = {
    'nav_nombre': ('Inter', 800, 20, 'black', 1),
    'nav_link':   ('Inter', 900, 20, 'black', 1),
    'boton':      ('Inter', 600, 20, 'white', 1),
    'bio_titulo': ('Asap', 800, 48.5, 'black', 1),
    'bio_parrafo': ('Inter', 400, 18, 'black', 0.8),
    'encabezado': ('Inter', 700, 28, 'black', 1),
    'tar_titulo': ('Inter', 600, 28, 'black', 1),
    'tar_desc':   ('Inter', 500, 20, 'black', 1),
    'habilidad':  ('Inter', 700, 40, 'black', 1),
    'secundario': ('Inter', 500, 20, 'black', 1),
    'cita':       ('Inter', 700, 18, 'black', 1),
    'bloque_txt': ('Inter', 700, 18, 'black', 1),
    'impactante': ('Inter', 800, 63.5, 'black', 1),
}


def _familia_render(fam, peso):
    return f'{fam} W{peso}' if fam in ('Inter', 'Asap') else fam


@functools.lru_cache(None)
def tinta(texto, fam, peso):
    """Caja de tinta del texto a 100px con baseline en y=0: (izq, der, arriba, abajo)."""
    W = len(texto) * 90 + 200
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="300">'
           f'<rect width="{W}" height="300" fill="white"/>'
           f'<text x="50" y="200" font-family="{_familia_render(fam, peso)}" font-size="100" '
           f'xml:space="preserve">{escape(texto)}</text></svg>')
    a = np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert('L')) < 128
    ys, xs = np.where(a)
    return xs.min() - 50, xs.max() - 50, ys.min() - 200, ys.max() - 200


def ancho(texto, estilo):
    fam, peso, tam, *_ = ESTILOS[estilo]
    l, r, _, _ = tinta(texto, fam, peso)
    return (r - l + 1) * tam / 100


def T(texto, estilo, izq, arriba, nombre=None):
    """<text> cuya tinta empieza en (izq, arriba), como en el original."""
    fam, peso, tam, color, op = ESTILOS[estilo]
    l, _, t, _ = tinta(texto, fam, peso)
    x = izq - l * tam / 100
    y = arriba - t * tam / 100
    extra = f' fill-opacity="{op}"' if op != 1 else ''
    idattr = f' id="{escape(nombre)}"' if nombre else ''
    return (f'<text{idattr} x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-weight="{peso}" '
            f'font-size="{tam}" fill="{color}"{extra} xml:space="preserve">{escape(texto)}</text>')


def lineas(pares, estilo, izq, nombre):
    return f'<g id="{nombre}">' + ''.join(T(t, estilo, izq, y) for t, y in pares) + '</g>'


def repetir(prefijo, letra, sufijo, objetivo, estilo):
    """Relleno tipo 'nnnn…' con tantas letras como quepan en el ancho medido."""
    n = 1
    while ancho(prefijo + letra * (n + 1) + sufijo, estilo) <= objetivo + 2:
        n += 1
    return prefijo + letra * n + sufijo


# ---------------------------------------------------------------- imágenes
_defs = []
_ids = {}


def img_b64(nombre):
    with open(os.path.join(IMG, nombre), 'rb') as f:
        return base64.b64encode(f.read()).decode()


def rect_imagen(x, y, w, h, archivo, nombre, forma='rect', rx=0):
    """Relleno de imagen modo FILL (cubrir y centrar), igual que exporta Figma."""
    iw, ih = Image.open(os.path.join(IMG, archivo)).size
    pid, iid = f'pat{len(_defs)}', _ids.setdefault(archivo, f'img{len(_ids)}')
    esc = max(w / iw, h / ih)
    sx, sy = esc * iw / w, esc * ih / h
    ox, oy = (1 - sx) / 2, (1 - sy) / 2
    _defs.append(f'<pattern id="{pid}" patternContentUnits="objectBoundingBox" width="1" height="1">'
                 f'<use xlink:href="#{iid}" transform="matrix({sx / iw:.8f} 0 0 {sy / ih:.8f} {ox:.6f} {oy:.6f})"/></pattern>')
    if forma == 'elipse':
        return f'<ellipse id="{nombre}" cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2}" ry="{h / 2}" fill="url(#{pid})"/>'
    r = f' rx="{rx}"' if rx else ''
    return f'<rect id="{nombre}" x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="url(#{pid})"/>'


def imagen_desplazada(x, y, w, h, archivo, nombre, m):
    """Relleno con la matriz exacta que usó Figma (recortes a mano)."""
    pid, iid = f'pat{len(_defs)}', _ids.setdefault(archivo, f'img{len(_ids)}')
    _defs.append(f'<pattern id="{pid}" patternContentUnits="objectBoundingBox" width="1" height="1">'
                 f'<use xlink:href="#{iid}" transform="matrix({m})"/></pattern>')
    return f'<rect id="{nombre}" x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{pid})"/>'


def svg(w, h, cuerpo, fondo='white'):
    imgs = []
    for archivo, iid in _ids.items():
        iw, ih = Image.open(os.path.join(IMG, archivo)).size
        imgs.append(f'<image id="{iid}" width="{iw}" height="{ih}" xlink:href="data:image/png;base64,{img_b64(archivo)}"/>')
    bg = f'<rect width="{w}" height="{h}" fill="{fondo}"/>' if fondo else ''
    out = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" '
           f'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n'
           f'{bg}\n{cuerpo}\n<defs>\n' + '\n'.join(_defs + imgs) + '\n</defs>\n</svg>\n')
    _defs.clear(); _ids.clear()
    return out


def grupo(nombre, dx, dy, contenido):
    t = f' transform="translate({dx} {dy})"' if dx or dy else ''
    return f'<g id="{nombre}"{t}>\n{contenido}\n</g>'


# ---------------------------------------------------------------- iconos
ICONOS_PATH = json.load(open(os.path.join(IMG, 'iconos.json')))
# nombre: (índice del path, origen del marco en coords de "lista de habilidades", tamaño)
ICONOS = {
    'gusano':   (0, (337, 14.5), (48, 48)),
    'diamante': (1, (707, 15), (48, 48)),
    'flor':     (2, (1079, 16.5), (44, 44)),
    'ala':      (3, (343, 145), (42, 44)),
    'arco':     (4, (711, 147), (43, 39)),
}


def icono(nombre, x, y):
    i, (ox, oy), _ = ICONOS[nombre]
    return (f'<g id="{nombre}" transform="translate({x - ox} {y - oy})">'
            f'<path d="{ICONOS_PATH[i]}" fill="#D9D9D9"/></g>')


# ---------------------------------------------------------------- componentes
LINKS = 5


def boton_principal(x, y, w=209, h=52, dx_txt=10.5, dy_txt=18):
    return (f'<g id="boton principal"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="black"/>'
            + T('continuar/siguiente', 'boton', x + dx_txt, y + dy_txt) + '</g>')


def boton_secundario(x, y):
    return (f'<g id="boton/secundario"><rect x="{x + 0.5}" y="{y + 0.5}" width="167" height="53" rx="7.5" '
            f'fill="white" stroke="#A76A6A"/>' + T('volver arriba ↑', 'secundario', x + 12, y + 19) + '</g>')


def navegacion(nombre_x, nombre_y, links_x, links_y, boton_xy, con_boton=True, fondo=None):
    w, h = fondo or (0, 0)
    s = f'<rect width="{w}" height="{h}" fill="white"/>' if fondo else ''
    s += T('Nombre Apellido', 'nav_nombre', nombre_x, nombre_y, 'nombre')
    s += '<g id="links">' + ''.join(T('link', 'nav_link', links_x + i * 94, links_y) for i in range(LINKS)) + '</g>'
    if con_boton:
        s += boton_principal(*boton_xy)
    return s


BIO_TITULO_ANCHO = [('hola, Estudiante de ciencia de la', 242), ('computacion', 304)]
BIO_TITULO_ANGOSTO = [('hola, Estudiante de ciencia de', 242), ('la computacion', 304)]
BIO_P_ANCHO = [
    ('las armas militares de españoles catolicos valientes,que por ignotos y soberbios mares,fueron a dominar', 386),
    ('remotas gentes,jamaz por los antiguos escchados,no menos el gusto a la adelfa llega,que al cardamo y', 415),
    ('cañamo oloroso,pues todo lo vuelve provechoso ,despues de a que a su sutil boca se apega.Poniendo el', 444),
    ('verbo eternos en los altares, que en otro tiempo de espanto gentilicos.', 473),
    ('Por haber dado a nuestras vidas,mas solo 270 fueron cosa maravillasa los de españa, que en tan poco numero', 518),
    ('lograron tan memorable y alta hazaña , no se acobardaron ni temieron por ver que gente salia a batalla, antes', 563),
    ('les dio fe y esperanza , el auxilio de Dios y de su lanza.', 592),
]
BIO_P_ANGOSTO = [
    ('las armas militares de españoles catolicos valientes,que por ignotos y', 386),
    ('soberbios mares,fueron a dominar remotas gentes,jamaz por los antiguos', 415),
    ('escchados,no menos el gusto a la adelfa llega,que al cardamo y cañamo', 444),
    ('oloroso,pues todo lo vuelve provechoso ,despues de a que a su sutil boca', 473),
    ('se apega.Poniendo el verbo eternos en los altares, que en otro tiempo de', 502),
    ('espanto gentilicos.', 531),
    ('Por haber dado a nuestras vidas,mas solo 270 fueron cosa maravillasa los', 576),
    ('de españa, que en tan poco numero', 605),
    ('lograron tan memorable y alta hazaña , no se acobardaron ni temieron por', 650),
    ('ver que gente salia a batalla, antes les dio fe y esperanza , el auxilio de Dios', 679),
    ('y de su lanza.', 709),
]


def biografia(angosta=False):
    s = rect_imagen(104, 63, 152, 144, 'avatar.png', 'foto', forma='elipse')
    s += lineas(BIO_TITULO_ANGOSTO if angosta else BIO_TITULO_ANCHO, 'bio_titulo', 107, 'titulo')
    s += lineas(BIO_P_ANGOSTO if angosta else BIO_P_ANCHO, 'bio_parrafo', 105, 'parrafo')
    return s


def encabezado(texto, x, y=66):
    return T(texto, 'encabezado', x, y, 'texto')


def tarjeta(dx, imagen, tops=(99, 157, 189)):
    """dx = desplazamiento de la columna de texto respecto a la versión de diseños (x=536)."""
    s = rect_imagen(73.5 + dx, 88, 430, 347, imagen, 'imagen')
    s += T('Titulo del proyecto', 'tar_titulo', 536 + dx, tops[0], 'titulo')
    s += lineas([('Una breve descripcion del proyecto , que resume', tops[1]),
                 ('algunas caracteristicas', tops[2])], 'tar_desc', 537 + dx, 'descripcion')
    s += boton_principal(535.5 + dx, 229, 201, 48, 6.5, 16)
    return s


def habilidades(dx=0):
    col = [
        (26, [('diseño web', 23)]), (26, [('empatia con el', 127), ('usuario', 175)]),
        (394, [('trabajo en', 0), ('equipo', 47)]), (394, [('proyectos con', 106), ('data', 152), ('almacenada', 200)]),
        (763, [('diseño', 0), ('conceptual', 48)]),
    ]
    s = ''.join(lineas(p, 'habilidad', x + dx, p[0][0]) for x, p in col)
    for n, (_, (ox, oy), _) in ICONOS.items():
        s += icono(n, ox + dx, oy)
    return s


def texto_impactante(x_txt, fondo):
    s = fondo
    s += lineas([('El titulo deber ser lo mas grande', 115), ('posible', 217)], 'impactante', x_txt, 'titulo')
    return s


def bloque_texto(dx=0):
    E = 'bloque_txt'
    L = [
        'dsjdds jjaj dajs jaj jajs ja jjasjda jsdj jasjd ajj djaj jja sjas jja sdjajs jaj jdasjdjasjdajsdj jd jaj djsaj daj djasj dja jdajs',
        'djajs js jdaj ja jaj jajs jdaj sjda jajsj dajs jajs jasj djas jdaj jajs jajs jasj jjajsdjajsjajdjajs djajjajajjajsdjasj djasj djasj',
        'jajja jja jjdja j jsjs jjs jdj sj dadsad mdan nasndn an nasndn asn dnasn dna nn nasn nnn nansn nnnnn da asda sda s',
        'sad as sa            ns djansj ans jajs nsn jsj jsn njs jajs djjs jjsjnasjd nsnj jasj jasj jns jdj jjas jjns jsjn jsaj jasj jsjn',
        repetir('jjsjjsj', 'n', '', 995, E),
        repetir('', 'n', '', 994, E), repetir('', 'n', '', 994, E), repetir('', 'n', '', 916, E),
        repetir('ns', 'j', 'd s', 551, E),
    ]
    # la primera línea fija la baseline; el resto va cada 29px
    fam, peso, tam, *_ = ESTILOS[E]
    base = 63 - tinta(L[0], fam, peso)[2] * tam / 100
    s = '<g id="texto">'
    for i, t in enumerate(L):
        l = tinta(t, fam, peso)[0]
        x = 1 + dx - l * tam / 100 if i not in (2, 4) else 0 + dx - l * tam / 100
        s += (f'<text x="{x:.2f}" y="{base + 29 * i:.2f}" font-family="{fam}" font-weight="{peso}" '
              f'font-size="{tam}" fill="black" xml:space="preserve">{escape(t)}</text>')
    return s + '</g>'


def cita(x=24, y=63):
    return T('texto de relleno jasjd jajd jajsd jajs jasj js jj jaj s jjj jj j j', 'cita', x, y, 'texto')


# ---------------------------------------------------------------- páginas
def pagina_disenos():
    home = [
        grupo('navegacion', 0, 0, navegacion(74, 45, 388, 50, (864.5, 36), fondo=(1147, 124))),
        grupo('biografia personal', 0, 232, biografia()),
        grupo('encabezado de seccion', 0, 1017, encabezado('trabajo', 527)),
    ]
    for i, (y, im) in enumerate([(1218, 'proyecto_orden_compra.png'), (1849, 'placeholder.png'), (2480, 'placeholder.png')]):
        home.append(grupo('tarjeta proyecto' + (f'-{i}' if i else ''), 0, y, tarjeta(0, im)))
    home += [
        grupo('lista de habilidades', 0, 3111, habilidades()),
        grupo('pie de pagina', 0, 3448, navegacion(25, 46, 507, 51, None, con_boton=False, fondo=(967, 126))),
        boton_secundario(977, 3496),
    ]
    home_svg = svg(1155, 3574, '\n'.join(home))  # antes de armar 'caso': svg() consume las imágenes pendientes
    caso = [
        grupo('navegacion', 39.5, 0, navegacion(35, 45, 349, 50, (824.5, 36), fondo=(1068, 124))),
        grupo('texto impactante', 0, 232, texto_impactante(43, imagen_desplazada(
            0, 0, 1147, 367, 'flujo_pedidos.png', 'imagen', '0.00111235 0 0 0.00347646 0 -0.330875'))),
        grupo('bloque de texto', 73, 707, bloque_texto()),
        grupo('encabezado de seccion', 0, 1188, encabezado('topico', 527)),
        grupo('bloque de imagen', 73.5, 1389, imagen_desplazada(
            69.5, 56, 861, 310, 'tabla_ordenes.png', 'imagen', '0.00065822 0 0 0.00182815 -0.0986513 0')),
        grupo('bloque de cita', 289, 1919, cita()),
        grupo('lista de habilidades', 0, 2168, habilidades()),
        grupo('pie de pagina', 39, 2505, navegacion(35, 46, 598, 51, None, con_boton=False, fondo=(1068, 126))),
    ]
    return {'home': home_svg, 'caso de estudio': svg(1147, 2631, '\n'.join(caso))}


def pagina_componentes():
    c = {}
    c['navegacion'] = svg(996, 80, navegacion(25, 23, 287, 28, (762.5, 14)))
    c['pie de pagina'] = svg(996, 80, navegacion(25, 23, 536, 28, None, con_boton=False))
    c['biografia personal'] = svg(852, 793, biografia(angosta=True), fondo=None)
    c['encabezado de seccion'] = svg(142, 94, encabezado('topico', 24), fondo=None)
    c['tarjeta proyecto'] = svg(1000, 498, tarjeta(-36, 'placeholder.png', (99, 156, 188)), fondo=None)
    c['texto impactante'] = svg(1241, 367, texto_impactante(90, rect_imagen(0, 0, 1241, 367, 'placeholder.png', 'imagen')))
    c['bloque de texto'] = svg(1001, 373, bloque_texto(), fondo=None)
    c['bloque de imagen'] = svg(909, 422, rect_imagen(24.5, 56, 861, 310, 'placeholder.png', 'imagen'), fondo=None)
    c['bloque de cita'] = svg(570, 141, cita(), fondo=None)
    c['lista de habilidades'] = svg(1223, 229, habilidades(38), fondo=None)
    c['boton principal'] = svg(209, 52, boton_principal(0, 0, 209, 52, 11, 18), fondo=None)
    c['boton/boton'] = svg(168, 54, boton_secundario(0, 0).replace('boton/secundario', 'boton'), fondo=None)
    for n, (_, (ox, oy), (w, h)) in ICONOS.items():
        c[n] = svg(w, h, icono(n, 0, 0), fondo=None)
    return c


# exploraciones: medidas de get_metadata + textos leídos de la captura (escala 0.395)
def pagina_exploraciones():
    E = dict(ESTILOS)
    ESTILOS.update({
        'exp_titulo': ('Inter', 700, 76, 'black', 1),
        'exp_topico': ('Inter', 700, 28, 'black', 1),
        'exp_cita': ('Inter', 400, 28, 'black', 1),
        'exp_parrafo': ('Inter', 400, 28, 'black', 1),
    })
    cita_l = ['dfjsfj sjf jsjf jdf jj jdjfsj js jsj jsd  sld fd', 'llssdfsj j jsjd js jsjssssssssssssss jsjd jsjd',
              'sfjdj jsjd js jsj jsj djj jj jfsjjsljjejogtuhndu fus', 'nsud sn u']
    par = ['hdshdas hahdhashd basdab hd abshd absdh absdha bsdah da hsdabsdah', 'hahb ahsh abd bad basd asdbh ahsdhashdahs',
           repetir('hashdahsdhahsdahshah', 'h', '', 987, 'exp_parrafo'), repetir('', 'h', 'shd', 562, 'exp_parrafo'),
           repetir('hashdah', 'h', '', 992, 'exp_parrafo'), repetir('', 'h', 'sh', 663, 'exp_parrafo'),
           repetir('ahshah', 'h', 'ahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 997, 'exp_parrafo'), 'aaaaaaahahaha']
    s = [grupo('Frame 1', 0, 110, rect_imagen(0, 0, 1440, 440, 'placeholder.png', 'fondo')
               + T('Titulo', 'exp_titulo', 720 - ancho('Titulo', 'exp_titulo') / 2, 30, 'titulo')),
         grupo('encabezado de seccion', 664, 575, T('Topico 1', 'exp_topico', 56.5 - ancho('Topico 1', 'exp_topico') / 2, 8)),
         grupo('cita', 435, 645, ''.join(T(t, 'exp_cita', 285 - ancho(t, 'exp_cita') / 2, 10 + 45.5 * i) for i, t in enumerate(cita_l))),
         grupo('texto de parrafo', 220, 850, ''.join(T(t, 'exp_parrafo', 0, 10 + 45.3 * i) for i, t in enumerate(par))),
         grupo('imagen', 220, 1235, rect_imagen(0, 0, 1000, 562, 'diagrama_exploracion.png', 'imagen', rx=8))]
    ESTILOS.clear(); ESTILOS.update(E)
    return {'exploracion de casos': svg(1440, 1850, '\n'.join(s))}


def pagina_4():
    # solo se conocen nombres y tamaños (get_metadata); posiciones y colores son los de Figma por defecto
    return {
        'Rectangle 2': svg(97, 100, '<rect id="Rectangle 2" width="97" height="100" fill="#D9D9D9"/>', fondo=None),
        'Frame 1': svg(155, 230, '<rect id="Rectangle 1" x="33.5" y="82" width="88" height="66" fill="#D9D9D9"/>'),
        'Frame 2': svg(124, 218, ''),
    }


PAGINAS = [('01_exploraciones', pagina_exploraciones), ('02_page_4', pagina_4),
           ('03_disenos', pagina_disenos), ('04_componentes', pagina_componentes)]

if __name__ == '__main__':
    for carpeta, fn in PAGINAS:
        for nombre, contenido in fn().items():
            ruta = os.path.join(AQUI, carpeta, nombre + '.svg')
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, 'w') as f:
                f.write(contenido)
            print(f'{carpeta}/{nombre}.svg  {len(contenido) // 1024} KB')
