# diagramas-conceptuales

Skill de Claude Code que lee un texto filosófico o teórico, reconstruye su estructura conceptual y la dibuja como diagrama TikZ en blanco y negro, fiel al texto. La forma del trazo lleva el significado: una relación unilateral no se dibuja como una recíproca.

## Contenido

- `SKILL.md`: flujo de trabajo (A–E).
- `references/`: léxico de trazos, arquetipos, libro de fidelidad y estilo.
- `assets/`: `diagrama.sty` (opciones `fino` y `robusto`), 37 ejemplos por arquetipo, 12 plantillas compilables.
- `scripts/`: `compilar.py` y `revisar.py` (detecta trazos que cruzan texto; usa Ghostscript).
- `evals/`: 5 casos de prueba (Deleuze, Kant, Laruelle, Platón, Sneed).

## Instalación

Copiar la carpeta a `~/.claude/skills/diagramas-conceptuales/`. Requiere una distribución LaTeX con TikZ y, para `revisar.py`, Ghostscript.
