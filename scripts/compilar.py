#!/usr/bin/env python3
"""Compila un diagrama TikZ standalone y saca una vista PNG.

Uso:
    python compilar.py diagrama.tex                 # PDF + PNG junto al .tex
    python compilar.py a.tex b.tex --dpi 110        # varios, con otra resolución
    python compilar.py diagrama.tex --salida build  # deja todo en ./build

Hace tres cosas que `pdflatex` solo no hace:
  1. Encuentra `diagrama.sty` aunque no esté junto al .tex (busca en ../assets de la skill).
  2. Si falla, muestra el primer error con el número de línea y la línea del .tex que lo causó,
     en vez de volcar el log entero.
  3. Rasteriza el PDF con pdftoppm para poder MIRAR el resultado (la verificación visual no es
     opcional: un diagrama que compila puede tener etiquetas encima de las líneas).

Sale con código 0 si todos compilaron, 1 si alguno falló.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def es_miktex() -> bool:
    try:
        out = subprocess.run(["pdflatex", "--version"], capture_output=True, text=True).stdout
    except FileNotFoundError:
        return False
    return "MiKTeX" in out


def primer_error(log: Path, tex: Path) -> str:
    """Devuelve el primer error del log con su contexto en el .tex."""
    try:
        lineas = log.read_text(encoding="utf-8", errors="replace").splitlines()
    except FileNotFoundError:
        return "(no se generó el log: ¿está instalado pdflatex?)"
    for i, linea in enumerate(lineas):
        if linea.startswith("!"):
            mensaje = linea[1:].strip()
            contexto = []
            num = None
            for sig in lineas[i + 1 : i + 12]:
                m = re.match(r"l\.(\d+)\s*(.*)", sig)
                if m:
                    num = int(m.group(1))
                    contexto.append(sig)
                    break
                contexto.append(sig)
            partes = [f"  ! {mensaje}"]
            if num is not None:
                fuente = tex.read_text(encoding="utf-8", errors="replace").splitlines()
                if 0 < num <= len(fuente):
                    partes.append(f"  {tex.name}:{num}:  {fuente[num - 1].strip()}")
            else:
                partes.extend("  " + c for c in contexto[:3])
            return "\n".join(partes)
    return "  (pdflatex falló sin un '!' en el log; revisa " + log.name + ")"


def compilar(tex: Path, salida: Path, dpi: int) -> bool:
    salida.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
           f"-output-directory={salida}"]
    if not (tex.parent / "diagrama.sty").exists():
        if es_miktex():
            cmd.append(f"-include-directory={ASSETS}")
        else:
            env["TEXINPUTS"] = str(ASSETS) + os.pathsep + env.get("TEXINPUTS", "")
    cmd.append(tex.name)
    r = subprocess.run(cmd, cwd=tex.parent, env=env, capture_output=True, text=True)
    base = tex.stem
    log = salida / f"{base}.log"
    pdf = salida / f"{base}.pdf"
    if r.returncode != 0 or not pdf.exists():
        print(f"ERROR  {tex.name}")
        print(primer_error(log, tex))
        return False
    if shutil.which("pdftoppm"):
        subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-singlefile",
                        str(pdf), str(salida / base)], check=False)
        vista = salida / f"{base}.png"
        print(f"ok     {tex.name}  ->  {pdf}  +  {vista}")
    else:
        print(f"ok     {tex.name}  ->  {pdf}   (sin pdftoppm: no hay PNG)")
    # lo que no hace falta entregar: el .log solo sirve si algo falla
    for ext in (".aux", ".log"):
        (salida / f"{base}{ext}").unlink(missing_ok=True)
    return True


def main() -> int:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivos", nargs="+", type=Path)
    ap.add_argument("--dpi", type=int, default=110, help="resolución del PNG (110 por omisión)")
    ap.add_argument("--salida", type=Path, default=None,
                    help="carpeta de salida (por omisión, la del .tex)")
    a = ap.parse_args()
    ok = True
    for f in a.archivos:
        f = f.resolve()
        if not f.exists():
            print(f"ERROR  {f}: no existe")
            ok = False
            continue
        ok &= compilar(f, (a.salida or f.parent).resolve(), a.dpi)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
