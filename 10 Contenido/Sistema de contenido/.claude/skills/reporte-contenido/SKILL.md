---
name: reporte-contenido
description: Escribe el reporte mensual de contenido — qué se publicó contra lo planificado, cómo rindió cada pieza (alcance, múltiplo, guardados, compartidos, consultas), qué funcionó por pilar, audiencia, formato y fórmula de gancho, y las tres decisiones para el mes siguiente. Usar el primer día del mes, al cerrar un mes, o cuando se pregunte cómo rindió el contenido.
---

# Reporte de contenido

Produce **un** archivo: `Áreas/Contenido/Reportes/aaaa-mm-dd.md`, con la plantilla de
`Áreas/Contenido/Templates/Reporte contenido.md`. **Se hace antes de armar el mes siguiente:** sin
esto, el plan que viene se arma de memoria.

## 0. Leer antes

1. `Áreas/Contenido/Plan mensual/aaaa-mm.md` del mes que cierra: qué se iba a hacer
2. El reporte anterior en `Reportes/`, para comparar
3. `Áreas/Contenido/Inspiración/Inspiración.md`: qué piezas vinieron de una adaptación

## 1. Los números

1. Buscar el export más nuevo en `Empresa/Datos y feedback/Crudos/` (de los últimos 7 días). Si no
   hay, pedir **una sola cosa**: el export de Meta Business Suite guardado ahí
2. `python Áreas/Contenido/herramientas/analizar-instagram.py`
3. **Las consultas que trajo cada pieza** no están en Instagram: preguntar cuántos mensajes llegaron
   por redes y, si se sabe, por qué pieza. Si no se sabe, "Sin medir", y se dice

## 2. Escribir

- **Pieza por pieza:** cruzar el plan con los números. Cada pieza del plan tiene que aparecer, también
  las que no se publicaron
- **Qué no salió y por qué.** Si es siempre el mismo motivo, decirlo: es el cuello de botella
- **Qué funcionó y qué no:** por pilar, audiencia, formato, **fórmula de gancho** y **adaptadas contra
  propias**. Con menos de 5 piezas en un grupo, es anécdota y se dice
- **La regla que queda**, solo con evidencia
- **Tres decisiones** para el mes que viene, no más

**Lo que falló se escribe igual que lo que funcionó**, sin maquillar.

## 3. Al terminar

1. En el plan del mes: los estados a **Medida** y la sección *Resultado del mes*
2. Lo que tiene evidencia → `Contenido.md`, *Lo que ya sabemos*
3. Seguidores y medianas → `Empresa/Números.md`, con fecha y fuente
4. En `Inspiración/Inspiración.md`, columna *¿Rindió?* de las adaptaciones publicadas
5. Lo que no se pudo contestar → `Plan.md`
6. Decir que sigue `/investigar-contenido` y `/plan-mensual-contenido`
