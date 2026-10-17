---
name: carrusel
description: Arma un carrusel de Instagram (o LinkedIn) de la marca a partir de una pieza del plan mensual o de una adaptación de inspiración, eligiendo el tipo de carrusel según su pilar, audiencia y contenido, y lo exporta a PNG 1080x1350. Usar cuando se pida hacer, diseñar o producir un carrusel, o producir las piezas de carrusel del mes.
---

# Carrusel

**La marca manda:** antes de producir, leer `Empresa/Marca/Manual de marca.md`. Si esta skill y el
manual dicen distinto, vale el manual y se corrige la skill.

Produce **una carpeta por carrusel**: `Áreas/Contenido/outputs/aaaa-mm/carruseles/NN-tema/`, donde **NN
es el número de la pieza en el plan del mes** (Pieza 3 → `03-tema`). Adentro: `index.html` (la fuente,
editable), `slide-01.png`, `slide-02.png`… (lo que se sube) y `Publicar.md`.

---

## 0. Leer antes de diseñar

1. **La pieza** en `Áreas/Contenido/Plan mensual/aaaa-mm.md` (o la ficha de `Inspiración/` si viene de
   una adaptación): título, pilar, audiencia, gancho, láminas si ya están escritas, el pie. **El texto
   de las láminas sale de ahí**, no se reescribe
2. `Áreas/Contenido/Templates/Tipos de carrusel.md`: **los tipos y cómo se elige**
3. `Áreas/Contenido/Templates/Estilo de carrusel.md`: **cómo se ve**, las paletas, las piezas. Las
   muestras en `Templates/Muestrario carrusel/`
4. `Áreas/Contenido/Templates/Cómo se arma una pieza.md`, sección *Carrusel*
5. `Empresa/Marca/marca.json`: la `cuenta` y el `descriptor` (van en la firma), el `cta.boton`, las
   paletas que existen. Si `aplicar-marca.py` no se corrió desde el último cambio de la ficha, correrlo
6. `Empresa/Catálogo.md` si hay un precio o un requisito. **Se verifica cada uno**
7. `Empresa/Conocimiento/` si la pieza afirma algo técnico: **todo dato sale de ahí, con su fuente**,
   y si no está no se afirma

Si se pide un carrusel suelto, sin pieza en el plan: pedir audiencia, pilar y de qué trata en un solo
mensaje, y seguir igual.

## 1. Elegir el tipo, y decirlo antes de diseñar

Las tres preguntas de `Tipos de carrusel.md` (pilar → forma del contenido → acción que busca) y se
presenta, en un mensaje corto:

```
Pieza 3 · 13/10 · Audiencia 2 · Autoridad
Tipo: Comparativa: son cuatro opciones para elegir
Descarté: Lista (no son ítems del mismo peso, se elige uno) · Paso a paso (no hay orden)
Paleta: alterna (la anterior fue principal) · Elementos: foto redonda, tabla, sticker
Láminas (8): 1 portada · 2 lo que tienen en común · 3-6 una ficha por opción · 7 tabla resumen · 8 CTA
Cambios contra el plan: la lámina 7 pasa a la 2, como segundo gancho
```

**Si las láminas del plan no calzan con el esqueleto del tipo, se propone el cambio y se explica.**
No se reordena en silencio. Recién con el OK se diseña.

## 2. Armar el HTML

1. Copiar `.claude/skills/carrusel/plantilla.html` a la carpeta del carrusel como `index.html` y
   completar el comentario de arriba (tipo, paleta y pieza)
2. **La paleta va en `<body class="paleta-NOMBRE">`**, distinta a la del carrusel anterior del mes;
   una o dos láminas `.clara` (con foto) y una sola `.golpe`. **Variedad:** dos o tres elementos del
   menú *A veces* de `Estilo de carrusel.md`, sin repetir la combinación del carrusel anterior
3. **La firma:** cambiar `@tucuenta` y `Lo que hacés` por `cuenta` y `descriptor` de `marca.json`, en
   todas las láminas. En la portada, con `.deslizar`
4. Una `<section class="slide">` por lámina, con las clases del tipo elegido
5. **Fotos de tres formas:** `.foto-mitad`, `.foto-redonda` o `.foto-marco-color`, desde
   `Áreas/Contenido/Material/Fotos/` con ruta relativa, sin copiarlas (desde la carpeta del carrusel:
   `../../../../Material/Fotos/Tema/foto.jpg`). **Nunca fotos de stock que
   muestren otro negocio**. Un solo acento de color, un solo logo y fotos solo de esas tres formas
6. El CTA (`.boton.wa`) con el `cta.boton` de `marca.json`, **solo en la última**
7. Abrir el `index.html` en el navegador: se ven todas las láminas juntas, para revisar el ritmo

**Las reglas del texto son las del plan:** el trato de la marca, frases cortas, nada de guion largo
(—), un solo CTA, nada de lo prohibido → `Empresa/Marca/Tono de voz.md`.

## 3. Exportar y revisar

```
python .claude/skills/carrusel/render.py Áreas/Contenido/outputs/aaaa-mm/carruseles/NN-tema
```

Abre Chrome o Edge sin ventana y deja una PNG de 1080 × 1350 por lámina. **No necesita internet** (las
fuentes están en `Áreas/Contenido/herramientas/fuentes/`). La primera vez: `pip install playwright`
(usa el Chrome instalado).

**Mirar las PNG una por una antes de darlo por terminado.** Chequear:

- [ ] Ningún texto cortado ni pegado al borde (36px de margen mínimo)
- [ ] La portada se entiende en un segundo, a tamaño de celular
- [ ] Firma con la cuenta real en todas, "deslizá" en la portada. Sin contador
- [ ] Una sola paleta, no más de dos claras y una sola de golpe; si sobra aire, se agranda la letra
- [ ] Cada precio o requisito coincide con `Empresa/Catálogo.md`; cada dato técnico, con `Conocimiento/`
- [ ] Ni un `—` en ninguna lámina
- [ ] Un solo CTA, en la última
- [ ] Lámina resumen antes del cierre, si el tipo la lleva
- [ ] La portada: seis palabras o menos de gancho, con una fórmula de `Fórmulas de gancho.md`

Corregir en el `index.html` y volver a exportar. **No se edita la PNG.**

## 4. Al terminar

1. `Publicar.md` en la carpeta, desde `Templates/Publicar.md`: el pie (pasado por
   `python Áreas/Contenido/herramientas/revisar-texto.py <carpeta>/Publicar.md`), hashtags, música,
   texto alternativo de la portada, y lo que falta confirmar
2. En el plan del mes, en la pieza: **tipo de carrusel**, **paleta y elementos**, la ruta de la
   carpeta, y el estado de la fila a **Producida**
3. Para LinkedIn: `<body class="paleta-NOMBRE linkedin">` (numera las láminas y saca "deslizá");
   `render.py` deja además `carrusel.pdf`, que es lo que se sube
4. Si en el camino salió un dato sin confirmar → `Plan.md`
