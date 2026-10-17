# Estilo de carrusel

Cómo se ven los carruseles, las historias y las portadas de los reels. Lo aplica
`.claude/skills/carrusel/base.css`, con los colores, letras y logo de `marca.css` (que genera
`aplicar-marca.py` desde `Empresa/Marca/marca.json`). **Muestras armadas:** `Muestrario carrusel/` y
`Muestrario historias/` (abrir `hoja.png` de cada una). No se publican.

## Las tres reglas

1. **Un color por lámina.** Fondo + tinta + un solo acento, todo de la familia de la paleta
2. **Un logo por lámina.** Si la lámina tiene foto o logo grande, la firma va solo con la cuenta
3. **Fotos de tres formas, nada más:** media lámina sin bordes (`.foto-mitad`), redondeada
   (`.foto-redonda`) o con marco de color y etiqueta (`.foto-marco-color`). Las fotos salen de
   `Material/Fotos/`

## Las paletas: una por publicación

Cada paleta es una familia de color en tres láminas. Va en `<body class="paleta-NOMBRE">` y se alterna
entre publicaciones seguidas. Los nombres y colores están en `marca.json` → `paletas` (por defecto:
`principal`, `alterna`, `clara`, `noche`).

| Lámina | Clase | Cuántas por publicación |
|---|---|---|
| Base | `.slide` | La mayoría |
| Clara | `.slide.clara` | Una o dos, para cortar el ritmo o mostrar una foto |
| Golpe | `.slide.golpe` | **Una sola:** la que más importa, casi siempre el cierre |

## Siempre y a veces

**Siempre:** una paleta, títulos enormes, la firma con el logo abajo a la izquierda, una lámina de
golpe, "deslizá" en la portada. Sin contador: Instagram ya lo pone.

**A veces:** cada publicación elige **dos o tres** de estos, y no repite la combinación de la anterior.
Se anota en la pieza del plan (*Paleta: noche · Elementos: tachado, foto con marco, sticker*).

| Elemento | Clase | Va bien en |
|---|---|---|
| "Paso #01" a mano + filas con recuadro | `.mano.grande`, `.filas`, `.recuadro` | Procesos con orden |
| Números enormes | `.cifra` | Listas, datos |
| Sticker sobre el título | `.sticker.encima` | Portadas con remate |
| Logo grande arriba | `.logo-grande` | Marca, Oferta, Lista |
| Foto (las tres formas) | `.foto-mitad`, `.foto-redonda`, `.foto-marco-color` + `.sticker` | Cuando hay una foto real que suma |
| Círculo de luz de fondo | `.luz` | Portadas sin foto |
| Texto repetido de fondo | `.eco` | Una lámina clara de pausa |
| Mito tachado y etiquetas | `.tachado`, `.etiqueta` | Mito o realidad |
| Casillas | `.check` | Checklists |
| Pasos con línea fina | `.pasos` (un `<em>` adentro es la nota a mano) | Pasos cortos |
| Marcador o subrayado | `.marcador`, `.subrayado` | La frase que tiene que quedar |
| Nota a mano | `.mano.chica` | "acá es donde casi todos se apuran" |
| Barra de aviso | `.barra` | Lo que no se puede saltear |
| Frase grande | `.frase` | Pilar Inspiración |
| Insignia con número | `.insignia` | Un cierre que recapitula |

**Básicos:** el contenido va en `<div class="cuerpo">` (centrado en alto; `class="slide arriba"` lo
sube). `h1.xl` para portadas de 6 palabras o menos. `.resalta` para la palabra en color. `.boton.wa`
para el único CTA. `.firma` en todas, con la `cuenta` y el `descriptor` de `marca.json`.

## Las letras

Los roles están en `marca.json` → `fuentes`; los archivos, en `herramientas/fuentes/`.

| Rol | Por defecto | Para qué |
|---|---|---|
| `titulo` / `texto` | Switzer | Títulos y texto |
| `frase` | Bricolage Grotesque | Solo frases de Inspiración y citas de Espejo |
| `mano` | Caveat | Solo acentos: "Paso #01", una nota, "deslizá". Nunca un párrafo |
| `marca` | Poppins | Firma, botón, stickers |

## Lo que no se hace

- Mezclar paletas en una misma publicación
- Más de una lámina de golpe, o más claras que de base
- Fotos de fondo a toda la lámina con velo oscuro, inclinadas, en círculo o teñidas
- Más de un resaltado fuerte por lámina (sticker + marcador + barra juntos)
- Fotos de stock que muestren otro negocio o algo que no es tuyo
- Capturas de mensajes o reseñas sin permiso, o inventadas
- Cambiar colores o el logo en el `index.html` o en `base.css`: se cambia `marca.json`
