---
name: diagramas-conceptuales
description: Lee un texto filosófico o teórico, extrae su estructura conceptual y la dibuja como diagrama TikZ de calidad editorial, en blanco y negro, fiel al texto y distinguiendo qué tipo de relación une cada par de ideas (derivación, génesis, reciprocidad, unilateralidad, retorno, totalización). Úsala siempre que se pida «el diagrama de este texto», «grafica las relaciones entre los conceptos de…», un mapa conceptual o esquema de una obra o capítulo (Kant, Deleuze, Laruelle, Bergson, Aristóteles, Platón, Carnap, Sneed…), «pásalo a TikZ», «visualiza el argumento», o cuando se comparta un PDF, imagen o fragmento filosófico con un pedido de figura, aunque no diga «diagrama» ni «TikZ». Reconstruye la arquitectura con un libro de fidelidad (cada nodo y arista con su pasaje) y un léxico donde la forma del trazo lleva el significado. No es para gráficos de datos, animaciones o videos (html-concept-animations, manim-concept-videos, claude-motion) ni para diagramas de software o de flujo.
---

# Diagramas conceptuales

Esta skill no resume ni ilustra el texto. **Reconstruye su arquitectura conceptual y la hace
visible**: qué entidades hay, qué relaciones afirma el autor entre ellas, cuáles agrupa bajo un
nombre y qué orientaciones globales atraviesan el conjunto. El resultado es un diagrama TikZ en
escala de grises donde *la forma del trazo lleva el significado*: una sola punta no es una
doble punta, un trazo rayado no es uno punteado, y esa diferencia está en el texto.

El criterio que manda es la **fidelidad**: el diagrama dice lo que dice el texto, ni más ni
menos. Un diagrama bonito que simetriza lo que el autor deja asimétrico es peor que ningún
diagrama, porque se lee como autoridad.

## Dónde está todo

La skill vive en `~/.claude/skills/diagramas-conceptuales/`. Todo lo que sigue es relativo a esa
carpeta.

| Qué | Dónde |
|---|---|
| Léxico de relaciones (qué trazo para qué relación) | `references/lexico.md`, y la hoja visual `assets/lexico-muestras.tex` |
| Catálogo de arquetipos (la figura) | `references/arquetipos.md` |
| Libro de fidelidad, plantilla y ejemplos | `references/fidelidad.md`, `assets/fidelidad-plantilla.md` |
| Estilo de la casa y errores de maquetación | `references/estilo.md` |
| Estilo unificado TikZ | `assets/diagrama.sty` |
| Plantilla compilable por arquetipo | `assets/plantillas/*.tex` (`base.tex` es el esqueleto) |
| 37 diagramas resueltos, por arquetipo | `assets/ejemplos/<arquetipo>-NN-nombre.tex` |
| Compilar y mirar | `scripts/compilar.py` |
| Revisar cotejo y solapes | `scripts/revisar.py` |

Lee `references/lexico.md` antes de dibujar la primera arista: el léxico es el corazón de la
skill. Lee `references/arquetipos.md` al elegir la figura. Los otros dos, cuando los necesites
(fidelidad al escribir el libro; estilo cuando algo se vea mal).

## Flujo

Las cinco fases son obligatorias y van en este orden. La razón de fondo es que la parte difícil
no es dibujar sino **decidir qué hay que dibujar**: si el libro de fidelidad está bien, el
dibujo es casi mecánico; si está mal, ningún pulido lo arregla.

### Fase A — Lectura estructural

1. **Lee el texto completo antes de dibujar nada.** Si es largo, localiza primero la tesis o las
   tesis que el diagrama debe mostrar, y **pregunta** al usuario si quiere el diagrama de todo
   el texto o de un pasaje (un capítulo entero suele ser tres o cuatro diagramas, no uno).
2. **Identifica los términos técnicos del autor en su forma original**: *Habitus*,
   *Mnemosyne*, *spatium*, *sentiendum*, *Aion*, dy/dx. En el diagrama aparece el vocabulario
   del autor, nunca una paráfrasis. Si hay traducción, el término original va en cursiva y
   entre paréntesis: «Superego (*Thanatos*)».
3. **Separa el texto en cuatro capas:**
   - **Entidades o instancias:** conceptos, facultades, niveles, momentos (ids `n`).
   - **Relaciones** que el texto afirma entre ellas (ids `e`).
   - **Agrupaciones o totalidades:** «las síntesis de reconocimiento», «la forma pura y vacía
     del tiempo» (ids `g`).
   - **Ejes u orientaciones globales:** contracción/dilatación, vida→muerte, monotonicidad
     (ids `x`).

### Fase B — Libro de fidelidad (antes del dibujo)

Escribe `fidelidad.md` con una fila por cada nodo y cada arista. Usa
`assets/fidelidad-plantilla.md`; el formato y tres ejemplos resueltos están en
`references/fidelidad.md`.

| id | elemento | tipo de relación | dirección | pasaje que lo respalda | estatus |
|---|---|---|---|---|---|

- **tipo de relación:** una entrada del léxico (`references/lexico.md`).
- **pasaje:** cita breve y página o sección.
- **estatus:** `textual` (el autor lo dice), `inferido` (se sigue directamente; explica cómo) o
  `interpretativo` (lectura tuya; se marcará en el dibujo).

**Si no hay pasaje que respalde una arista, esa arista no se dibuja.** Si el usuario no da el
texto sino que pide «el diagrama de X en Y», trabaja con los pasajes que provea o que puedas
citar con seguridad, y declara el estatus de todo lo demás (casi todo será `interpretativo`).
No completes con memoria de «lo que el autor suele decir»: es justo lo que el libro existe para
evitar.

### Fase C — Elegir el arquetipo

Elige la figura (`references/arquetipos.md`) **por la lógica del texto, no por costumbre**: una
génesis pide cascada; una división por género y especie, árbol; una correlación entre dos
órdenes, columnas en paralelo; un pasado que se contrae en un presente, un cono; una totalidad
dividida por un corte, semidiscos con cesura. **Justifica la elección en una línea** y anótala
en el libro. Se pueden combinar arquetipos (el 08 es cascada + columnas + bucles), pero cada
parte tiene que ser legible por sí sola.

### Fase D — Dibujar

1. Parte de la plantilla (`assets/plantillas/<arquetipo>.tex`) y de un ejemplo parecido de
   `assets/ejemplos/`. Cópialos a la carpeta de trabajo y renómbralos `NN-nombre.tex`.
2. Escribe en TikZ con `\usepackage{diagrama}`. **Estilos con nombre semántico**: cada arista
   se dibuja con el estilo de su relación (`genesis`, `sucesion`, `unilateral`, `reciproca
   debil`…), no con un aspecto genérico.
3. **Nombra los nodos con su id del libro** (`\node (n3) …`) y marca cada arista con su id al
   final de la sentencia (`% e4`), para que código y tabla se puedan cotejar.
4. Coordenadas en la grilla fija (1 unidad = 1,6 cm), tamaños con `\px{n}`.
5. Lo `interpretativo` va en gris claro (`interp`) con † y nota al pie (`\nota`); lo `inferido`
   discutible lleva * (`\discutible`).

### Fase E — Verificar

Compila y **mira la imagen**: un diagrama que compila puede tener etiquetas encima de las
líneas.

```bash
python ~/.claude/skills/diagramas-conceptuales/scripts/compilar.py 38-nombre.tex
python ~/.claude/skills/diagramas-conceptuales/scripts/revisar.py 38-nombre.tex
```

`compilar.py` genera PDF + PNG junto al `.tex` y, si falla, muestra el primer error con su
línea. `revisar.py` coteja el dibujo con `fidelidad.md` (puntos 1 y 3 de abajo), detecta rótulos
solapados (punto 2) y deja `<nombre>-revision.png` con lo sospechoso en rojo. Después lee el
PNG tú mismo. Revisa estos cinco puntos:

1. **Cada arista del dibujo está en la tabla y viceversa.**
2. **Ninguna etiqueta tapa una línea ni otra etiqueta.**
3. **Las asimetrías del texto siguen siendo asimetrías** (§ reglas duras).
4. **Los números del texto coinciden con los del dibujo** (tres síntesis, cuatro estratos, dos
   articulaciones): cuéntalos en el PNG, no los supongas.
5. **Se lee de un vistazo**: hay un camino principal claro y las relaciones secundarias tienen
   trazo más leve.

Corrige y repite hasta pasar los cinco. Si tras tres vueltas algo no cuadra, suele ser un
problema de la Fase B o C (la tabla o el arquetipo), no de maquetación.

## Léxico en una tabla

El léxico completo, con corpus y fragmentos, está en `references/lexico.md`. Para orientarte:

| Relación | Estilo | Trazo |
|---|---|---|
| Derivación, división género→especie | `derivacion` | sólida, punta llena |
| Sucesión, transición | `sucesion` | sólida o rayada, punta **hueca** |
| Génesis, actualización, fuerza | `genesis` | rayada, punta llena |
| Virtual: repetición, disfraz, desplazamiento | `virtual` | punteada fina, punta hueca |
| Operación singular del autor (clonación, extracción…) | `operacion` | raya-punto + rótulo |
| Reciprocidad, correlación, paralelismo | `reciproca` / `reciproca rayada` / `reciproca debil` | **doble** punta; la fuerza baja con el trazo |
| Unilateralidad: determina sin ser determinado | `unilateral` | **una sola** punta, nunca doble |
| Inclusión, subsunción | `subsuncion` + verbo | flecha con etiqueta verbal, o encastre |
| Autorreferencia, paradoja | `paradoja` | arco que salta de nivel |
| Retroalimentación | `retroalim` | haz de arcos punteados |
| Retorno, rechazo, metamorfosis entre series | `retorno` | arco punteado de doble punta |
| Anulación, exclusión | `anulacion` + «Cancelled» | punteada, o `\tachar` |
| Totalización | `totalidad` / `totalidad virtual` / `totalidad abierta` | llave sólida / rayada / punteada |
| Eje u orientación global | `eje` | flecha larga al margen, raya-punto, rotulada |
| Serie abierta | `\dots` | «…» |

Reglas complementarias del corpus: **el estatus ontológico se codifica en el contorno** (sólido
= actual, rayado = virtual, punteado = incognoscible: `caja`, `caja virtual`, `caja abierta`);
**el grosor jerarquiza** (camino principal grueso, secundario fino); **si el texto nombra la
relación, la arista lleva su nombre** en cursiva pequeña sobre fondo blanco (`rotulo`); un nodo
es «término + (alias o función)»; los niveles se nombran al margen (`nivel`).

El léxico puede ampliarse si un texto lo exige, pero cada trazo nuevo se define con nombre
semántico en el propio `.tex`, se explica en la leyenda del diagrama y se añade a
`references/lexico.md`.

## Cuando no hay texto delante

Es lo normal: el usuario nombra una obra y pide el diagrama. Los agentes que probaron esta skill tropezaron aquí más que en ningún otro sitio, así que:

- **Búscalo si puedes** (texto de dominio público, un PDF que el usuario tenga en alguna carpeta); un pasaje real vale más que cualquier memoria.
- **Los diagramas de `assets/ejemplos/` no son el texto.** Son interpretaciones de un tercero y a veces discrepan entre sí. Úsalos para el vocabulario y el arquetipo, no como pasaje citado.
- **Todo lo que no puedas citar baja de estatus**: términos inconfundibles «de memoria, sin cotejar»; lo demás `inferido` o `interpretativo`. Detalles en `references/fidelidad.md`.
- Dilo en la entrega, y ofrece volver a compilar cuando el usuario pase el pasaje.

## Reglas duras de fidelidad

Hay una razón detrás de cada una; si la entiendes, sabrás aplicarla en casos que no están aquí.

- **No simetrizar.** Si el texto dice que A determina a B y no al revés, la flecha va en un solo
  sentido. Una doble punta afirma dependencia mutua; ponerla «porque queda más equilibrado» es
  inventar una tesis. Las relaciones unilaterales de Laruelle y la determinación en última
  instancia son los casos de prueba.
- **No completar ni redondear.** Si el autor da tres síntesis, van tres; no se agrega una cuarta
  por equilibrio visual. Si deja una serie abierta, va «…».
- **No unificar vocabularios.** Dos autores que usan la misma palabra con sentidos distintos
  llevan nodos distintos, y una nota los distingue.
- **Un elemento sin contraparte queda sin arista.** Si un componente de una teoría no tiene equivalente en la otra (las reglas de correspondencia de Carnap en Sneed), no se le inventa una flecha: queda suelto, y si dibujas una por interpretación, va gris con †.
- **La disposición no reordena una tupla.** Si la maqueta obliga a reordenar los componentes de una fórmula (⟨Mp, M, C, Mpp⟩), la cabecera conserva el orden del autor y una nota al pie declara el reordenamiento.
- **Una dependencia en un solo sentido** (el texto da A→B y la inversa solo está implícita) se dibuja con una flecha de una punta marcada *, y el libro anota que la inversa no se dibuja.
- **Mostrar las tensiones.** Paradojas, cancelaciones, rechazos, lo que el texto excluye y lo que
  señala como incognoscible (el «?», la cosa en sí) se dibujan; no se omiten porque estorben.
- **Lo interpretativo se ve.** Gris claro + † + nota al pie. Lo inferido discutible lleva *.
- **Las etiquetas citan, no explican.** El rótulo es la palabra del autor; la explicación va en
  el párrafo de entrega.
- **Leyenda** si el diagrama usa más de tres tipos de trazo (los del corpus casi nunca la
  necesitan, porque cada arista lleva su nombre).

## Cuándo preguntar al usuario

Pregunta, antes de dibujar, solo lo que cambia el diagrama:

- **Alcance:** ¿todo el texto o un pasaje? Un capítulo largo suele ser varios diagramas.
- **El texto mismo**, si no lo diste: «¿me lo pasas, o trabajo con lo que puedo citar y marco el
  resto como interpretativo?».
- **Qué tesis mostrar**, si el texto defiende varias y cabe solo una en la figura.
- **Idioma de las etiquetas.** Regla por omisión, para no preguntar: los **términos técnicos van en la lengua del texto que el usuario nombra** (alemán para Kant, griego translitero para Platón, francés para Deleuze o Laruelle, o la lengua de la traducción si trabaja sobre una), y el resto de rótulos y notas en la lengua en que el usuario escribe. Declara la elección en la entrega; si el diagrama va a una publicación en otra lengua, pregunta.

No preguntes por estilo, arquetipo o trazos: eso lo decides tú con el léxico y lo justificas.

## Entrega

Carpeta de trabajo con `NN-nombre.tex` + PDF + PNG + `fidelidad.md`, y **un párrafo** que diga:

1. qué muestra el diagrama (la tesis);
2. **por qué ese arquetipo** (una línea);
3. qué decisiones interpretativas se tomaron (las filas †);
4. **qué del texto quedó fuera y por qué.**

Si el trabajo va dentro de `~/.claude/diagramas-tikz/`, continúa la numeración (el siguiente
número libre; el último es el 37) y añade el nuevo diagrama a `todos.tex` solo si el usuario lo
pide.

## Anti-patrones

- **Una lista con flechas.** Si todas las aristas son iguales, falta análisis.
- **Flechas genéricas «→»** para relaciones de distinto tipo.
- **Cajas para todo.** La caja solo aparece cuando la forma significa algo.
- **Parafrasear términos técnicos** («memoria pura» en lugar de *Mnemosyne*).
- **Comentario del diagramador dentro del dibujo.** Va en el párrafo de entrega o, si es una
  decisión interpretativa, en una nota † al pie.
- **Rellenar el espacio con simetrías que el texto no tiene.** Un diagrama con huecos es un
  diagrama honesto.
- **Dibujar desde la memoria de «la doctrina»** en lugar del pasaje: es la causa de casi todas
  las infidelidades.
