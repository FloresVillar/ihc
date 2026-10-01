"""Compara los SVG generados contra los exports originales de Figma.

Por cada par guarda comparacion/<nombre>.png (original | generado | diferencias)
y un resumen con dos medidas:
  - similitud: 1 - diferencia media absoluta / 255 sobre todo el lienzo
  - tinta exacta: de los píxeles con contenido (en cualquiera de las dos
    imágenes), cuántos coinciden con diferencia < 40 niveles. Es la medida dura:
    el blanco no la infla, y castiga el suavizado distinto de cada motor.
  - tinta ±1px: F1 entre las tintas, aceptando 1px de desvío. Mide posición.
"""
import io, os, re, sys
import cairosvg, numpy as np
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.join(AQUI, '..', 'figma_export')
OUT = os.path.join(AQUI, 'comparacion')
os.makedirs(OUT, exist_ok=True)


def fuentes_render(txt):
    # font-family="Inter" font-weight="800" -> "Inter W800" (instancias locales por peso)
    return re.sub(r'font-family="(Inter|Asap)" font-weight="(\d+)"', r'font-family="\1 W\2"', txt)


def patrones_a_imagenes(t):
    """cairosvg repite (tile) los rellenos de imagen con desplazamiento; Figma no.
    Para comparar, cada relleno pattern se cambia por <image> recortada a la forma."""
    pats = {m[0]: m[1:] for m in re.findall(
        r'<pattern id="([^"]+)"[^>]*>\s*<use xlink:href="#([^"]+)" transform="matrix\(([^)]+)\)"/>\s*</pattern>', t)}
    imgs = {m[0]: m[1:] for m in re.findall(r'<image id="([^"]+)" width="([\d.]+)" height="([\d.]+)"[^>]*xlink:href="([^"]+)"', t)}
    k = [0]

    def rep(m):
        el, pid = m.group(0), m.group(2)
        if pid not in pats: return el
        iid, mat = pats[pid]; a, _, _, d, e, f = map(float, mat.split())
        iw, ih, href = imgs[iid]
        at = lambda n, dflt=0: float(re.search(n + r'="([-\d.]+)"', el).group(1)) if re.search(' ' + n + r'="', el) else dflt
        if el.startswith('<ellipse'):
            cx, cy, rx, ry = at('cx'), at('cy'), at('rx'), at('ry'); x, y, w, h = cx - rx, cy - ry, 2 * rx, 2 * ry
            forma = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>'
        else:
            x, y, w, h = at('x'), at('y'), at('width'), at('height')
            tr = re.search(r'transform="translate\(([-\d.]+)(?:[ ,]([-\d.]+))?\)"', el)
            if tr: x += float(tr.group(1)); y += float(tr.group(2) or 0)
            forma = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{at("rx")}"/>'
        k[0] += 1; cid = f'cmp{k[0]}'
        return (f'<clipPath id="{cid}">{forma}</clipPath><image clip-path="url(#{cid})" x="{x + e * w}" y="{y + f * h}" '
                f'width="{float(iw) * a * w}" height="{float(ih) * d * h}" preserveAspectRatio="none" xlink:href="{href}"/>')
    return re.sub(r'<(rect|ellipse)[^>]*fill="url\(#([^)]+)\)"[^>]*/>', rep, t)


def render(ruta, ancho=None, generado=False):
    if ruta.endswith('.png'):
        im = Image.open(ruta).convert('RGBA')
    else:
        t = open(ruta).read()
        if generado:
            t = fuentes_render(t)
        t = patrones_a_imagenes(t)
        w = int(re.search(r'width="([\d.]+)"', t).group(1)); h = int(re.search(r'height="([\d.]+)"', t).group(1))
        # 4x y reducir: evita el hinting de cairo en textos pequeños (Figma no hace hinting)
        im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=t.encode(), output_width=w * 4, output_height=h * 4))).convert('RGBA')
        im = im.resize((w, h), Image.LANCZOS)
    bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3])
    return bg


def comparar(nombre, original, generado, recorte=None, escala=None):
    a = render(original)
    b = render(generado, generado=True)
    if recorte: a = a.crop(recorte)
    if escala or a.size != b.size:
        b = b.resize(a.size, Image.LANCZOS)
    A = np.asarray(a).astype(float).mean(2); B = np.asarray(b).astype(float).mean(2)
    d = np.abs(A - B)
    sim = 1 - d.mean() / 255
    tinta = (A < 235) | (B < 235)
    coinc = (d[tinta] < 40).mean() if tinta.any() else 1
    # ±1px: tinta de cada imagen que tiene tinta de la otra a 1px o menos (F1)
    from PIL import ImageFilter
    ma, mb = A < 160, B < 160
    dil = lambda m: np.asarray(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.MaxFilter(3))) > 0
    if ma.any() and mb.any():
        p, r = (mb & dil(ma)).sum() / mb.sum(), (ma & dil(mb)).sum() / ma.sum(); tol = 2 * p * r / (p + r)
    else:
        tol = 1.0
    # imagen: original | generado | diferencias (rojo)
    dif = Image.fromarray(np.dstack([np.full_like(d, 255), 255 - d, 255 - d]).astype('uint8'))
    W, H = a.size; esc = min(1, 700 / W)
    tiles = [x.resize((int(W * esc), int(H * esc))) for x in (a, b, dif)]
    lienzo = Image.new('RGB', (tiles[0].width * 3 + 40, tiles[0].height + 30), (235, 235, 235))
    dr = ImageDraw.Draw(lienzo)
    for i, (t, et) in enumerate(zip(tiles, ('original', 'generado', 'diferencias'))):
        lienzo.paste(t, (i * (t.width + 20), 30)); dr.text((i * (t.width + 20) + 4, 8), et, fill=(180, 0, 0))
    lienzo.save(os.path.join(OUT, nombre.replace('/', '-') + '.png'))
    return sim, coinc, tol


C = os.path.join(EXP, 'componentes')
G = os.path.join(AQUI, '04_componentes')
pares = [('03 diseños / home', os.path.join(EXP, 'home.svg'), os.path.join(AQUI, '03_disenos', 'home.svg'), None, None),
         ('03 diseños / caso de estudio', os.path.join(EXP, 'caso de estudio.svg'), os.path.join(AQUI, '03_disenos', 'caso de estudio.svg'), None, None)]
for n in ['navegacion', 'pie de pagina', 'biografia personal', 'encabezado de seccion', 'tarjeta proyecto', 'texto impactante',
          'bloque de texto', 'bloque de imagen', 'bloque de cita', 'lista de habilidades', 'boton principal', 'boton/boton',
          'gusano', 'diamante', 'flor', 'ala', 'arco']:
    pares.append((f'04 componentes / {n}', os.path.join(C, n + '.png'), os.path.join(G, n + '.svg'), None, None))
k = 569 / 1440
pares.append(('01 exploraciones / exploracion de casos', '/home/esau/ihc/imagenes/Captura de pantalla 2026-09-23 133503.png',
              os.path.join(AQUI, '01_exploraciones', 'exploracion de casos.svg'), (709, 130, 709 + 569, 130 + round(1850 * k)), k))

if __name__ == '__main__':
    filas = []
    for nombre, o, g, rec, esc in pares:
        r = comparar(nombre, o, g, rec, esc)
        filas.append(f'{nombre:45s} similitud {r[0]:6.1%}   tinta exacta {r[1]:6.1%}   tinta ±1px {r[2]:6.1%}')
        print(filas[-1], flush=True)
    with open(os.path.join(OUT, 'resumen.txt'), 'w') as f:
        f.write('\n'.join(filas) + '\n')
