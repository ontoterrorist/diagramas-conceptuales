# El libro de fidelidad

Es la tabla `fidelidad.md` que se escribe **antes** de dibujar. Cada nodo y cada arista del
diagrama tiene una fila con el pasaje que lo respalda. Sirve para tres cosas:

1. **Obliga a leer el texto** y no a recordar la doctrina. Cuando no hay pasaje, se ve.
2. **Hace discutibles las decisiones**: quien revisa el diagrama puede ir a la fila y decir «esa
   flecha no está ahí» o «aquí falta la vuelta».
3. **Permite cotejar el código con la tabla** (`scripts/revisar.py`), porque cada fila tiene un
   id y el dibujo lleva los mismos ids.

**Contenido:** [Plantilla](#plantilla) · [Ids](#convención-de-ids) ·
[Estatus](#los-tres-estatus) · [Citar los pasajes](#citar-los-pasajes) ·
[Ejemplos resueltos](#ejemplos-resueltos) · [Si no hay texto](#si-el-usuario-no-da-el-texto)

## Plantilla

Hay una copia lista para llenar en `assets/fidelidad-plantilla.md`.

```markdown
# Libro de fidelidad: <título del diagrama>

Texto: <autor, obra, edición, capítulo o pasaje>. Alcance: <todo el texto | pasaje X–Y>.
Arquetipo: <árbol | cascada | …> — <una línea: por qué este y no otro>.

| id | elemento | tipo de relación | dirección | pasaje que lo respalda | estatus |
|---|---|---|---|---|---|
| n1 | *Habitus* (Id) | — | — | «…» (§ o p.) | textual |
| e1 | Pasado → Presente | sucesión | A→B | «…» (p.) | textual |
| g1 | «Forma pura y vacía del tiempo» | totalización (virtual) | n1,n2,n3 | «…» (p.); inferido porque el texto la aplica a las tres | inferido |
| x1 | contracción ↑ / dilatación ↓ | eje | — | «…» (p.) | textual |
```

Columnas:

- **id** — `n` nodo, `e` arista, `g` totalidad o agrupación, `x` eje u orientación global, `m` marca o nota que no es un nodo (un asterisco, un alias).
- **elemento** — el término del autor **en su forma original**, en cursiva si es técnico
  (*Habitus*, *Mnemosyne*, *spatium*). En una arista, «origen → destino».
- **tipo de relación** — una entrada del léxico (`references/lexico.md`): derivación,
  sucesión, génesis, virtual, operación, reciprocidad (fuerte/media/débil), unilateral,
  subsunción, paradoja, retroalimentación, retorno, anulación, totalización, eje.
- **dirección** — `A→B`, `A↔B` o `—`. Para una unilateral, **solo una**; si el texto da la
  vuelta, es otra fila.
- **pasaje que lo respalda** — cita breve entrecomillada y página o sección.
- **estatus** — **una sola palabra**: `textual`, `inferido` o `interpretativo` (siguiente sección). La explicación de un `inferido` va en la columna del pasaje, no aquí; `revisar.py` solo lee la primera palabra de la celda.

## Convención de ids

El dibujo lleva los mismos ids, para que código y tabla se puedan cotejar:

```latex
\node (n1) at (3.6,6.1) {Pasado};                            % nodo n1
\node (n2) at (9.0,6.1) {Presente};
\draw[sucesion larga] (n1) -- (n2);                           % e1  (marca al final de la sentencia)
\draw[totalidad virtual, llave=1.7cm] (9,3) -- (3.6,3);       % g1
\draw[eje] (1.5,2) -- (1.5,8);                                % x1
```

`revisar.py` encuentra los ids por los nombres de nodo (`(n1)`) y por comentarios `% e1`. Una
sentencia `\draw … ;` puede ocupar varias líneas; la marca va en cualquiera de ellas.

## Los tres estatus

| Estatus | Qué significa | En el dibujo |
|---|---|---|
| `textual` | el autor lo dice | trazo normal |
| `inferido` | se sigue directamente de lo que dice | trazo normal; si es discutible, marca `\discutible` (*) y nota al pie |
| `interpretativo` | es lectura del diagramador | **gris claro** (`interp`) y marca † (`\interpretativo`) con su nota al pie del diagrama |

Para `inferido`, la columna del pasaje dice **cómo** se infiere («A dice X en p. 5 y Y en p. 7;
de ahí que…»).

**Regla dura: si no hay pasaje que respalde una arista, esa arista no se dibuja.** El rincón
tentador es una arista «obvia» que completa la figura. Si de verdad crees que está implícita,
es `interpretativo`: va en gris claro con †, y el lector sabe que es tuya.

## Citar los pasajes

- **Cita breve** (una cláusula basta) con página o sección; no transcribas párrafos. El libro
  es un índice hacia el texto, no una copia.
- Cuando el texto traduce un término, cita el **original**: «*Habitus*», no «hábito» si el autor
  escribe *Habitus*.
- Si el usuario te dio un PDF o un fragmento, cita de **ese** texto. No completes con memoria
  de «lo que el autor suele decir»: eso es exactamente lo que el libro está para evitar.

## Ejemplos resueltos

En estos tres casos la «fuente» es la figura original del corpus (las imágenes en
`~/.claude/diagramas-tikz/originales/`), que es lo que se tuvo delante. Al dibujar desde un
texto, la columna del pasaje lleva la cita del texto y la página.

### Ejemplo A — árbol: la diferencia en el marco representacional de Aristóteles (`ejemplos/arbol-24-aristoteles.tex`)

Arquetipo: **árbol de división**, porque el texto divide la cualidad en especies por diferencias
sucesivas; no hay génesis ni correspondencia entre órdenes.

| id | elemento | tipo | dir. | pasaje (rótulo de la figura fuente) | estatus |
|---|---|---|---|---|---|
| n1 | *Quality* | — | — | nodo raíz izquierdo | textual |
| n2 | *Quantity* | — | — | nodo raíz derecho (con «…») | textual |
| n3 | *Animal* | — | — | hijo de *Quality* | textual |
| n4 | *Plant* | — | — | hijo de *Quality* (con «…») | textual |
| n5, n6 | *With Wings*, *With Feet* | — | — | hijos de *Animal* | textual |
| n7–n10 | *Bat*, *Dove*, *Man*, *Baboon* | — | — | hojas de las diferencias específicas | textual |
| n11–n18 | *Bat 1*, *Bat 2* … *Baboon 2* | — | — | «perceptual resemblances» | textual |
| e1, e2 | *Quality* → *Animal*, *Quality* → *Plant* | derivación | A→B | división de la cualidad | textual |
| e3, e4 | *Animal* → *With Wings* / *With Feet* | derivación | A→B | diferencia genérica | textual |
| e5–e8 | *With Wings* → *Bat*/*Dove*; *With Feet* → *Man*/*Baboon* | derivación | A→B | diferencia específica | textual |
| e9–e16 | cada especie → sus dos individuos | derivación | A→B | semejanzas perceptuales | textual |
| g1 | «…» junto a *Quality*/*Quantity* y bajo *Animal*, *Plant*, *Quantity*, *With Wings*, *With Feet* | serie abierta | — | la serie queda sin cerrar | textual |
| x1 | GENERIC / SPECIFIC DIFFERENCE / PERCEPTUAL RESEMBLANCES | niveles al margen | — | rótulos laterales | textual |

Lo que esta tabla **impide**: dibujar *Quantity* con sus propias especies (el texto solo lo
muestra con «…»), cerrar la rama de *Plant*, o poner una arista entre *Bat* y *Dove* (no hay
relación horizontal).

### Ejemplo B — unilateral: la distinción unilateral (`ejemplos/triangulo-14-philosophy-non-philosophy.tex`, panel inferior derecho)

Arquetipo: **triángulo de mediación y distinción unilateral**; el panel se hace *para* mostrar
la asimetría.

| id | elemento | tipo | dir. | pasaje (rótulo de la figura fuente) | estatus |
|---|---|---|---|---|---|
| n1 | Identity (*One*) | — | — | nodo izquierdo | textual |
| n2 | Duality (*Force-of-Thought*) | — | — | nodo derecho | textual |
| e1 | *One* → *Force-of-Thought* | **unilateral** | A→B | «Unilateral Cause (Determination-in-the-Last-Instance)» | textual |
| e2 | *Force-of-Thought* → *One* | **unilateral** | B→A | «Unilateral Distinction (Duality-Without-Synthesis)» | textual |

Las **dos** aristas son unilaterales, cada una con una sola punta y su nombre. No es una
reciprocidad: son dos relaciones distintas que van en sentidos distintos, y por eso una sola
flecha de doble punta *borraría* la tesis (que no hay síntesis). Es el caso de prueba de la
fidelidad.

```latex
\draw[unilateral, rounded corners=4pt] (n1.north) -- ++(0,0.6) -| (n2.north);   % e1
\draw[unilateral, rounded corners=4pt] (n2.south) -- ++(0,-0.6) -| (n1.south);  % e2
```

### Ejemplo C — serie con retornos: la síntesis del tiempo puro (`ejemplos/serie-21-sintesis-tiempo-puro.tex`)

Arquetipo: **serie temporal con cesura**, porque la tesis es la relación entre un antes, una
cesura y un después, y entre series.

| id | elemento | tipo | dir. | pasaje (rótulo de la figura fuente) | estatus |
|---|---|---|---|---|---|
| n1 | *Narcissistic Ego* (*Fractured Self*) | — | — | nodo superior | textual |
| n2–n4 | Pasado (*Id*, *Habitus*), Presente (*Ego Ideal*, *Eros-Mnemosyne*), Futuro (*Superego*, *Thanatos*) | — | — | serie ordinal | textual |
| e1–e3 | *Narcissistic Ego* → cada término | virtual | A→B | «First / Second / Third Repetition» | textual |
| e4, e5 | Pasado → Presente → Futuro | sucesión | A→B | «Succession» | textual |
| n5 | *The Unequal* (*Caesura*) | — | — | figura de cesura | textual |
| e6 | Pasado ↔ *Before* | retorno | A↔B | «Refusal» | textual |
| e7 | Presente ↔ cesura | retorno | A↔B | «Metamorphosis» | textual |
| e8 | Futuro ↔ *After* | retorno | A↔B | «Eternal Return» | textual |
| g1 | «Pure and Empty Form of Time» | totalización (punteada) | n2–n4 | llave inferior | textual |
| g2 | «Totality» | totalización | antes, cesura, después | rótulo a la derecha | textual |

El Futuro lleva contorno **raya-punto** (`caja futura`): no es actual. Y el *Eternal Return*
es una arista de **retorno** entre el Futuro y el *After*: no un cuarto término de la serie.

## Si el usuario no da el texto

Es el caso más frecuente y el que más tienta a inventar. Reglas:

- **La figura del corpus no es el texto.** Los diagramas de `assets/ejemplos/` son interpretaciones de un tercero: dos de ellos pueden discrepar entre sí (en el corpus, *Extraction* va One→X en unas figuras y One→Clone en otras) y alguno asigna cosas de otro modo que la lectura estándar (el 21 pone *Habitus* en el «pasado»). Úsalos como **fuente secundaria**, para el vocabulario y el arquetipo, y no los cites como «lo que dice el autor».
- **Lo que recuerdas con seguridad pero no puedes citar**: términos técnicos y tesis muy conocidas. Va como `textual` solo si es un término o una fórmula inconfundible; escribe en el pasaje «(de memoria, sin cotejar)». Lo demás es `inferido` con *, o `interpretativo`.
- **Un asterisco o una nota que no es un nodo** (el alias de un término, una advertencia) lleva su propia fila con id `m`.
- **Si el usuario nombra una obra pero no la entrega**, dilo en la entrega: «las citas son de memoria; cotéjalas antes de publicar».
- Si tienes acceso a la red y el texto es de dominio público, puedes **buscar el pasaje** (un agente descargó el alemán de la Akademie-Ausgabe para Kant); cita la edición y no inventes la paginación de otra.

Si pide «el diagrama de X en Y» sin darte el texto:

- Trabaja con los pasajes que el usuario provea, o con los que puedas **citar con seguridad**
  (obras muy conocidas, con sección que puedas dar).
- **Declara el estatus de todo lo demás**: lo que no puedas respaldar con un pasaje es
  `interpretativo` y se dibuja como tal. No lo presentes como «lo que dice Y».
- Dilo en el párrafo de entrega: «sin acceso al texto, las filas n3, e2 y e5 son lectura mía».
- Ofrece compilarlo de nuevo cuando el usuario pase el pasaje: es la salida honesta.
