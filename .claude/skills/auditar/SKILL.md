---
name: auditar
description: Detecta huecos y problemas en el proyecto Nutrición Evolutiva (conocimiento, negocio y web) y entrega prioridades. Usar cuando el usuario dice "auditá el sistema", "qué falta", "dónde hay huecos" o pide revisar el estado general.
---

# Auditar

Si Agus nombra un área, auditá solo esa. Si no, las tres, en este orden.

## Conocimiento
Con grep y lectura de propiedades (sin abrir notas completas salvo que haga falta), buscá:
- conceptos, mecanismos, intervenciones y protocolos con `fuentes: []`;
- fuentes sin backlinks;
- posibles duplicados (títulos o sinónimos parecidos);
- protocolos con `nivel_evidencia` C, D, E o F, o vacío;
- productos sin `necesidad` o sin `alineacion`;
- notas con `fecha_revision` de más de 180 días o `estado: revisar`;
- preguntas abiertas por prioridad;
- pilares vacíos (`01 Pilares/`) y pilares con muchas notas y evidencia débil;
- entradas pendientes en la bandeja.

## Orden del vault
- Archivos sueltos en la raíz o en carpetas que no corresponden a su `tipo`.
- Notas sin `tipo`.
- Documentos duplicados o casi iguales (títulos y contenido parecidos).
Proponé dónde mover cada uno y movelo solo con la aprobación de Agus.

## Negocio, web y operación
- Ítems *a completar* en `20 Negocio/Visión y objetivos.md`.
- Decisiones **pendientes** en `20 Negocio/Decisiones.md`.
- Riesgos pendientes en `20 Negocio/Riesgos y cumplimiento.md`.
- Ítems sin construir de la versión actual en `30 Web/Especificación web.md` y `30 Web/Hoja de ruta web.md`.
- Temas *pendientes* en `40 Operación/Logística.md` y `40 Operación/Ventas y clientes.md`.

## Entrega
1. Una tabla por área: problema · notas afectadas · acción sugerida.
2. **Prioridades**: las 5 más importantes, ordenadas por impacto, incertidumbre, importancia en el sistema, aplicabilidad y necesidad de actualización.
3. Actualizá la sección *Huecos conocidos* de cada nota de Estado auditada.
