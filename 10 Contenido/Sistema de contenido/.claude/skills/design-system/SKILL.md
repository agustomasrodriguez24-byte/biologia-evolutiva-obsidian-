---
name: design-system
description: El sistema de diseño de las piezas de redes — cómo se definen y cambian las paletas, el logo y las letras de la marca en marca.json, cómo se chequea el contraste y cómo se aplica a carruseles, historias, portadas y videos. Usar cuando se pida definir, cambiar o revisar colores, paletas, logo, tipografía o el estilo visual, o antes de diseñar algo fuera de las plantillas.
---

# Design system

**Una sola fuente:** `Empresa/Marca/marca.json`. De ahí salen los colores, el logo y las letras de
todo lo que se diseña. `aplicar-marca.py` lo convierte en `.claude/skills/carrusel/marca.css` (que usan
carruseles, historias y portadas) y `video.py` lo lee directo.

```
marca.json ──aplicar-marca.py──▶ carrusel/marca.css ──▶ base.css ──▶ carruseles, historias, portadas
     └────────────────────────────────────────────────▶ video.py  ──▶ ganchos, gráficos, subtítulos
```

**Nunca se cambia un color en `base.css`, en `marca.css` ni en un `index.html`.** Se cambia
`marca.json` y se corre:

```
python Áreas/Contenido/herramientas/aplicar-marca.py
```

La marca en palabras (qué es, cuándo va cada paleta, qué fotos sí) está en
`Empresa/Marca/Manual de marca.md`, sección 5. Cómo se ve cada elemento →
`Áreas/Contenido/Templates/Estilo de carrusel.md`.

---

## El estilo, en una línea

**Plano, una familia de color por pieza, títulos enormes, una sola lámina de golpe.** Es lo que hace que
las piezas se reconozcan en el feed sin leer el nombre. Lo que cambia entre marcas son los colores, el
logo y las letras; la estructura (base, clara, golpe; la firma; las tres formas de foto) queda igual.

## Las paletas

Cada paleta tiene tres láminas y ocho colores:

| Campo | Qué es | Regla |
|---|---|---|
| `base` | Fondo de la mayoría de las láminas | El color más reconocible de la marca, en su versión profunda |
| `tinta_base` | Texto sobre la base | Blanco o casi negro, el que dé más contraste |
| `acento` | La palabra en color, stickers, marcador | El color más vivo de la familia. **Contraste con `base` de 3:1 como mínimo** |
| `clara` | Fondo de las láminas claras | Casi blanco, teñido de la familia |
| `tinta_clara` | Texto sobre la clara | Normalmente, el color de `base` |
| `acento_clara` | Acento sobre la clara | Una versión más oscura del acento (el acento vivo no se lee sobre claro) |
| `golpe` | Fondo de la lámina que más importa | Normalmente, el mismo `acento` |
| `tinta_golpe` | Texto sobre el golpe | Normalmente, el color de `base` |

**Cuatro paletas** alcanzan: una de todos los días, una para alternar, una clara, una oscura e íntima.
Los nombres se eligen libres (`principal`, `bosque`, `arena`…): son los que se escriben en
`<body class="paleta-NOMBRE">` y en el `"paleta"` del `edl.json`. `paleta_por_defecto` dice cuál va
si no se elige.

**Cómo se arma desde los colores de la marca:**

1. Tomar el color principal (del logo o la web) y bajarle la luminosidad hasta que el blanco se lea
   encima con 7:1: esa es la `base` de la paleta principal
2. El `acento`: el segundo color de la marca, o el principal más vivo. Si no hay segundo color, uno
   complementario de la misma temperatura
3. La `clara`: la base al 5-8 % sobre blanco
4. Las otras paletas: un tono vecino (alterna), la versión clara (base clara, golpe oscuro) y una
   noche (casi negro + un color que solo vive ahí)

**Chequear el contraste:** `aplicar-marca.py` lo hace solo y marca `MAL` cada par que no llega
(texto sobre fondo 4,5:1, acento sobre fondo 3:1). Se ajusta el color en `marca.json` y se vuelve a
correr hasta que diga *OK en todas las paletas*.

## El logo

Dos PNG con fondo transparente en `Empresa/Marca/logos/`:

- `logo-fondo-oscuro.png`: el que se lee sobre oscuro (normalmente, blanco o en negativo)
- `logo-fondo-claro.png`: el que se lee sobre claro (normalmente, a color o negro)

El sistema elige cuál va en cada lámina según la luminosidad del fondo. En la lámina de golpe, el logo
va sobre una pastilla blanca. **Recortados sin aire alrededor** (si no, salen chicos en la firma).
Mientras exista `BORRAR-ESTO-al-poner-los-logos-reales.txt`, `aplicar-marca.py` avisa que son de ejemplo.

## Las letras

Seis roles en `marca.json` → `fuentes`: `titulo`, `texto`, `marca`, `mano`, `frase`, `serif`. El kit
que trae el sistema (Switzer, Poppins, Caveat, Bricolage Grotesque, Instrument Serif, Questrial) está
en `Áreas/Contenido/herramientas/fuentes/`, sin internet.

### Cambiar una letra (carruseles e historias)

1. Bajar la letra en `.woff2` (Google Fonts o la fuente de la marca, **con licencia que permita uso
   comercial**) a `herramientas/fuentes/`, con su licencia al lado
2. Sumar su `@font-face` en `herramientas/fuentes/fuentes.css` (familia, peso, archivo)
3. Poner el nombre de la familia en el rol de `marca.json` → `fuentes`
4. `aplicar-marca.py` y exportar el muestrario para ver que no se corta ningún título (las letras
   anchas necesitan bajar el tamaño de `h1.xl` en `base.css`)

### Cambiar la letra del video

`video.py` usa la familia `Switzer` (y el `Switzer-Extrabold.ttf` para los subtítulos) y `Poppins`.
Para otra letra: reemplazar en `video.py` las referencias `Switzer` por la familia nueva en los
`@font-face` y en el estilo de subtítulos (`Style: Sub` y `Style: Dest`, que usan el nombre interno
del `.ttf`), y poner el `.ttf` en `fuentes/`. Probar con `video.py armar --vista-previa 5` antes de
dar por bueno.

## Las fotos

Tres formas, nada más: media lámina (`.foto-mitad`), redondeada (`.foto-redonda`), con marco de color y
etiqueta (`.foto-marco-color`). **Fotos reales** de `Áreas/Contenido/Material/Fotos/`. Si una foto es
HEIC, se convierte una vez a JPG al lado del original y se usa esa.

## Antes de diseñar algo fuera de las plantillas

(Una placa para un anuncio, una portada distinta, una pieza para imprimir.) Partir de `base.css` igual:
crear el HTML con `<link rel="stylesheet" href=".../carrusel/base.css">`, una `<section class="slide">`
y las mismas clases. Si no alcanza, sumar el estilo en un `<style>` en ese mismo archivo usando las
variables (`var(--fondo)`, `var(--tinta)`, `var(--acento)`, `var(--f-titulo)`), nunca colores fijos.

## Checklist del design system

- [ ] `aplicar-marca.py` corre sin avisos de logo
- [ ] `aplicar-marca.py` dice *OK en todas las paletas*
- [ ] El muestrario exportado se ve bien en las cuatro paletas (cambiar la clase del `<body>` para verlas)
- [ ] La sección 5 del Manual de marca dice cuándo va cada paleta
