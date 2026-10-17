---
name: historias
description: Arma un recorrido de historias de Instagram de la marca (3 a 7 historias con principio y final, la mayoría juegos, con el lugar para cada sticker) a partir de la sección Historias del plan mensual, con el mismo estilo de los carruseles, y lo exporta a PNG 1080x1920 con su Publicar.md. Usar cuando se pida hacer historias, stories, un recorrido o un juego de historias, o producir las historias de la semana o del mes.
---

# Historias

**Módulo opcional.** Si `Empresa/Marca/marca.json` → `modulos.historias` es `false`, avisar que está
desactivado y preguntar si se quiere activar (→ `/configurar-marca`, bloque 6) antes de seguir.

**La marca manda:** antes de producir, leer `Empresa/Marca/Manual de marca.md`. Si esta skill y el
manual dicen distinto, vale el manual.

Produce **una carpeta por recorrido**: `Áreas/Contenido/outputs/aaaa-mm/historias/NN-tema/`, donde **NN
es el número de la fila en la sección 4 · Historias del plan del mes**. Adentro: `index.html` (la
fuente), `historia-01.png`, `historia-02.png`… (lo que se sube) y `Publicar.md` (qué sticker va en
cada una y cuándo se sube).

## 0. Leer antes

1. `Áreas/Contenido/Plan mensual/aaaa-mm.md`, sección **4 · Historias**: la fila que se produce
2. `Áreas/Contenido/Templates/Recorridos de historias.md`: **dónde va cada cosa, qué sticker para qué,
   los juegos**. Si la fila no dice qué juego, proponer uno que no se haya hecho en las últimas semanas
3. `Áreas/Contenido/Templates/Estilo de carrusel.md`: el estilo, las paletas y las tres reglas
4. `Empresa/Marca/Tono de voz.md` y, si hay precio, `Empresa/Catálogo.md` (**se verifica cada uno**)
5. `Empresa/Conocimiento/` para todo juego o quiz con respuesta técnica: **el dato sale de ahí, con su
   fuente**, y si no está no se afirma. La sección *Para contenido* de cada tema es fuente de preguntas
6. `Empresa/Marca/marca.json`: `cuenta`, `descriptor`, paletas

## 1. Elegir el recorrido y decirlo antes de diseñar

```
Recorrido: Juego · Mito o realidad (la fila pide algo de errores comunes)
Paleta: noche (las últimas historias fueron principal)
Historias: 1 foto + anuncio · 2 ronda 1 (encuesta) · 3 respuesta · 4 ronda 2 (quiz) · 5 respuesta + deslizador
Respuestas: de Conocimiento/Técnica básica.md · Para confirmar con: {{quién}}
```

## 2. Armar

1. Copiar la muestra de `Áreas/Contenido/Templates/Muestrario historias/01-juego-mito-o-realidad/` a la
   carpeta nueva; **cambiar la ruta del CSS** a `../../../../../../.claude/skills/carrusel/base.css`
   (desde `outputs/aaaa-mm/historias/NN-tema/` hay seis niveles hasta la raíz) y la paleta en `<body>`
2. La firma: `cuenta` y `descriptor` de `marca.json`
3. Una `<section class="slide historia">` por historia. Las variantes son las del carrusel: `clara`,
   `golpe` (la del CTA o el cierre), `foto-mitad`, `mano`, `pasos`, `check`, `cifra`, `sticker`…
4. **Donde va un sticker de Instagram, un `<div class="hueco">`** (`chico`, `grande`) con lo que va
   adentro escrito. Se ve punteado al abrir el `index.html` y sale vacío en la PNG: el sticker se pone
   en la app al subir
5. Variar contra el recorrido anterior: otra paleta, otros elementos

## 3. Exportar y revisar

```
python .claude/skills/carrusel/render.py Áreas/Contenido/outputs/aaaa-mm/historias/NN-tema
```

Detecta que son historias y deja `historia-01.png`… de 1080 × 1920. Mirarlas una por una:

- [ ] Nada importante arriba de 250 px ni abajo de 1580 px (lo tapa la app)
- [ ] **La 1 tiene algo real** (cara, mano, lugar, producto) a media pantalla
- [ ] **El sticker entre la 2 y la 4**, nunca solo en la última; en un juego, uno por ronda
- [ ] Un solo CTA (o ninguno, si es un juego). Máximo 7 historias
- [ ] Toda respuesta técnica, de `Conocimiento/` y confirmada (si no, a `Plan.md` y no se publica)
- [ ] Una sola paleta, un logo por historia
- [ ] Se entiende cada una en 3 segundos: poco texto, letra grande
- [ ] Ni un `—`, nada de lo prohibido, ningún precio sin verificar

## 4. El Publicar.md y al terminar

1. `Publicar.md` en la carpeta, con la tabla de la muestra: **#, cuándo se sube, imagen, qué se pone en
   la app (sticker exacto, opciones, la correcta, texto del enlace), para qué**. Más música y destacada
2. **Recordar en el Publicar.md: a quien contesta un sticker se le escribe por mensaje** ese mismo día
3. En el plan del mes, en la fila: la ruta de la carpeta y el estado a **Producida**
4. Si un juego funcionó (muchas respuestas), anotarlo en el banco de ideas, sección 12
