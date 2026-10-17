---
tipo: negocio
fecha_creacion: 2026-10-06
fecha_revision: 2026-10-06
relacionados:
  - "[[Modelo Nutrición Evolutiva]]"
  - "[[Método de trabajo]]"
  - "[[Claims permitidos]]"
---

# Dirección creativa

> Cómo creamos anuncios, ángulos, guiones y miniaturas para que **cada peso invertido esté medido y se use con inteligencia**. Claude actúa como director creativo; Agus decide, graba y aprueba. Skill: `/crear-campana`.

## Las 5 reglas
1. **El anuncio nunca promete más que la ficha.** Todo sale de la nota de `08 Productos/` y pasa `/revisar-cumplimiento`.
2. **Un producto, muchos ángulos.** No se busca "el anuncio perfecto": se prueban ángulos y gana el dato.
3. **Cada anuncio aterriza en su landing.** El titular de la landing repite la promesa del anuncio (*message match*). Destino: `/producto/<slug>?angulo=<id>`.
4. **Todo lleva nombre y UTM.** Sin nombre ni UTM no se publica: si no se mide, no se aprende.
5. **Se decide con reglas, no con ganas.** Las reglas de corte y escala están escritas abajo y se definen antes de gastar.

## Los 8 ángulos de venta
Para cada producto se eligen 3 o 4 ángulos para la primera prueba.

| # | Ángulo | La idea | Ejemplo (lentes) | Cuidado |
|---|---|---|---|---|
| 1 | **Situación** | Una escena cotidiana que el cliente reconoce | "Son las 23 h y seguís con el celular en la cama" | Describir la situación, no diagnosticar |
| 2 | **Mecanismo** | Explicar el porqué biológico en simple | "Tu cerebro lee la hora con la luz" | Solo mecanismos con nota y nivel |
| 3 | **Te ahorramos el trabajo** | Curaduría: buscamos, filtramos y verificamos por vos | "Leímos la evidencia para que no tengas que hacerlo" | El diferencial de la marca |
| 4 | **Origen y trazabilidad** | De dónde viene, quién lo produce, cómo llega | "Huevos de [productor] de Maldonado, a tu puerta el martes" | Solo datos verificados del proveedor |
| 5 | **Honestidad** | Lo que el producto hace y lo que no | "No te van a curar el insomnio. Esto sí hacen" | Muy potente; coherente con la marca |
| 6 | **Caso 0** | Agus cuenta lo que hizo y lo que notó | "Probé esto 3 semanas. Esto noté" | Experiencia personal (E), nunca resultado garantizado |
| 7 | **Contraste** | Contra el enemigo común: ultraprocesados, marketing sin evidencia | "La mayoría de las etiquetas prometen. Nosotros mostramos la fuente" | Sin nombrar marcas de terceros |
| 8 | **Local y personal** | Reparto propio y atención humana | "Lo pedís por WhatsApp y te lo llevamos en Maldonado y Punta del Este" | Funciona muy bien en campañas locales |

## Formatos
| Formato | Duración | Para qué | Quién lo produce |
|---|---|---|---|
| Reel / video vertical | 15–30 s | Probar hooks y ángulos | Agus graba con el celular; guion de Claude |
| Cara a cámara (Agus) | 30–60 s | Caso 0, honestidad, mecanismo | Agus |
| Carrusel | 5–7 placas | Mecanismo y educación | Diseñadora; texto de Claude |
| Estático | 1 imagen | Oferta, local, recordatorio | Diseñadora; brief de Claude |
| Miniatura / portada | n/a | Que frenen el scroll | Diseñadora; brief de Claude |

## Estructura de guion (15–30 s)
```
0–3 s   HOOK        Frena el scroll: pregunta, escena o dato. Texto en pantalla.
3–10 s  PROBLEMA    La situación que el cliente reconoce.
10–18 s MECANISMO   El porqué biológico, en una frase simple.
18–25 s SOLUCIÓN    Hábito primero; el producto como herramienta.
25–30 s CTA         "Pedilo por WhatsApp" / "Hacé el test gratis".
```
Por cada guion se escriben **3 hooks alternativos**: se graba el cuerpo una vez y se cambian solo los primeros 3 segundos. Así se prueban tres anuncios por el costo de grabar uno.

## Miniaturas y estáticos
- Una sola idea por pieza; **máximo 5 palabras** en grande.
- Contraste alto; producto o cara en primer plano.
- Sello de evidencia (A–F) visible: es la marca.
- Paleta y tipografías de la web (verde profundo, crema, ámbar; Petrona y Figtree).
- Claude entrega el brief (texto, jerarquía, composición y referencia) y la diseñadora lo produce en Canva o Figma.

## Nombres y UTM
**Nombre de cada anuncio:** `PRODUCTO_ANGULO_FORMATO_HOOK_V#`, por ejemplo `LENTES_SITUACION_REEL_H2_V1`.

**URL de destino:**
```
https://<dominio>/producto/<slug>?angulo=<angulo>&utm_source=meta&utm_medium=paid&utm_campaign=<producto>_<fecha>&utm_content=<nombre del anuncio>
```

## Embudo y métricas
| Etapa | Métrica | Qué dice |
|---|---|---|
| Atención | **Hook rate** (vistas de 3 s / impresiones) | Si el inicio frena el scroll |
| Interés | **CTR** (clics / impresiones) | Si el ángulo interesa |
| Intención | **Costo por clic a WhatsApp** y **costo por test completo** | Si la landing convence |
| Venta | **Costo por venta** (ventas cargadas en el panel) | Si el negocio cierra |
| Valor | **Recompra y valor por cliente** | Cuánto se puede pagar por cliente |

Las ventas se cierran por WhatsApp. Por eso **cada venta se carga en el panel con el anuncio de origen**: así se cierra el círculo entre el peso invertido y la venta.

## Reglas de presupuesto
> Valores iniciales a calibrar con los datos de las primeras 2 semanas. Se anotan en *Aprendizajes*.

1. **Fase de prueba:** 3–4 ángulos × 3 hooks, el mismo presupuesto diario chico para cada uno, durante 3 a 5 días, segmentado a Maldonado y Punta del Este.
2. **Cortar** un anuncio cuando, con impresiones suficientes, queda en el tercio peor de hook rate y de CTR del grupo, o cuando su costo por clic a WhatsApp supera en 2 veces el promedio.
3. **Escalar** a los ganadores de a poco (+20–30 % cada 2–3 días) mientras el costo por venta se mantenga.
4. **Reparto del presupuesto:** 70 % a ganadores, 20 % a variaciones de ganadores (nuevo hook o formato), 10 % a ángulos nuevos.
5. **Reciclar:** un ángulo ganador se lleva a todos los formatos (reel → carrusel → estático → WhatsApp).

## El ciclo creativo semanal
Encaja en el paso 5 del [[Método de trabajo]]:
1. **Lunes:** Claude lee los resultados de la semana (Agus exporta el reporte de Meta y lo pega), aplica las reglas y propone qué cortar, qué escalar y qué probar.
2. **Martes:** `/crear-campana` arma los ángulos, guiones, hooks y briefs de miniatura, ya revisados contra los claims.
3. **Miércoles:** Agus graba (un bloque de 1 hora alcanza para 3–4 guiones) y la diseñadora hace los estáticos.
4. **Jueves:** se publica con nombres y UTM.
5. **Siempre:** lo aprendido se anota abajo.

## Aprendizajes
*Biblioteca viva: qué ángulos, hooks y formatos ganan. Una línea por aprendizaje, con fecha y dato.*

| Fecha | Producto | Aprendizaje | Dato |
|---|---|---|---|

Campañas: notas en `10 Contenido/` creadas con la plantilla `Campaña`.
