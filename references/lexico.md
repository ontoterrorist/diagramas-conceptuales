# Léxico de relaciones

En los 37 diagramas del corpus **la forma del trazo lleva el significado**: el tipo de línea,
la punta, el grosor y la etiqueta. Eso es lo que permite que un lector vea de un vistazo que
A *determina* a B (una sola punta) y que C y D *se corresponden* (doble punta punteada).
Si todas las flechas son iguales, el diagrama es una lista con flechas y no dice nada que el
texto no dijera mejor.

Cada relación tiene un **estilo con nombre semántico** en `assets/diagrama.sty`. El código se
escribe con el nombre de la relación, no con su aspecto: `\draw[genesis] (n1) -- (n2);` se lee
como la fila del libro de fidelidad. La hoja `assets/lexico-muestras.tex` muestra todos los
trazos juntos; compílala y mírala cuando dudes entre dos.

**Contenido:** [Cómo elegir](#cómo-elegir-la-relación-a-partir-del-texto) ·
[1 Derivación](#1-derivación) · [2 Sucesión](#2-sucesión) · [3 Génesis](#3-génesis) ·
[4 Virtual](#4-virtual) · [5 Operación singular](#5-operación-singular-del-autor) ·
[6 Reciprocidad](#6-reciprocidad) · [7 Unilateralidad](#7-unilateralidad) ·
[8 Inclusión](#8-inclusión-y-subsunción) · [9 Paradoja](#9-autorreferencia-y-paradoja) ·
[10 Retroalimentación](#10-retroalimentación) · [11 Retorno](#11-retorno-rechazo-metamorfosis) ·
[12 Anulación](#12-anulación-y-exclusión) · [13 Totalización](#13-totalización) ·
[14 Ejes](#14-orientación-ejes-y-gradientes) · [15 Series abiertas](#15-serie-abierta) ·
[Reglas del contorno, grosor y etiqueta](#reglas-complementarias) ·
[Ampliar el léxico](#ampliar-el-léxico)

## Cómo elegir la relación a partir del texto

Lo que el autor escribe suele delatar la relación. Estas son las señales más fiables; ante la
duda, **vuelve al pasaje** y pregúntate qué hace A con B, no qué tan cerca están en la página.

| El texto dice… | Relación | Estilo |
|---|---|---|
| «se divide en», «se especifica en», «A es un género de B» | derivación | `derivacion` |
| «de A se sigue B», «A condiciona a B», «B se funda en A» | derivación (o génesis, si es un proceso) | `derivacion` / `genesis` |
| «después», «a continuación», «A, luego B», «el presente pasa a futuro» | sucesión | `sucesion` |
| «engendra», «produce», «se actualiza en», «fuerza que empuja», «efectúa» | génesis | `genesis` |
| «se encarna en», «se disfraza como», «se desplaza hacia», «repite» | virtual | `virtual` |
| una operación que el autor nombra (*clonación*, *extracción*, *reducción*, *contracción*) | operación singular | `operacion` |
| «se corresponde con», «es paralelo a», «están en relación recíproca» | reciprocidad | `reciproca*` |
| «determina sin ser determinado», «en última instancia», «sin síntesis» | unilateralidad | `unilateral` |
| «está subsumido en», «está contenido en», «es un caso de» | inclusión | `subsuncion` + verbo |
| «se aplica a sí mismo», «el conjunto que se contiene», «viola su propio nivel» | paradoja | `paradoja` |
| «la teoría superior reformula las inferiores» | retroalimentación | `retroalim` |
| «el eterno retorno», «rechazo», «metamorfosis» entre dos series | retorno | `retorno` |
| «queda cancelado», «se excluye», «no hay» | anulación | `anulacion` |
| «las tres juntas forman…», «la totalidad de…» | totalización | `totalidad*` |
| «hacia la contracción / la dilatación», «de la vida a la muerte», «gradiente» | eje | `eje` |
| «etc.», «y así sucesivamente», «…» | serie abierta | `\dots` |

Las tres confusiones más frecuentes y cómo evitarlas:

- **Derivación vs. génesis.** Derivación es una relación lógica o de división (género → especie,
  condición → condicionado). Génesis es un *proceso* que produce algo (una fuerza que empuja una
  facultad a su ejercicio). Si el texto habla de tiempo, fuerza o producción, es génesis (rayada).
- **Sucesión vs. génesis.** Sucesión solo ordena (A, luego B); no dice que A produzca B. Va con
  punta hueca. Si el texto afirma que A engendra B, es génesis, aunque también haya orden.
- **Reciprocidad vs. dos unilaterales.** Si el texto dice que A y B se determinan mutuamente, es
  una arista de doble punta. Si dice que A determina a B *y* B (de otra manera) a A, son dos
  aristas distintas, cada una con su nombre.

---

## 1. Derivación

**Cuándo:** determinación fuerte, división género → especie, de la condición a lo condicionado.
Es la relación por defecto de los árboles. **Trazo:** sólido, punta llena (`derivacion`).

**Corpus:** 24 (Aristóteles: cualidad → animal/planta → alas/pies → bat/dove), 17
(intensivo → extensivo: «Explication», «Covering»), 06 (teorización).

```latex
% baja 0.6 desde el padre y el codo -| lleva el trazo hasta la vertical de cada hijo
\draw[derivacion, rounded corners=6pt] (quality.south) -- ++(0,-0.6) -| (animal.north);  % e1
\draw[derivacion, rounded corners=6pt] (quality.south) -- ++(0,-0.6) -| (plant.north);   % e2
```

**Trampa:** una arista sin nombre solo es aceptable cuando la relación es la división o
derivación por defecto del arquetipo. Fuera de un árbol, rotúlala.

## 2. Sucesión

**Cuándo:** orden dentro de una serie o transición; no afirma producción. **Trazo:** sólido o
rayado, punta **hueca** (`sucesion`, `sucesion rayada`, `sucesion larga`).

**Corpus:** 22 (hábito: A → B → A), 21 (*Succession* entre Pasado, Presente y Futuro, en
rayas largas), 04 (Need → Brain → Affect).

```latex
\draw[sucesion larga] (n1) -- node[rotulo=18, above=2pt] {\textit{Succession}} (n2);  % e1
```

**Trampa:** la punta hueca es lo que distingue sucesión de derivación. Si dibujas una serie
con puntas llenas, estás diciendo «determina». Y una enumeración («primera, segunda, tercera
síntesis») **no es sucesión** si el texto no afirma un orden de aparición: numerar los nodos
basta, sin flechas.

**Relaciones entre teorías** (una reformula, sustituye o reconstruye a otra): el léxico no
tiene un trazo propio; usa `sucesion` con el nombre del autor en el rótulo (*Ramsey–Sneed*,
*T-theoretical*) y di en la leyenda que es «paso de una teoría a otra».

## 3. Génesis

**Cuándo:** actualización, fuerza que empuja, algo que se produce en el tiempo. **Trazo:**
rayado, punta llena (o hueca si lo producido es virtual o meramente posible): `genesis`,
`genesis hueca`.

**Corpus:** 08 (*Force* de cada facultad a su ejercicio trascendental), 20 (acoplamiento →
sistema), 18 (nivel *Ontological*).

```latex
\foreach \y in {-5.45,-7.86} {
  \draw[genesis] (3.3,\y) -- (4.85,\y);
  \node[rotulo=21] at (3.9,\y+0.25) {\textit{Force}};
}
```

## 4. Virtual

**Cuándo:** relaciones débiles, de correspondencia o de segundo orden: repetición, encarnación,
disfraz, desplazamiento; lo que *no* es una determinación sino una expresión. **Trazo:**
punteado fino, punta hueca (`virtual`; `virtual fuerte` si el punteado es grueso).

**Corpus:** 23 (*Disguise* y *Displacement* entre el objeto virtual V1 y los objetos reales
R1, R2), 26 (*Embedding*), 21 (las tres repeticiones desde el yo fracturado).

```latex
\draw[virtual] (v1) to[out=-100, in=60] node[rotulo=20] {\textit{Disguise}} (r1);   % e1
\draw[virtual] (r1) -- node[rotulo=20] {\textit{Displacement}} (r2);                  % e2
```

## 5. Operación singular del autor

**Cuándo:** el autor da nombre propio a una operación que no es ni derivación ni génesis:
*Cloning*, *Extraction*, *Reduction* (Laruelle), *expectation* (Deleuze, hábito),
traslación/rotación (Bergson), contracción. **Trazo:** raya-punto (`operacion`; `operacion
hueca` si el término de llegada queda sin determinar).

**Corpus:** 02 y 13 (*Cloning*, *Extraction*, *Reduction*), 22 (*expectation*), 03
(*translation/rotation* de cada sección del cono a su imagen).

```latex
\draw[operacion] (x1) -- node[rotulo=24] {\textit{extraction}} (x2);   % e1
\draw[operacion] (one) -- node[rotulo=24] {\textit{Cloning}} (clone);   % e2
```

**Trampa:** el rótulo es **obligatorio**: la forma raya-punto dice «operación del autor», y el
nombre dice cuál. Si dos figuras de referencia ponen la misma operación entre términos distintos,
vale lo que dice el texto; si no lo tienes, elige una y anótalo en el libro.

## 6. Reciprocidad

**Cuándo:** correlación, interdependencia, paralelismo; los dos términos se codeterminan. **Trazo:** doble punta. La
fuerza de la relación baja con el trazo: `reciproca` (sólido, fuerte) → `reciproca rayada`
(media) → `reciproca debil` (punteado, paralelismo o correspondencia).

**Corpus:** 07 (síntesis trascendental entre sensibilidad y entendimiento), 25
(*Interdependency*), 02 (*Parallelism*), 14 (*Decision* entre inmanencia y trascendencia),
08 (*Transcendental Exercise* entre facultad y objeto).

```latex
\draw[reciproca debil] (a) -- node[rotulo=24] {\textit{Parallelism}} (b);   % e1
\draw[reciproca rayada] (immanence) -- (transcendence);                      % e2
```

**Trampa:** no uses doble punta «por simetría visual». Es una afirmación fuerte: A y B
dependen el uno del otro. Si el texto no lo dice, es unilateral o es una correspondencia débil.

## 7. Unilateralidad

**Cuándo:** A determina a B sin ser determinado por B. Es el caso de prueba de la fidelidad:
la determinación en última instancia de Laruelle, la distinción unilateral, la causa
ocasional. **Trazo:** **una sola punta, nunca doble** (`unilateral`; `unilateral fuerte` si el
texto la da como derivación plena). A veces un bucle que no se cierra: la ida y la vuelta se
dibujan como dos aristas distintas, cada una con su nombre, para que no parezcan una
reciprocidad.

**Corpus:** 14 (*Unilateral Cause / Determination-in-the-Last-Instance* del Uno a la
Dualidad; *Unilateral Distinction / Duality-Without-Synthesis* de vuelta), 02 (*Determination
in the last instance*), 13, 15.

```latex
\draw[unilateral, rounded corners=4pt] (one.north) -- ++(0,0.6) -| (duality.north);    % e1
\node[rotulo=22] at (3,4.4) {\textit{Unilateral Cause}};
\draw[unilateral, rounded corners=4pt] (duality.south) -- ++(0,-0.6) -| (one.south);   % e2
\node[rotulo=22] at (3,2.2) {\textit{Unilateral Distinction}};
```

`scripts/revisar.py` marca como error una arista declarada `unilateral` en el libro de
fidelidad cuyo código tenga doble punta.

## 8. Inclusión y subsunción

**Cuándo:** un término queda comprendido en otro. **Trazo:** o una flecha con **etiqueta
verbal** («is subsumed by», «is realized in»), o un **encastre espacial** (una teoría
dibujada dentro de otra).

**Corpus:** 01 (cada principio ético *is subsumed by* su correlato político, con una segunda
línea fina rayada que nombra el modo: «realization in institutional and political terms»),
29 (la teoría virtual contiene un modelo contraparte, que contiene otra teoría).

```latex
\node[font=\px{23}] at (7.55,\ya+0.28) {is subsumed by};
\draw[subsuncion] (5.75,\ya) -- (9.38,\ya);            % e1
```

## 9. Autorreferencia y paradoja

**Cuándo:** el texto muestra que un término se aplica a sí mismo o viola su propio nivel (un
conjunto que se contiene a sí mismo, el «elemento rebelde»). **Trazo:** un **arco** que salta
de nivel y vuelve sobre un elemento del propio nivel, punteado fino, punta hueca (`paradoja`).

**Corpus:** 12 (*Paradox of the Abnormal Set*, *Paradox of the Rebel Element*: en el panel
del sinsentido, un nodo «Animal» aparece donde debía haber «Bird» y otro donde debía haber
«Fruit»).

```latex
\draw[paradoja] (3.27,-16.62) .. controls (2.55,-16.6) and (2.7,-14.55) .. (4.88,-14.55); % e1
\node[termino] at (1.3,-15.65) {Paradox of the\\Abnormal Set};
```

## 10. Retroalimentación

**Cuándo:** un nivel superior reelabora o explicita los inferiores. **Trazo:** un **haz de
arcos punteados** que suben desde un mismo nodo hacia todos los niveles que reelabora
(`retroalim`).

**Corpus:** 28 (*Global Explicitation* desde la sistematización hacia cada nivel inferior;
*Local Explicitation* entre dos niveles contiguos), 36.

```latex
\foreach \c in {3.04, 2.55, 2.04, 1.58, 1.05}   % control de cada arco, más abierto cuanto más lejos
  \draw[retroalim] (sis.west) .. controls (\c,7.90) and (\c,3.0) .. (mat.west);
```

## 11. Retorno, rechazo, metamorfosis

**Cuándo:** relaciones entre dos series o dos regiones lejanas del diagrama que ni suceden ni
derivan: el eterno retorno, el rechazo de un término, la metamorfosis. **Trazo:** **arco
punteado de doble punta** entre las regiones (`retorno`).

**Corpus:** 21 (*Refusal*, *Metamorphosis*, *Eternal Return*, entre el antes y el después de
la cesura). El eterno retorno aquí **no es un cuarto término** de la serie, es una relación
entre series.

```latex
\draw[retorno] (14.9,6.77) .. controls (17.4,6.75) and (17.4,8.2) .. (17.4,9.5)
               .. controls (17.2,11.8) and (16.2,13.0) .. (14.58,13.02);              % e1
\node[rotulo=32] at (17.42,9.35) {\textit{Eternal\\Return}};
```

## 12. Anulación y exclusión

**Cuándo:** el texto dice que un término queda anulado o excluido (una magnitud variable que
se cancela en el límite). **Trazo:** línea punteada hasta el punto de anulación, con la
etiqueta **«Cancelled»**, o el elemento tachado con `\tachar{(x,y)}`.

**Corpus:** 16 (Bordas-Demoulin: la *Quantitas* variable se cancela y queda la
*Quantitativity* continua). También sirve para una arista que **niega** algo que el texto
afirma que no hay (los objetos de la noesis «sin imágenes»): lleva estatus `textual`, como
cualquier otra, y el pasaje es el que lo niega.

```latex
\draw[anulacion] (10.15,-8.35) -- (10.15,-9.12);
\node[rotulo=22] at (10.1,-9.12) {\textit{Cancelled}};
```

## 13. Totalización

**Cuándo:** el texto agrupa varios términos bajo un nombre («las síntesis de reconocimiento»,
«la forma pura y vacía del tiempo»). **Trazo:** **llave**. Sólida si la agrupación es
definicional (`totalidad`); rayada si la totalidad es virtual (`totalidad virtual`); punteada
si es abierta (`totalidad abierta`).

**Corpus:** 27 (*Cognition*, llave gruesa rayada sobre todos los niveles), 21 (*Pure and Empty
Form of Time*, llave punteada), 37 (llaves anidadas: sentient ⊂ sapient).

```latex
% la punta de la llave queda a la izquierda del sentido del trazo
\draw[totalidad virtual, llave=1.7cm] (14.12,16.38) -- (4.08,16.38);        % g1
\node[subtitulo=40] at (9.10,17.90) {Pure and Empty Form of Time};
```

## 14. Orientación, ejes y gradientes

**Cuándo:** una tendencia global que atraviesa varios nodos: contracción/dilatación,
vida→muerte, monotonicidad. **Trazo:** **flecha larga al margen**, raya-punto (`eje`) o
punteada (`eje virtual`), con un rótulo en cursiva.

**Corpus:** 23 (*Dilation* y *Contraction*), 28 (*Functional Embedding*), 05 (*Catharsis*,
de la vida a la muerte).

```latex
\draw[eje] (1.52,16.75) -- (1.52,4.95);                    % x1
\node[rotulo=30] at (0.63,9.15) {\textit{Dilation}};
```

## 15. Serie abierta

**Cuándo:** el texto deja una serie sin cerrar. **Trazo:** «…» (`\dots`). No la cierres, no
agregues un último término «por equilibrio».

**Corpus:** 20 (la serie a—a′ … c—c′), 24 («…» entre especies).

---

## Reglas complementarias

**El estatus ontológico se codifica en el contorno.** Lo actual o determinado lleva contorno
sólido (`caja`); lo virtual o indeterminado, rayado (`caja virtual`); lo incognoscible o
contraparte, punteado (`caja abierta`); lo que aún no es, raya-punto (`caja futura`).
Ejemplos: V1 rayado frente a R1 sólido (23); el Futuro en raya-punto (21); *Things-in-Themselves*
en paralelogramo rayado (27); el modelo contraparte punteado (29).

**El grosor jerarquiza.** El camino principal va grueso (30 *Homomorphic Embedding*; 31 S←…→U)
y lo secundario, fino. Se compone sobre el estilo: `\draw[derivacion, line width=2pt]`.

**Si el texto nombra la relación, la arista lleva su nombre**, en cursiva pequeña sobre fondo
blanco (`rotulo`): *Coupling*, *Succession*, *Reciprocal Determination*, *Implication*. Una
arista sin nombre solo es aceptable cuando la relación es la división o derivación por defecto
del arquetipo.

**Un nodo es «término + (alias o función)»**: «Id (*Habitus*)», «Ego Ideal
(*Eros-Mnemosyne*)». Cuando el texto da una fórmula propia del concepto, va citada en cursiva
dentro del nodo («"The act is too big for me"»).

**Los niveles se nombran al margen** en versalitas o negrita: FORMS/METHODS/STAGES,
COMMON SENSE/GOOD SENSE, STRUCTURAL (THINKING)/FUNCTIONAL (DOING)/ONTOLOGICAL (BEING). Estilo
`nivel`.

## Ampliar el léxico

Un texto puede exigir una relación que el léxico no tiene. Está permitido, con tres condiciones:

1. El trazo nuevo se **define con nombre semántico** (`\tikzset{nombre/.style={…}}` en el
   propio `.tex`, no en la `.sty` compartida), de modo que el código se lea como la tabla.
2. Se **define en la leyenda del diagrama** (`\muestra{nombre}{x}{y}{qué significa}`).
3. Se **añade a este archivo**, con el pasaje que lo motivó, para que la próxima vez no haya
   que reinventarlo.

Antes de crear un trazo, comprueba que no baste combinar los existentes: casi siempre una
combinación de *trazo (sólido, rayado, punteado, raya-punto)* × *punta (llena, hueca, doble)* ×
*grosor* × *rótulo* dice lo que hace falta.
