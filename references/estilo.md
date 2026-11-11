# Estilo de la casa y errores frecuentes de maquetación

El estilo existe para que la información esté en la **forma** (trazo, punta, contorno, grosor) y
no en el adorno. Todo lo que sigue sale del corpus de 37 diagramas y está implementado en
`assets/diagrama.sty`.

**Contenido:** [Reglas](#reglas) · [Escala y coordenadas](#escala-y-coordenadas) ·
[Etiquetas](#etiquetas) · [Lo interpretativo](#lo-interpretativo) · [Leyenda](#leyenda) ·
[Errores de maquetación](#errores-frecuentes-de-maquetación) ·
[Errores de compilación](#errores-de-compilación-que-ya-pasaron)

## Reglas

- **TikZ standalone**, `\documentclass[tikz,border=12pt]{standalone}` y `\usepackage{diagrama}`
  (EB Garamond `[lining]`, `fontenc T1`). TeX Gyre Heros (`\sffamily`) solo para diagramas de
  corte técnico o analítico (28, 29, 36, 37: lógica, ciencia cognitiva, teorías formales).
- **Dos variantes de trazo:** `\usepackage[robusto]{diagrama}` (por omisión, 1.1 pt, puntas
  grandes, más legible al reducir) y `[fino]` (0.9 pt; para diagramas densos con mucho texto,
  como 01 y 07).
- **Opción `negro`:** si el usuario pide «blanco y negro» estricto, `\usepackage[negro]{diagrama}` pone el texto y los trazos en negro puro (`tinta` y `gris`); lo interpretativo conserva su gris claro, que es lo que lo distingue.
- **Solo escala de grises, sin color.** `tinta` (casi negro) para texto y contorno de lo
  actual; `gris` para contornos virtuales y trazos secundarios; `grisclaro` para lo
  interpretativo. Un diagrama de este estilo se imprime en blanco y negro sin perder nada.
- **Títulos** en negrita (`titulo=46`); **términos técnicos y relaciones** en cursiva
  (`\textit`, `termino`, `rotulo`); **niveles** en versalitas o negrita al margen (`nivel`). Un
  subtítulo en cursiva puede situar la obra: «*The Subsumption of Ethics in Politics in
  Dussel's Politics of Liberation*» (`subtitulo=32`).
- **Estilos con nombre semántico, no gráfico:** `genesis`, `sucesion`, `unilateral`… en lugar
  de `dashed, -latex`. El código se lee como el libro de fidelidad. Los nombres están en
  `references/lexico.md`.
- **Una sola figura, un camino principal.** El grosor jerarquiza: la relación principal va
  gruesa (`line width=2pt`) y las secundarias, finas. El ojo debe poder recorrer el diagrama
  de un vistazo.

## Escala y coordenadas

- 1 unidad = 1,6 cm (equivalente a 100 px de la imagen original). Las coordenadas se leen
  directamente: un diagrama de 12 × 8 unidades cabe en una hoja apaisada.
- **Sin `[img]`, y crece hacia arriba** (como en matemáticas). Con `\begin{tikzpicture}[img]`, y
  crece hacia abajo y las coordenadas son (x/100, y/100) de una imagen de partida: útil cuando
  se redibuja desde una figura.
- **Tamaños de letra relativos: `\px{n}`**, donde n son los píxeles de la imagen original.
  `\px{30}` es el cuerpo normal de un nodo, `\px{20}` el de un rótulo de arista, `\px{46}` un
  título. Usarlo (en vez de `\large`, `\small`) permite escalar el diagrama sin desarmar las
  proporciones.
- Para que todos los nodos de un diagrama compartan cuerpo:
  `\begin{tikzpicture}[every node/.append style={font=\px{30}}]`.
- Las medidas `minimum width=…cm` **están en centímetros**, no en unidades: 3 unidades son
  4,8 cm. Es el error de escala más frecuente (ver más abajo).

## Etiquetas

- **Rótulos de arista con fondo blanco y `inner sep` pequeño:** estilo `rotulo` (`etq` +
  cursiva). Nada de texto cruzado por líneas.
- **Las etiquetas citan, no explican.** El rótulo es la palabra del autor (*Coupling*,
  *Succession*, *Reciprocal Determination*). La explicación va en el párrafo de entrega, no
  dentro del dibujo. «Pasa de lo virtual a lo actual por una fuerza» **no** es un rótulo; *Force*
  sí.
- **Un nodo es «término + (alias o función)»:** «Id (*Habitus*)», «Ego Ideal
  (*Eros-Mnemosyne*)». Las fórmulas propias del concepto van en cursiva citada.
- **El término original, nunca la paráfrasis.** Si el texto escribe *Mnemosyne*, el diagrama
  dice *Mnemosyne*, no «memoria pura».
- **Nodos como texto suelto.** En el corpus la mayoría de los nodos no tienen caja; las cajas
  aparecen solo cuando la forma significa algo (facultades en 08, principios en 01, modelos en
  29).

## Lo interpretativo

Lo que sea **lectura del diagramador** y no del texto se ve:

- La arista o el nodo va en gris claro: `\draw[unilateral, interp] …` o `\node[interp] …`.
- Lleva la marca † (`\interpretativo`, que da `\textsuperscript{\textdagger}`) pegada al rótulo.
- La nota al pie del diagrama la explica: `\nota{x,y}{† Lectura del diagramador: …}`.
- Lo `inferido` y discutible lleva `\discutible` (*) con su nota.

## Leyenda

Si el diagrama usa **más de tres tipos de trazo** y las aristas no llevan su nombre, añade una
leyenda mínima con `\muestra{estilo}{x}{y}{significado}`, una por trazo. Los diagramas del
corpus casi nunca la necesitan porque cada arista lleva su nombre; si la necesitas, es
posible que te falten rótulos.

## Errores frecuentes de maquetación

| Síntoma | Causa y arreglo |
|---|---|
| Una línea atraviesa un texto | Pon el texto en un nodo con `etq`/`rotulo` (fondo blanco) sobre la línea, o desplaza el texto. `scripts/revisar.py` lo detecta. |
| La punta de la flecha toca el texto | Dibuja de nodo a nodo (`(n1) -- (n2)`, no entre coordenadas): TikZ recorta en el borde. Si el nodo es texto suelto, añade `inner sep=4pt`. |
| Los rótulos de dos aristas se pisan | Sepáralos con `pos=0.3` / `pos=0.7`, o con `above`/`below`; nunca los dejes en el centro de ambas. |
| El haz de arcos tapa rótulos | Escalona el control de cada arco (ver 28 en `ejemplos/`) y pon los rótulos al borde. |
| Todo el dibujo parece apretado a la izquierda | Los nodos de texto largo se ensanchan hacia ambos lados desde el centro; deja ≥ 0.8 unidades entre columnas. |
| Las dos mitades de un panel no coinciden | Dibuja la estructura una vez como macro (`\newcommand\panel[…]{…}`) y aplícala dos veces con `shift={(dx,0)}`. |
| Una llave queda al revés | La punta de `llave` queda a la **izquierda del sentido del trazo, tal como lo ves en la página**: para una punta hacia arriba, traza de izquierda a derecha; punta hacia abajo, de derecha a izquierda; punta hacia la derecha, **de arriba abajo**; punta hacia la izquierda, de abajo arriba. Sale al revés de lo que se espera, así que compila una de prueba y mira. |
| La leyenda es más grande que el dibujo | Es señal de que sobran estilos; revisa si de verdad hay más de tres tipos de relación. |
| El diagrama «se ve bonito» pero no dice nada | Es una lista con flechas: todas las aristas son iguales. Vuelve a Fase A; falta separar las relaciones. |
| La figura sugiere una tesis que el autor no sostiene | Es una geometría decorativa. Quita la figura o vuelve a un arquetipo plano. |

## Errores de compilación que ya pasaron

- `Undefined control sequence … \usepackage` con una `S` o similar: viene de editar con `sed`
  en Windows, donde `\u` se interpreta como «mayúscula» en la sustitución. Escribe los archivos
  `.tex` con la herramienta de edición o con Python en cadenas crudas (`r"\usepackage"`).
- `xshift=#1 cm` en una macro desplaza **centímetros**, no unidades. Usa
  `shift={(#1,0)}` para moverte en la grilla.
- `minimum width=7cm` con coordenadas en unidades: 7 cm son 4.4 unidades. Convierte (÷ 1.6) al
  escribir las coordenadas de lo que va dentro.
- Un `\foreach` con valores que contienen comas o barras necesita llaves:
  `\foreach \a/\b in {1/{Término, A}, 2/{Término B}}`.
- Las llaves de `\foreach` anidados no deben llevar `%` al final de línea si hay texto
  después; el `%` se come el salto.
- Un apóstrofo en `Término 1'` dentro de un `\foreach` va bien; una comilla recta `"` no. Para
  comillas del autor usa `\textit{"…"}` o ``…''.
- Con `[img]`, `\draw[…] (n1) -- ++(0,0.6)` sube **hacia abajo** (y está invertida).
- Un salto de línea con espacio negativo seguido de un grupo, `\\[-3pt]{…}` o `\\[1pt]{\px{15}…}` dentro de un nodo con `align=center`, rompe con `Undefined control sequence … \tikzscope@linewidth`. Pon cada `\\` en el nivel superior del texto del nodo, sin llaves de por medio, o parte el texto en dos nodos.
- **Heredocs y `printf` en Bash colapsan `\\` y se atragantan con apóstrofos**, igual que `sed`. Para escribir `.tex` o `.md` con TikZ usa siempre la herramienta de escritura, o un script de Python guardado en un archivo.
- Para anclar una arista a una abscisa fija dentro de un nodo ancho: `(x,0 |- n.south)` toma la x de `x` y la y del borde sur del nodo.
- **Griego, ruso y otros alfabetos:** `diagrama.sty` no carga LGR ni cirílico. Translitera en cursiva, sin macrones, y da la glosa en la lengua del usuario: *noesis*, *dianoia*, *anypotheton arche*.
