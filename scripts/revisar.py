#!/usr/bin/env python3
"""Revisa un diagrama: cotejo con el libro de fidelidad + rótulos solapados.

Uso:
    python revisar.py diagrama.tex                         # busca fidelidad.md junto al .tex
    python revisar.py diagrama.tex --fidelidad otra.md
    python revisar.py diagrama.tex --solo-solapes          # sin libro de fidelidad
    python revisar.py diagrama.tex --dpi 200

Necesita que el PDF ya exista (python compilar.py diagrama.tex). Hace dos revisiones:

A. COTEJO CON EL LIBRO DE FIDELIDAD  (puntos 1 y 3 de la Fase E)
   Convención de ids, que el dibujo debe seguir para poder cotejarse:
     n1, n2…  nodos      → \\node (n3) at … {…};        (o un comentario  % n3)
     e1, e2…  aristas    → \\draw[genesis] (n1) -- (n2);  % e4   (comentario al final)
     g1, g2…  totalidades (llaves, agrupaciones)           % g1
     x1, x2…  ejes u orientaciones globales                % x1
     m1, m2…  marcas y notas que no son nodos (*, †, alias)  % m1
   Comprueba: ids en el dibujo que no están en la tabla (y al revés); estatus válido
   (textual | inferido | interpretativo); aristas sin pasaje; que lo `interpretativo`
   se dibuje en gris claro (estilo `interp`) con su †; que una relación `unilateral`
   no tenga doble punta y que una `reciproca` sí la tenga.

B. SOLAPAMIENTOS  (punto 2 de la Fase E)
   Con las cajas de palabras del PDF (ghostscript txtwrite) y una versión del PDF sin texto
   (ghostscript -dFILTERTEXT) busca (i) palabras que se pisan entre sí y (ii) trazos que
   cruzan una palabra sin que una etiqueta con fondo blanco los tape. Deja
   `<diagrama>-revision.png` con las palabras sospechosas en rojo: MÍRALO.
   Son avisos, no sentencias: una barra de fracción bajo una letra o una llave junto a un
   rótulo pueden saltar sin ser un error.

Sale con 1 si hay errores de cotejo; los avisos de solape no cambian el código.
"""
import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ESTATUS = {"textual", "inferido", "interpretativo"}
ID_RE = r"[negxm]\d+[a-z]?"
DOBLE_PUNTA = re.compile(r"llenos|huecos|barbas|reciproca|<->|<-\s*>|Latex\[[^\]]*\]\}\s*-\s*\{|Triangle\[[^\]]*\]\}\s*-\s*\{")


# ------------------------------------------------------------------ A. libro de fidelidad
def estatus_de(celda: str) -> str:
    """La palabra de estatus, aunque la celda lleve marcas (* †) o una explicación tras ':'."""
    m = re.match(r"[\s`*†]*([A-Za-zñé]+)", celda)
    return m.group(1).lower() if m else ""


def leer_fidelidad(ruta: Path):
    filas = {}
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.strip().startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if not celdas or not re.fullmatch(ID_RE, celdas[0].strip("` *")):
            continue
        celdas += [""] * (6 - len(celdas))
        filas[celdas[0].strip("` *")] = {
            "elemento": celdas[1], "tipo": celdas[2].lower(), "direccion": celdas[3],
            "pasaje": celdas[4], "estatus": estatus_de(celdas[5]),
        }
    return filas


def sentencias(tex: str):
    """(texto, línea_inicio, línea_fin) de cada \\draw/\\node/\\path/\\fill hasta su ';'."""
    res = []
    for m in re.finditer(r"\\(?:draw|path|node|fill|filldraw|coordinate)\b.*?;", tex, re.S):
        a = tex.count("\n", 0, m.start()) + 1
        b = a + m.group(0).count("\n")
        res.append((m.group(0), a, b))
    return res


def ids_del_dibujo(tex: str):
    """Devuelve {id: [sentencias asociadas]} a partir de comentarios % id y nombres (id)."""
    lineas = tex.splitlines()
    sent = sentencias(tex)
    asociadas = {}

    def asociar(i, n_linea):
        # sentencia que contiene la línea, o la siguiente si el comentario va solo
        for s, a, b in sent:
            if a <= n_linea <= b:
                asociadas.setdefault(i, []).append(s)
                return
        for s, a, b in sent:
            if a > n_linea:
                asociadas.setdefault(i, []).append(s)
                return
        asociadas.setdefault(i, [])

    for n, linea in enumerate(lineas, 1):
        if "%" in linea:
            comentario = linea[linea.index("%"):]
            for i in re.findall(rf"\b({ID_RE})\b", comentario):
                asociar(i, n)
        for i in re.findall(rf"\\(?:node|coordinate)\s*(?:\[[^\]]*\]\s*)?\(({ID_RE})\)", linea):
            asociar(i, n)
    return asociadas


def cotejar(tex_ruta: Path, fid_ruta: Path):
    errores, avisos = [], []
    tex = tex_ruta.read_text(encoding="utf-8")
    filas = leer_fidelidad(fid_ruta)
    if not filas:
        return [f"{fid_ruta.name}: no encontré filas con ids (n1, e1, g1, x1…) en la tabla"], []
    dibujo = ids_del_dibujo(tex)

    for i in sorted(set(dibujo) - set(filas)):
        errores.append(f"'{i}' está en el dibujo pero no en {fid_ruta.name}")
    for i in sorted(set(filas) - set(dibujo)):
        errores.append(f"'{i}' ({filas[i]['elemento'][:40]}) está en {fid_ruta.name} pero no en el dibujo")

    hay_interp = False
    for i, f in filas.items():
        if f["estatus"] not in ESTATUS:
            errores.append(f"'{i}': estatus '{f['estatus']}' no válido (textual | inferido | interpretativo)")
        if f["estatus"] in ("textual", "inferido") and len(f["pasaje"]) < 8:
            errores.append(f"'{i}': estatus {f['estatus']} pero sin pasaje que lo respalde. "
                           "Si no hay pasaje, no se dibuja (o se marca interpretativo)")
        if f["estatus"] == "interpretativo":
            hay_interp = True
            codigo = " ".join(dibujo.get(i, []))
            if codigo and "interp" not in codigo:
                avisos.append(f"'{i}' es interpretativo pero su código no usa el estilo `interp` (gris claro)")
        codigo = " ".join(dibujo.get(i, []))
        if i.startswith("e") and codigo:
            if "unilateral" in f["tipo"] and DOBLE_PUNTA.search(codigo):
                errores.append(f"'{i}' es unilateral pero tiene doble punta: no simetrizar")
            if re.search(r"reciproc|correlaci|paralelism|interdepend", f["tipo"]) and not DOBLE_PUNTA.search(codigo):
                avisos.append(f"'{i}' es {f['tipo']} pero el código no muestra doble punta; ¿falta la segunda?")
    if hay_interp and not re.search(r"\\interpretativo|\\textdagger|†", tex):
        avisos.append("hay elementos interpretativos pero el dibujo no usa la marca † (\\interpretativo) ni nota al pie")
    if hay_interp and "\\nota" not in tex and "diagramador" not in tex:
        avisos.append("hay elementos interpretativos pero no veo una nota al pie que explique el † (usa \\nota{…})")
    return errores, avisos


# ------------------------------------------------------------------ B. solapamientos
def gs_exe():
    return shutil.which("gswin64c") or shutil.which("gs")


def palabras_pdf(pdf: Path):
    """Palabras de la página 1 con su caja en puntos (origen arriba-izquierda).

    Usa el dispositivo txtwrite de ghostscript (formato XML), que da la línea base y el
    cuerpo de cada palabra; es más grueso que pdftotext -bbox pero no depende de poppler.
    """
    gs = gs_exe()
    if not gs:
        return None, None, []
    r = subprocess.run([gs, "-q", "-dBATCH", "-dNOPAUSE", "-dFirstPage=1", "-dLastPage=1",
                        "-sDEVICE=txtwrite", "-dTextFormat=0", "-sOutputFile=-", str(pdf)],
                       capture_output=True)
    if r.returncode != 0:
        return None, None, []
    salida = r.stdout.decode("utf-8", errors="replace")
    pal = []
    for sp in re.finditer(r'<span bbox="(-?\d+) (-?\d+) (-?\d+) (-?\d+)"[^>]*size="([\d.]+)">(.*?)</span>', salida, re.S):
        x0, y0, x1, y1 = map(float, sp.groups()[:4])
        cuerpo = float(sp.group(5))
        texto = html.unescape("".join(re.findall(r'c="([^"]*)"', sp.group(6))))
        base = (y0 + y1) / 2
        pal.append([x0, base, x1, cuerpo, texto])
    # ghostscript parte las palabras en tramos (kerning, cambios de fuente): se vuelven a unir
    pal.sort(key=lambda p: (round(p[1]), p[0]))
    unidas = []
    for p in pal:
        if unidas:
            q = unidas[-1]
            if abs(q[1] - p[1]) <= 1 and p[0] - q[2] <= 0.12 * max(q[3], p[3]):
                q[2] = max(q[2], p[2])
                q[3] = max(q[3], p[3])
                q[4] += p[4]
                continue
        unidas.append(list(p))
    pal = [(x0, base - 0.72 * c, x1, base + 0.22 * c, t) for x0, base, x1, c, t in unidas]
    dim = subprocess.run([gs, "-q", "-dBATCH", "-dNOPAUSE", "-sDEVICE=bbox", "-dFirstPage=1", "-dLastPage=1", str(pdf)],
                         capture_output=True, text=True)
    m = re.search(r"%%HiResBoundingBox: ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)", dim.stderr)
    ancho = float(m.group(3)) if m else 0.0
    alto = float(m.group(4)) if m else 0.0
    return ancho, alto, pal


def raster_sin_texto(pdf: Path, dpi: int, destino: Path):
    gs = gs_exe()
    if not gs:
        return False
    r = subprocess.run([gs, "-q", "-dBATCH", "-dNOPAUSE", "-dFILTERTEXT", "-sDEVICE=pnggray",
                        f"-r{dpi}", "-dFirstPage=1", "-dLastPage=1",
                        f"-sOutputFile={destino}", str(pdf)], capture_output=True, text=True)
    return r.returncode == 0 and destino.exists()


def solapes(pdf: Path, dpi: int):
    import numpy as np
    from PIL import Image, ImageDraw

    avisos = []
    ancho, alto, pal = palabras_pdf(pdf)
    if ancho is None:
        return ["no encontré ghostscript (gs): salto la revisión de solapes; revisa a ojo el PNG"], None
    sx = dpi / 72.0
    pal = [p for p in pal if re.search(r"\w", p[4])]
    sospechosas = []

    # (i) palabras que se pisan. Las cajas de pdftotext son más altas que los glifos: se acortan.
    def caja(p):
        h = p[3] - p[1]
        return (p[0], p[1] + 0.12 * h, p[2], p[3] - 0.12 * h)

    for i in range(len(pal)):
        a = caja(pal[i])
        for j in range(i + 1, len(pal)):
            b = caja(pal[j])
            ix = min(a[2], b[2]) - max(a[0], b[0])
            iy = min(a[3], b[3]) - max(a[1], b[1])
            if ix > 0.8 and iy > 0.8:
                area = ix * iy
                menor = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1]))
                if menor > 0 and area / menor > 0.2:
                    avisos.append(f"se pisan «{pal[i][4]}» y «{pal[j][4]}» cerca de "
                                  f"({pal[i][0] / 28.35:.1f} cm, {pal[i][1] / 28.35:.1f} cm)")
                    sospechosas += [pal[i], pal[j]]

    # (ii) trazos que cruzan una palabra, sobre el PDF sin texto
    with tempfile.TemporaryDirectory() as td:
        sin_texto = Path(td) / "g.png"
        if raster_sin_texto(pdf, dpi, sin_texto):
            g = np.array(Image.open(sin_texto).convert("L"))
            for p in pal:
                x0, y0, x1, y1, t = p
                h = y1 - y0
                ya, yb = int((y0 + 0.22 * h) * sx), int((y1 - 0.22 * h) * sx)
                xa, xb = int(x0 * sx) + 1, int(x1 * sx) - 1
                if yb <= ya or xb <= xa:
                    continue
                tinta = int((g[ya:yb, xa:xb] < 200).sum())
                if tinta >= 6:
                    avisos.append(f"un trazo pasa por «{t}» cerca de ({x0 / 28.35:.1f} cm, {y0 / 28.35:.1f} cm): "
                                  "tápalo con un rótulo de fondo blanco (etq) o muévelo")
                    sospechosas.append(p)
        else:
            avisos.append("no encontré ghostscript (gs): salto la detección de trazos que cruzan palabras; "
                          "revisa a ojo el PNG")

    # imagen con las sospechosas en rojo
    anotada = None
    img_ruta = Path(str(pdf.with_suffix("")) + "-revision.png")
    gs = gs_exe()
    if gs:
        r = subprocess.run([gs, "-q", "-dBATCH", "-dNOPAUSE", "-dTextAlphaBits=4", "-dGraphicsAlphaBits=4",
                            "-sDEVICE=png16m", f"-r{dpi}", "-dFirstPage=1", "-dLastPage=1",
                            f"-sOutputFile={img_ruta}", str(pdf)], capture_output=True)
        if r.returncode == 0 and img_ruta.exists():
            im = Image.open(img_ruta).convert("RGB")
            d = ImageDraw.Draw(im)
            for x0, y0, x1, y1, _ in sospechosas:
                d.rectangle([x0 * sx - 2, y0 * sx - 2, x1 * sx + 2, y1 * sx + 2], outline=(220, 0, 0), width=3)
            im.save(img_ruta)
            anotada = img_ruta
    return avisos, anotada


# ------------------------------------------------------------------ main
def main() -> int:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tex", type=Path)
    ap.add_argument("--fidelidad", type=Path, default=None)
    ap.add_argument("--pdf", type=Path, default=None)
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--solo-solapes", action="store_true")
    a = ap.parse_args()

    tex = a.tex.resolve()
    pdf = (a.pdf or tex.with_suffix(".pdf")).resolve()
    codigo = 0

    if not a.solo_solapes:
        fid = (a.fidelidad or tex.parent / "fidelidad.md").resolve()
        print("== A. Cotejo con el libro de fidelidad ==")
        if not fid.exists():
            print(f"  (no existe {fid.name}: crea el libro ANTES de dibujar; ver references/fidelidad.md)")
            codigo = 1
        else:
            errores, avisos = cotejar(tex, fid)
            for e in errores:
                print("  ERROR ", e)
            for v in avisos:
                print("  aviso ", v)
            if not errores and not avisos:
                print("  ok: cada nodo y arista del dibujo está en la tabla y viceversa")
            codigo = 1 if errores else 0

    print("== B. Solapamientos ==")
    if not pdf.exists():
        print(f"  (no existe {pdf.name}: compila primero con compilar.py)")
        return 1
    avisos, anotada = solapes(pdf, a.dpi)
    for v in avisos:
        print("  aviso ", v)
    if not avisos:
        print("  ok: ninguna palabra se pisa y ningún trazo cruza el texto")
    if anotada:
        print(f"  imagen con lo sospechoso en rojo: {anotada}")

    print("\nA mano todavía (no se automatiza): ¿los números del texto coinciden con los del dibujo?"
          " ¿las asimetrías del texto siguen siendo asimetrías? ¿se lee de un vistazo?")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
