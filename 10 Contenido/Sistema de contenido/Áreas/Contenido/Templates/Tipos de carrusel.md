# Tipos de carrusel

**Qué carrusel se hace para cada pieza.** Lo usa `/carrusel` para elegir el tipo y
`/plan-mensual-contenido` para anotarlo al escribir la pieza. Las reglas generales (portada, una idea
por lámina, cierre con un solo CTA) están en [Cómo se arma una pieza](C%C3%B3mo%20se%20arma%20una%20pieza.md).
Esto dice **qué esqueleto usar**.

---

## Cómo se elige: tres preguntas, en este orden

**1. ¿Qué pilar es la pieza?** Achica la lista:

| Pilar | Tipos posibles |
|---|---|
| **Autoridad** 🧭 | Paso a paso · Lista · Mito o realidad · Comparativa · Checklist · Dato |
| **Espejo** 🪞 | Espejo · Lista (de situaciones, no de consejos) |
| **Conexión** 🤝 | Historia · Lista (de razones, con prueba) · Dato (números propios verificados) |
| **Inspiración** 🌟 | Frases |
| **Oferta** 💸 | Oferta |

**2. ¿Qué forma tiene el contenido?**

| Si el contenido... | Tipo |
|---|---|
| tiene un **orden** que no se puede cambiar | **Paso a paso** |
| son **opciones para elegir** | **Comparativa** |
| desarma **creencias falsas** | **Mito o realidad** |
| es **lo que hay que llevar o tener listo** | **Checklist** |
| gira alrededor de **un número fuerte** | **Dato** |
| son **ítems sueltos del mismo tipo**, sin orden | **Lista** |
| es **una sensación** que la persona reconoce | **Espejo** |
| son **frases** para guardar o mandar | **Frases** |
| es **una persona real** que cambió algo | **Historia**, solo con permiso escrito |

**3. ¿Qué acción busca?** Define el cierre:

| Busca | Cierre |
|---|---|
| Que lo guarde (Checklist, Paso a paso, Lista) | Una razón para volver a mirarlo: "lo vas a necesitar el día que..." |
| Que comente (Mito o realidad, Comparativa) | Una pregunta que se contesta con una palabra: "¿Cuál te toca?" |
| Que escriba (Oferta) | El CTA de `marca.json`, solo |
| Que siga a la cuenta (Espejo, Historia) | Sin CTA de venta: lo que viene en la cuenta |

**Si dos tipos empatan**, gana el que mejor guardado tuvo en el último informe de `Investigación/`.
Sin datos, gana el de menos láminas.

---

## Los diez tipos

Todos usan el mismo estilo con la paleta que toque, una o dos láminas claras y una de golpe. Las clases
son de `base.css` → [Estilo de carrusel](Estilo%20de%20carrusel.md).

### 1 · Paso a paso · Autoridad

**Para:** procesos con orden. **Largo:** 6-9 láminas.

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | Promesa con el número de pasos: "{{El proceso}} en 5 pasos" | `h1.xl`, `.mano.grande`, `.sticker` |
| 2 | Por qué importa el orden (segundo gancho): "El 3 es donde se traba casi todo el mundo" | `h2` |
| 3..N-1 | Un paso por lámina: "Paso #0N" a mano, título, una línea o filas con recuadro | `.mano.grande`, `h3`, `p` o `.filas` |
| N | Recapitula los pasos en una línea cada uno + cierre de guardar | `.pasos` |

### 2 · Lista · Autoridad o Espejo

**Para:** ítems del mismo tipo sin orden: errores, consejos, señales. **Largo:** 5-9 láminas.
**El mejor ítem va último y se anuncia en la lámina 2.**

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | "N errores que…": número y promesa | `h1.xl`, `.sticker` |
| 2 | Para quién es y "el último es el que casi nadie sabe" | `h2` |
| 3..N-1 | Un ítem por lámina: el número a mano, el ítem grande, una línea | `.mano.grande`, `h2`, `p`, `.barra` |
| N | Cierre según la acción | — |

### 3 · Mito o realidad · Autoridad

**Para:** creencias que frenan o confunden. **Largo:** 5-8 láminas. **Engancha comentarios.**
Toda "realidad" sale de [Conocimiento](../../../Empresa/Conocimiento/Conocimiento.md).

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | "¿Mito o realidad?" + la creencia más difundida | `h1` |
| 2..N-1 | La creencia arriba (etiqueta MITO, tachada) y la realidad abajo, grande | `.etiqueta.mito`, `.tachado`, `.etiqueta`, `h2` |
| N | "¿Cuántas sabías?" | — |

### 4 · Comparativa · Autoridad

**Para:** elegir entre opciones. **Largo:** 1 portada + 1 por opción + resumen + cierre.
**Toda opción usa la misma ficha, con las mismas filas y en el mismo orden.**

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | Las opciones en grande + "¿Cuál necesitás?" | `h1.xl`, `.sticker` |
| 2 | Lo que tienen en común, o el dato que cambia la decisión | `h2` |
| 3..N-2 | Una opción por lámina, con foto si hay, y la ficha | `.foto-redonda`, `.ficha` |
| N-1 | Tabla resumen de todas | `.tabla` |
| N | Cierre: pregunta o CTA | `.boton.wa` |

### 5 · Checklist · Autoridad

**Para:** lo que hay que llevar o tener listo. **Es el que más se guarda.** **Largo:** 4-6 láminas.

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | "Lo que tenés que tener antes de…" | `h1` |
| 2-3 | La lista, máximo 6 ítems por lámina | `.check` |
| N-1 | "Lo que casi todos se olvidan": un solo ítem destacado | `h2`, `.marcador`, `.barra` |
| N | Por qué conviene tenerla a mano | — |

### 6 · Dato · Autoridad o Conexión

**Para:** un número que sorprende, de una fuente oficial o de [Números.md](../../../Empresa/N%C3%BAmeros.md).
**Largo:** 3-5 láminas. **Ningún número sin fuente en la última lámina.**

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | La cifra, enorme, y una línea | `.cifra` |
| 2 | Qué quiere decir | `h2`, `p` |
| 3 | Qué hacer con eso | `.barra` o `.check` |
| N | Fuente y fecha en chico + cierre | `p.chico` |

### 7 · Espejo · Espejo

**Para:** que la persona se sienta entendida. **No enseña nada y no vende nada.** **Largo:** 4-7
láminas. Variante: paleta `noche`, sin stickers ni lámina de golpe: tono más íntimo.

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | "Si alguna vez pensaste esto…" | `h1` |
| 2..N-2 | Una frase que la persona diría, por lámina (de [Personas.md](../../../Empresa/Personas.md)) | `.cita` |
| N-1 | El giro: no sos la única persona, y un dato que lo prueba | `h2` |
| N | Lo que viene en la cuenta. **Sin oferta** | — |

### 8 · Historia · Conexión

**Para:** un cliente real que cambió algo. **Solo con su permiso escrito.** **Largo:** 5-7 láminas.

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | El antes, en una frase de él o ella | `.cita` |
| 2 | Qué lo frenaba | `h2` |
| 3-4 | Qué cambió, concreto. Su mensaje real, si lo autorizó | `.pasos` o `.captura` |
| 5 | El después, con foto si hay | `.foto-mitad` |
| N | Cierre que conecta con quien está en el antes | — |

### 9 · Oferta · Oferta

**Para:** la promoción del mes. **Una sola en el feed por mes.** **Largo:** 3-4 láminas. **Todo monto
sale de [Catálogo.md](../../../Empresa/Cat%C3%A1logo.md) o queda `[CONFIRMAR]` y no se exporta.**

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | Qué es y hasta cuándo | `h1` |
| 2 | Qué incluye | `.check` |
| 3 | El precio | `.cifra` |
| 4 | Cómo empezar + CTA | `.boton.wa` |

### 10 · Frases · Inspiración

**Para:** el pilar Inspiración. **Se guarda y se manda:** es el tipo que más se comparte.
**Largo:** 5-8 láminas.

| Lámina | Qué va | Clases |
|---|---|---|
| 1 | El tema: "Lo que nadie te dice de {{tu tema}}" | `h1.xl`, `.sticker` |
| 2..N-1 | Una frase por lámina, 20 palabras como mucho. Arriba, a mano, para quién es | `.frase`, `.resalta`, `.mano.chica` |
| N | En la lámina de golpe: la frase más corta y "Mandásela a quien la necesita" | `.slide.golpe`, `.frase` |

**Las frases:** concretas, de tu tema, con tu trato. Nada de "¡Vos podés!" ni citas de famosos.

### LinkedIn (si el módulo está activo)

Se sube como **documento PDF** (`<body class="paleta-principal linkedin">`: numera las láminas y
`render.py` arma `carrusel.pdf`). Mismo estilo, sin stickers ni letra a mano. Tono más formal, mismo trato.

**A · Educativo:** portada (gancho de 6 palabras o menos) · lo que está en juego (un costo o riesgo
con fuente) · una idea por lámina (título de 3-7 palabras, 25 palabras como mucho) · resumen · cierre
con una acción. **7 a 10 láminas.**

**B · Caso de un cliente empresa:** foto real + "Trabajamos con [empresa] en [tema]" · qué necesitaba
· qué hicimos · cómo fue (fotos) · lo que se llevaron (nada inventado) · cierre. **Solo con permiso
escrito de la empresa**; sin permiso, se cuenta sin nombre.

---

## Lo que vale para los diez

- **Formato 4:5, 1080 × 1350.** Lo resuelve `base.css`
- **Una paleta por carrusel**, una o dos `.clara` y una sola `.golpe`
- **Sin contador:** Instagram ya muestra "1/9"
- **Si sobra aire, se agranda la letra.** Texto corrido a 23px de CSS; mínimo 18px (`p.chico`). Si no
  entra, son dos láminas
- **El texto de la portada, lejos del borde** (60px de CSS por lado): la grilla del perfil recorta
- **Lámina resumen antes del cierre** cuando el tipo lo permite: es la que se captura y se manda
- **La lámina 2 funciona sola:** Instagram puede mostrar el carrusel arrancando desde ahí
- **Nada de guion largo (—)**
