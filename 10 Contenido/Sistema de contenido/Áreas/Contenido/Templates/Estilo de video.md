# Estilo de video

**Cómo se ven los videos de la marca, cómo se filman y cómo se escribe la lista de cortes.** Lo usa
`/editar-video`. Las reglas del contenido (gancho, largos, pie) están en
[Cómo se arma una pieza](C%C3%B3mo%20se%20arma%20una%20pieza.md); esto es la forma.

**La cuenta, las paletas y el logo salen de `Empresa/Marca/marca.json`.** Las letras del video son las
del kit por defecto (Switzer, Poppins, Instrument Serif): cambiarlas es una tarea para Claude con la
skill `design-system`, porque toca `video.py`.

---

## La ficha de estilo

**Lo que hace que un video se vea de la marca.** Se cambia acá, no video por video.

| | Regla |
|---|---|
| **Tipografía** | La misma letra de títulos que los carruseles, en el gancho, los gráficos y los subtítulos |
| **Colores** | La **paleta** del video (una de `marca.json`, como los carruseles): el gancho en el color de base con la palabra clave en acento, los gráficos en el color de golpe |
| **Subtítulos** | **De a una palabra, centrada**, un poco abajo del medio. Lo destacado, sobre un rectángulo del color de acento. `"palabras_por_vez": 3` vuelve a tandas |
| **Ritmo** | Tomas de 1,5 a 3 segundos. Sin silencios ni repeticiones |
| **Gráficos** | Uno por video, para el dato que hay que ver: un número, una regla, un paso |
| **Voz** | Lo que dice quien habla no se reescribe en los subtítulos: se corrige la transcripción |
| **Encuadre** | Vertical, sin bandas. Cámara quieta; el movimiento lo dan los cortes |

## Los cuatro tipos de video

Cada video del plan dice cuál es (`"tipo"` en el `edl.json`). Los tres primeros no necesitan a nadie
a cámara; el cuarto, sí.

| | **Frases** (`frases`) | **Info** (`info`) | **Inspiración** (`inspiracion`) | **A cámara** (`instructor`) |
|---|---|---|---|---|
| **Qué es** | Tomas que van cambiando y **frases que cambian con corte seco**, de 2 a 6 | **Una sola toma** y un **texto fijo, centrado**, que explica algo | Igual que Info, pero **poético** | Alguien explica a cámara: se corta lo que dice y se edita todo |
| **Para qué** | Un tip, un error común, un paso, un "esto sí / esto no" | Requisitos, qué llevar, cómo es algo: lo que se lee en 5 segundos | Pilar Inspiración | Enseñar con autoridad; sirve para anuncios |
| **Título** | Sí, si suma: limpio y arriba todo el video | El renglón de arriba (`kicker`) | No | Sí: centrado, aparece de una |
| **Destacado** | Palabras en acento con subrayado a mano | En acento | En itálica y acento | La palabra sobre un rectángulo de acento |
| **Animación** | El subrayado; si hace falta listas, ✓/✗, círculo, recortes | Ninguna | Ninguna | Zooms, insertos, capítulos, recortes, blanco y negro, listas, ✓/✗ |
| **Voz** | Sin voz **o con voz en off** (`voz`) | No | No | La de quien habla, con subtítulos |
| **Sonido** | Canción en Instagram al publicar, o `musica` | Canción en IG | Canción en IG | Voz + efectos |
| **Largo** | 8 a 20 s (unos 3 s por frase) | 5 a 10 s | 5 a 10 s | 20 a 60 s |
| **Qué se filma** | 2 a 6 tomas sin hablar | Una toma linda, estable, con lugar para el texto | Una toma con luz y aire | La persona, con el sonido, y tomas de apoyo |

**El título** (gancho): en frases va limpio (`simple`); en a cámara va con `marcador` (la palabra
clave sobre un bloque de acento). Hay otros con `"diseno"`: `subrayado`, `mezcla`, `serif`,
`espaciado`; `"turnar"` los alterna.

**Dónde va el texto:** en tomas con cielo o fondo despejado arriba, arriba (`"posicion": "cielo"`, lo
de frases por defecto). Arriba, el fondo se oscurece apenas para que se lea (`velo`).

## Videos de referencia (de afuera)

**Cuentas de otros con el ritmo o los recursos que queremos.** Colores y letras, siempre los nuestros.
Las suma `/adaptar-inspiracion` cuando la inspiración es de video.

| Link | Tipo | Qué tomamos (ritmo, recursos) |
|---|---|---|
| | | |

## Lo que ya decidimos

**Las correcciones que valen para todos los videos.** Se suman al cerrar cada video (`/editar-video`,
paso 5), con la fecha. Así el próximo hereda la decisión en vez de repetir el error.

- *Todavía ninguna.*

## Videos propios que sirven de modelo

| Video | Para qué sirve de modelo |
|---|---|
| *Todavía ninguno* | |

## La marca en video

| Elemento | Cómo es |
|---|---|
| **Placa del gancho** | Bloque del color de base, esquinas redondeadas, título grande con la palabra de `resalta` en acento |
| **Dónde va** | Arriba, debajo de la barra de Instagram, sin tocar la columna de íconos de la derecha |
| **Final** | **Sin placa de cierre** por defecto: el video termina con la última toma y la venta va en el pie |
| **Encuadre** | 9:16, 1080 × 1920, sin bandas negras: lo horizontal se recorta |
| **Volumen** | -14 LUFS, normalizado en el armado |

**Lo que no se hace:** transiciones con efecto (cortes secos, siempre), filtros de color, más de una
tipografía, texto que se mueve sin razón. **Ni video generado con IA** que muestre lugares, productos o
personas que no existen: un negocio no puede mostrar lo que no es real.

## Zonas seguras de Reels

Sobre 1080 × 1920, lo que tapa la app:

| Zona | Píxeles | Qué hay ahí |
|---|---|---|
| Arriba | 0-220 | Barra de la app |
| Abajo | 1470-1920 | Nombre de la cuenta, pie, audio |
| Derecha | los últimos 120 | Like, comentar, compartir |
| Izquierda | los primeros 60 | Margen |

`video.py revisar` las pinta de rojo sobre cada cuadro.

## Cómo se filma, para que la edición salga sola

- **Vertical, 4K o 1080p, 30 cuadros.** Lente principal, no el gran angular
- **Cámara quieta en cada plano.** Trípode o apoyada. El movimiento se hace cortando
- **A cámara:** cada frase se dice entera, y **si sale mal se repite entera** desde el principio, con
  una pausa antes. La edición se queda con la última buena. Mirar a la lente
- **Sin nadie a cámara:** 3-5 segundos de cada toma, de más. Siempre se recorta
- **Luz de frente o de costado**, nunca contraluz
- **Sonido:** micrófono de solapa si hay; si no, cerca del celular y sin ruido

## `edl.json`: la lista de cortes

Vive en la carpeta del video. Es lo único que se edita para cambiar el video.

```json
{
  "tipo": "frases",
  "segmentos": [
    { "clip": "Material/Piezas/2026-10/04-tema/IMG_0412.MOV", "desde": 3.42, "hasta": 6.10 },
    { "clip": "Material/Piezas/2026-10/04-tema/IMG_0415.MOV", "desde": 0.80, "hasta": 3.60 }
  ],
  "paleta":  "principal",
  "gancho":  { "texto": "El error que todos cometen", "resalta": "todos", "diseno": "simple" },
  "textos":  { "frases": ["Primera frase con su palabra", "Segunda frase", "Tercera frase"],
               "resalta": ["palabra", "Segunda"] },
  "portada": { "titulo": "El error de todos", "resalta": "todos", "segundo": 1.2 }
}
```

| Campo | Qué hace | Por defecto |
|---|---|---|
| `tipo` | `frases`, `info`, `inspiracion` o `instructor` (a cámara) | según `textos` |
| `segmentos` | Las tomas en orden. `desde`/`hasta` en segundos del clip. `zoom` acerca, `x`/`y` (0 a 1) mueven el recorte. `byn`: ese tramo en blanco y negro | a cámara: un ángulo distinto en cada corte (`"zooms": "no"` lo apaga) |
| `paleta` | El nombre de una paleta de `marca.json`: la misma que la portada, distinta a la publicación anterior | la de por defecto |
| `estilo_animacion` | Cómo se ven las capas: `cine-sticker` (fino, y listas como recortes blancos), `cine`, `sticker`, `fuerte`, `caja` | `cine-sticker` |
| `gancho` | El título: `texto`, `resalta`, `diseno`, `remate`, `desde`, `hasta` (sin `hasta`, todo el video), `animar` | todo el video |
| `animado` | Las capas se animan con HyperFrames (necesita Node.js 22). `false` solo si falla | `true` |
| `graficos` | Placas en el medio: `texto`, `detalle`, `desde`, `hasta` | ninguno |
| `subtitulos` | Necesita `preparar --transcribir` | sí en a cámara |
| `audio_original` | Si se escucha el sonido de los clips | sí en a cámara |
| `voz` | Voz en off: `archivo`, `desde`, `recorte`, `volumen`. Los subtítulos salen de ahí | — |
| `correcciones` | Palabra transcrita → como tiene que salir (se suman a las de `marca.json`) | — |
| `musica` | Archivo en la carpeta del proyecto, `volumen` 0 a 1. **Solo con licencia** | 0,9 sin voz · 0,12 con voz |
| `sonidos` | Efectos en cada animación (whoosh, pop, ding, error, tic). `false` los apaga | `true` |
| `cierre` | Placa final, solo si una pieza la pide: `texto`, `resalta`, `boton`, `segundos` | sin cierre |
| `listas` | Ítems que aparecen de a uno: `titulo`, `items`, `desde`, `hasta`, `paso` | — |
| `veredictos` | ✓ o ✗ grande: `tipo` (`bien`/`mal`), `texto`, `desde`, `hasta` | — |
| `flechas` | Un círculo que señala algo: `x`, `y`, `texto`, `desde`, `hasta` | — |
| `textos` | Frases, info, inspiración: `frases` o `texto`, `fuente`, `posicion`, `kicker`, `resalta`, `tiempos`, `velo`, `subrayar` | — |
| `destacar` | A cámara: palabras que salen sobre el rectángulo de acento cuando se dicen | — |
| `insertos` | Una foto o toma encima mientras sigue la voz: `archivo`, `desde`, `hasta`, `forma` (`ventana`, `arriba`, `pantalla`) | — |
| `capitulos` | "1. Título" en el centro: `numero`, `texto`, `desde`, `hasta`, `repaso` | — |
| `recortes` | Un PNG sin fondo que salta con borde blanco: `archivo`, `x`, `y`, `ancho`, `giro`, `desde`, `hasta` | — |
| `portada` | La portada del reel → `/editar-video`, *La portada* | — |

**Las capas con movimiento** las arma [HyperFrames](https://github.com/heygen-com/hyperframes)
(gratis y de código abierto) encima del video cortado, animadas con GSAP.
