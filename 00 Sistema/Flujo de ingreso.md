---
tipo: sistema
fecha_revision: 2026-10-03
---

# Flujo de ingreso

Cómo una información nueva encuentra su **lugar preciso** en el sistema.

## Paso 0: capturar

Cualquier cosa nueva (un paper, un video, una idea, una charla) entra primero a `13 Bandeja de entrada/` con la plantilla **Entrada**. No hace falta clasificarla al capturarla. Después, pedile a Claude: *"procesá la bandeja"*.

**Desde Instagram:** los posts que Agus se manda al chat con @nutricionancestral.uy entran en lote con `/importar-instagram`. Ver [[Importar desde Instagram]].

## Paso 1: analizar

1. ¿Qué afirma? (una oración)
2. ¿Cuál es la fuente? ¿Qué tipo de fuente es?
3. ¿Qué nivel de evidencia tiene? → [[Niveles de evidencia]]
4. ¿Es realmente nueva o ya está en el sistema?

## Paso 2: ubicar

```
Nueva información
       ↓
Pilar → Subpilar → Concepto existente
       ↓
¿Es propiedad del concepto? ¿mecanismo? ¿evidencia? ¿intervención?
¿protocolo? ¿fuente? ¿hipótesis? ¿pregunta?
       ↓
¿Confirma? ¿Amplía? ¿Matiza? ¿Contradice? ¿Reemplaza? ¿Es nuevo?
```

**Buscá antes de crear.** Si hay una nota donde la información encaja, se actualiza esa nota. Si no existe un lugar adecuado:

```
NUEVO NODO → plantilla del tipo → asignar pilar(es) → enlazar con lo relevante → aparece en el MOC del pilar
```

## Paso 3: integrar

| Si la información… | Entonces |
|---|---|
| **Confirma** | Agregar la fuente a `fuentes`, subir el nivel de evidencia si corresponde |
| **Amplía** | Agregar al cuerpo de la sección que corresponda, con su fuente |
| **Matiza** | Agregar a *Qué NO sabemos* o *Debate* |
| **Contradice** | `## Debate / evidencia contradictoria` + **CONFLICTO DE EVIDENCIA** |
| **Reemplaza** | Actualizar y conservar la versión anterior en `## Historial` con fecha y motivo |
| **Es nuevo** | Crear nodo con plantilla |

## Paso 4: propagar

- ¿Cambia algún **protocolo** enlazado? → revisarlo.
- ¿Afecta algún **producto** o **contenido**? → revisarlo, sobre todo si la evidencia bajó.
- ¿Deja **preguntas abiertas**? → crear nota en `12 Preguntas abiertas/`.

## Paso 5: registrar

- `fecha_revision` = hoy en cada nota tocada.
- Línea en [[Registro de cambios]].
- La entrada de la bandeja pasa a `estado: procesada`, enlaza las notas afectadas y **se mueve a `99 Archivo/Bandeja/`**, para que en la bandeja quede solo lo pendiente.

> Claude ejecuta todo este flujo con la skill `/procesar-bandeja`.

## Las 12 preguntas de control

1. ¿Qué afirma? 2. ¿Cuál es la fuente? 3. ¿Qué tipo de fuente es? 4. ¿Qué nivel de evidencia tiene? 5. ¿Es realmente nueva? 6. ¿Qué conceptos existentes modifica? 7. ¿Contradice algo? 8. ¿Confirma algo? 9. ¿Qué notas deben actualizarse? 10. ¿Qué relaciones nuevas aparecen? 11. ¿Qué protocolos podrían cambiar? 12. ¿Qué contenido comercial queda afectado?

Volver a [[Inicio]].
