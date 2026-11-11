# Catálogo de arquetipos

El arquetipo es la **figura** del diagrama. Se elige por la lógica del texto, no por costumbre:
una génesis pide una cascada; una división por género y especie, un árbol; una correlación entre
dos órdenes, columnas en paralelo; un pasado que se contrae en un presente, un cono. Elegir
mal es el error más caro, porque ninguna cantidad de pulido arregla una figura que dice otra
cosa que el texto.

Cada arquetipo tiene una **plantilla compilable** en `assets/plantillas/` (cópiala, renombra
los nodos y cambia los estilos de arista por los que pida el texto) y **ejemplos resueltos** en
`assets/ejemplos/` (el prefijo del nombre es el arquetipo). Se pueden combinar: el 08 es
cascada + columnas en paralelo + bucles. Cada parte tiene que ser legible por sí sola.

**Contenido:** [Cuál elegir](#cuál-elegir) · [1 Árbol](#1-árbol-de-división) ·
[2 Cascada](#2-cascada-genética) · [3 Columnas](#3-columnas-en-paralelo) ·
[4 Estratos](#4-estratos-con-rótulos-al-margen) · [5 Geometría](#5-geometría-conceptual) ·
[6 Triángulo](#6-triángulo-de-mediación-y-distinción-unilateral) ·
[7 Serie](#7-ciclo-frente-a-línea-y-series-temporales) · [8 Paneles](#8-paneles-comparativos) ·
[9 Matriz](#9-matriz-o-tabla-conceptual) · [10 Jerarquía](#10-jerarquía-con-retroalimentación-o-tubería) ·
[11 Anidamiento](#11-anidamiento-o-alcance)

## Cuál elegir

Hazte estas preguntas sobre el texto, en este orden; la primera que responda «sí» decide.

| Pregunta | Arquetipo |
|---|---|
| ¿El texto contrapone **dos versiones** de una misma estructura (lo regular y lo paradójico, filosofía y no-filosofía)? | 8 Paneles |
| ¿El texto usa o justifica **una figura espacial** (cono, círculos, reloj de arena, elipse)? | 5 Geometría |
| ¿Hay un proceso que **engendra** términos de lo virtual a lo actual, o de condiciones a condicionados? | 2 Cascada |
| ¿Hay un **género** que se divide en especies? | 1 Árbol |
| ¿Hay **dos órdenes** cuyos términos se corresponden fila a fila? | 3 Columnas |
| ¿Hay **niveles** de un mismo proceso (estructural / funcional / ontológico)? | 4 Estratos |
| ¿Hay una **síntesis** frente a una distinción sin síntesis (mediación / unilateralidad)? | 6 Triángulo |
| ¿Hay **tiempo**: serie, ciclo frente a línea, sucesión de teorías? | 7 Serie |
| ¿Hay **dominios cruzados con niveles**? | 9 Matriz |
| ¿Un nivel superior **reelabora** los inferiores, o hay una tubería de entradas y salidas? | 10 Jerarquía |
| ¿Un modelo, teoría o dominio está **dentro de otro**? | 11 Anidamiento |

Si ninguna encaja del todo, probablemente el texto tiene **dos tesis**: dibuja dos diagramas, o
combina dos arquetipos y comprueba que cada parte se lee sola. Justifica la elección en una
línea al entregar («cascada porque el texto describe una génesis, no una clasificación»).

---

## 1. Árbol de división

**Cuándo:** clasificaciones, representación aristotélica género → especie → diferencia.
**Plantilla:** `plantillas/arbol.tex`. **Ejemplos:** 24 (Aristóteles), 33–34 (grupos
nominales), 35 (forma teórica), 04, 06.

- Las ramas son `derivacion`; los niveles se rotulan al margen en versalitas
  («GENERIC DIFFERENCE», «SPECIFIC DIFFERENCE»).
- Las hojas son texto suelto, no cajas: en el 24 solo los nodos de género van en caja porque
  la caja *significa* «categoría».
- **Riesgo:** imponer jerarquía donde el texto ve una red. Si un término depende de dos padres,
  el árbol miente; usa cascada o matriz.

## 2. Cascada genética

**Cuándo:** génesis, actualización, derivación de las condiciones a lo condicionado. Puede ir
de arriba abajo (lo virtual se actualiza) o de abajo arriba (las condiciones fundan).
**Plantilla:** `plantillas/cascada.tex`. **Ejemplos:** 08 (doble génesis), 18 (Maimon),
20 (ur-síntesis), 27 (cognición en Kant), 17 (intensivo/extensivo), 02, 16.

- Las flechas son `genesis` (rayadas) con el nombre del autor en el rótulo (*Force*,
  *Coupling*, *Transcendental Exercise*).
- Los niveles van al margen. La figura se lee de un camino principal claro; las relaciones
  secundarias (correlaciones laterales) van más finas.
- **Riesgo:** convertir en causal lo que el texto presenta como condición lógica. Si no hay
  proceso ni tiempo, es derivación sólida, no génesis.

## 3. Columnas en paralelo

**Cuándo:** correlación entre dos órdenes (ética ↔ política, sensibilidad ↔ entendimiento,
sustancia ↔ forma, S ↔ U). **Plantilla:** `plantillas/columnas.tex`. **Ejemplos:** 01, 07, 09,
25, 31.

- Cada fila une un término de cada columna con una arista de doble punta (`reciproca debil`
  para correspondencia, más fuerte si el texto lo dice) rotulada.
- Dentro de cada columna puede haber una secuencia (`derivacion`, `sucesion`).
- **Riesgo:** inventar correspondencias para completar filas. Si un término no tiene par en el
  texto, la fila queda vacía de ese lado.

## 4. Estratos con rótulos al margen

**Cuándo:** niveles de un mismo proceso o de una misma escala; el texto dice «tres niveles»,
«cuatro estratos». **Plantilla:** `plantillas/estratos.tex`. **Ejemplos:** 06, 19, 26, 30, 33.

- Rótulo del nivel al margen (`nivel`), contenido a la derecha, llaves para agrupar los niveles
  que el texto agrupa bajo un nombre (*Cognition* sobre tres síntesis).
- **Riesgo:** perder la dirección. Si los niveles se condicionan, las flechas verticales lo
  dicen; si son simples capas, no dibujes flechas.

## 5. Geometría conceptual

**Cuándo:** una forma espacial **es la tesis**: cono (03 Bergson, 23 memoria), círculos
concéntricos (09, 10), semidiscos con cesura (21), elipse envolvente (05, 22), rombo como
campo (20), reloj de arena (32), plano o paralelogramo (03, 27). **Plantilla:**
`plantillas/geometria.tex`. **Solo cabe cuando el propio texto usa o justifica la figura.**

- La figura lleva contorno según estatus: el cono de lo virtual, rayado o punteado; el plano
  de lo actual, sólido.
- Los ejes globales (contracción/dilatación) van al margen como `eje`.
- **Riesgo:** decorar. Una elipse sin que el texto hable de envolvente es adorno; peor,
  sugiere una tesis que el autor no sostiene.

## 6. Triángulo de mediación y distinción unilateral

**Cuándo:** una síntesis dialéctica (dos términos mediados por un tercero) frente a una
no-síntesis donde la relación es unilateral. **Plantilla:** `plantillas/triangulo.tex`.
**Ejemplos:** 14 (filosofía / no-filosofía), 13, 15.

- Arriba, doble punta; abajo, una sola. Es el arquetipo en el que más se nota si simetrizaste.
- **Riesgo:** dibujar la distinción unilateral con la misma forma que la mediación, que borra
  precisamente lo que el autor quiere mostrar.

## 7. Ciclo frente a línea y series temporales

**Cuándo:** el texto tiene tiempo: dos lecturas del tiempo (ciclo Cronos / línea Aion), serie
ordinal (pasado–presente–futuro), hábito (A→B→A), sucesión de teorías. **Plantilla:**
`plantillas/serie.tex`. **Ejemplos:** 11, 21, 22, 29.

- La serie va con `sucesion` (punta hueca); la cesura parte la serie; los retornos entre
  series con `retorno`; la totalidad con llave.
- **Riesgo:** cerrar una serie que el texto deja abierta, o añadir un término «por equilibrio»
  (tres síntesis son tres, no cuatro).

## 8. Paneles comparativos

**Cuándo:** dos versiones de la misma estructura que muestran una diferencia. **Plantilla:**
`plantillas/paneles.tex`. **Ejemplos:** 11, 12 (ley regular / sinsentido), 14–15, 33/34.

- **Las dos mitades comparten disposición**, para que la diferencia salte a la vista: dibuja la
  estructura una sola vez como macro y aplícala dos veces, cambiando solo lo que el texto
  dice que cambia.
- **Riesgo:** que los paneles difieran en cosas que el texto no dice (otra disposición, otro
  tamaño): el lector buscará una diferencia que no existe.

## 9. Matriz o tabla conceptual

**Cuándo:** dominios cruzados con niveles. **Plantilla:** `plantillas/matriz.tex`.
**Ejemplos:** 05 (vida filosófica: ontología, epistemología, estética… por niveles de la
línea dividida), 07 (categorías en cuatro grupos con llaves y combinación), 30 (grilla 3×5
con dos ejes: estructural/funcional/ontológico × cinco componentes).

- Cabeceras en cursiva negrita, celdas con vocabulario del autor, ejes como flechas al margen
  o entre celdas (`gruesa`, para la relación principal).
- **Riesgo:** una matriz que es una tabla de Word. Si las celdas no se relacionan entre sí por
  flechas o ejes, quizá no necesitas diagrama.

## 10. Jerarquía con retroalimentación o tubería

**Cuándo:** una jerarquía funcional donde el nivel superior reelabora los inferiores, o una
tubería de entradas y salidas. **Plantilla:** `plantillas/jerarquia.tex`. **Ejemplos:** 28
(explicitación local/global), 36 (jerarquía semántica), 37 (IN/OUT con llaves anidadas).

- Cajas apiladas con `derivacion`, y un haz de arcos `retroalim` desde el nivel que reelabora.
- **Riesgo:** que el haz de arcos tape los rótulos; escalona la apertura de cada arco.

## 11. Anidamiento o alcance

**Cuándo:** modelos dentro de modelos, un dominio dentro de otro. **Plantilla:**
`plantillas/anidamiento.tex`. **Ejemplos:** 29 (teoría virtual dentro de otra), 10 (estratos
anidados).

- El encastre espacial *es* la inclusión; el contorno dice el estatus (sólido, rayado,
  punteado). No añadas flecha de «contiene»: sería redundante.
- **Riesgo:** profundidad ilegible. Más de tres niveles de anidamiento pide otro arquetipo.
