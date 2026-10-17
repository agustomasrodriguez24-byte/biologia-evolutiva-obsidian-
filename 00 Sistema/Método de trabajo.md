---
tipo: sistema
fecha_creacion: 2026-10-06
fecha_revision: 2026-10-06
relacionados:
  - "[[Modelo Nutrición Evolutiva]]"
  - "[[Flujo de ingreso]]"
  - "[[Criterios de la tienda]]"
---

# Método de trabajo

> Cómo construimos Nutrición Evolutiva: ordenado, sin dispersarnos y con Agus viviendo el sistema mientras lo construye. Filosofía y principios: [[Modelo Nutrición Evolutiva]].

## La regla de oro: un órgano por semana, de punta a punta
No se construye "todo el conocimiento" y después "toda la tienda". Cada semana un órgano recorre la cadena completa y sale terminado:

```
ÓRGANO → LEGOS (lo que necesita) → ALIMENTOS que los aportan → TIPS (hábitos)
       → PRODUCTOS alineados → FICHA DE VALOR → WEB + TEST + CONTENIDO
       + Agus prueba el tip en su vida (caso 0)
```

**Por qué así:** cada semana termina algo publicable y vendible; los errores de la cadena aparecen enseguida, no al final; y el mapa del cuerpo, el catálogo y el test crecen juntos y alineados.

> Si la semana no alcanza, el ciclo dura dos semanas. El orden no cambia. Mejor un órgano terminado que tres a medias.

## El ciclo semanal

| Bloque | Qué se hace | Quién | Herramienta |
|---|---|---|---|
| **1. Investigar** | Nota del órgano: función, legos (materiales, señales, condiciones, regulación), mecanismos, qué no sabemos. Se suma lo que Agus ya sabe (su marco) como entrada a la bandeja | Claude arma, Agus aporta | `/retomar conocimiento`, `/procesar-bandeja` |
| **2. Revisar** | Agus lee, corrige y aprueba. Lo aprobado pasa a `activo` | Agus decide | Obsidian |
| **3. Alimentos** | Los alimentos que mejor aportan los legos del órgano se evalúan con la matriz. Se anotan los proveedores posibles en Uruguay | Claude evalúa, Agus elige proveedor | `/evaluar-alimento` |
| **4. Tips y productos** | Tips desde intervenciones y protocolos. Los productos candidatos pasan el filtro y reciben su ficha de valor. Todo texto pasa el control de claims | Claude propone, Agus aprueba | `/evaluar-producto`, `/revisar-cumplimiento` |
| **5. Publicar y anunciar** | El órgano entra a la web (catálogo, test, mapa). Sus productos reciben campaña: ángulos, guiones y miniaturas ([[Dirección creativa]]). Se deja todo anotado | Claude ejecuta, Agus graba y aprueba | `/crear-campana`, `/generar-contenido`, `/cerrar-sesion` |
| **En paralelo** | Agus aplica 1 tip del órgano en su vida durante 2 a 4 semanas y lo registra | Agus vive, Claude ordena | Nota en `09 Experimentos/` |

### Un órgano está terminado cuando…
- [ ] Su nota en `16 Órganos/` está `activo`, con fuentes en cada lego.
- [ ] Cada lego enlaza a su nota (nutriente, concepto o intervención), con su nivel A–F.
- [ ] Hay al menos 2 alimentos evaluados que aportan sus legos principales.
- [ ] Hay al menos 3 tips publicables (nivel A–C, con nota de respaldo).
- [ ] Los productos alineados tienen ficha de valor y pasaron `/revisar-cumplimiento`.
- [ ] El órgano y sus objetivos están en el test y en la web.
- [ ] Hay 1 experimento de Agus en curso o terminado.

## Agus, caso 0
Agus es la primera persona que vive el sistema. Cada tip que se publica, Agus lo prueba antes.
- **Para qué:** detectar qué es aplicable de verdad, generar contenido propio y auténtico ("esto hice yo y esto noté"), y encontrar fricciones antes que los clientes.
- **Cómo:** una nota en `09 Experimentos/` por tip, con la plantilla Experimento: qué hice, cuánto tiempo, qué medí y qué noté.
- **Límite:** un n=1 es nivel E. Se cuenta como experiencia personal, nunca como prueba.

## Ritmo
| Frecuencia | Qué | Tiempo |
|---|---|---|
| **Diario** | Capturar ideas, links y preguntas en `13 Bandeja de entrada/` sin ordenarlas (desde el celular con Obsidian). Registrar el experimento en curso | 5–10 min |
| **Por sesión** | Un chat = una tarea. Arrancar con `/retomar <área>` y cerrar con `/cerrar-sesion` | 60–90 min |
| **Semanal** | El ciclo del órgano (arriba). Al empezar la semana se elige el órgano; al terminar se marca como hecho | 3–5 sesiones |
| **Mensual** | `/auditar`: huecos, decisiones pendientes, métricas del mes y elección de los órganos del mes siguiente | 1 sesión |

**Límites para no dispersarse:** un solo órgano abierto a la vez · máximo 3 tareas en curso · las ideas nuevas van a la bandeja, no a la sesión actual.

## Roles
| Agus | Claude |
|---|---|
| Decide (todo lo que entra a `activo` y cada decisión de [[Decisiones]]) | Investiga, estructura y redacta con fuentes |
| Aporta su marco, su experiencia y su criterio | Marca el nivel de evidencia y los huecos |
| Vive los tips (caso 0) | Controla los claims antes de publicar |
| Elige proveedores, vende y atiende por WhatsApp | Programa la web, el test y el panel |
| Consigue validación profesional (nutricionista, legal) | Mantiene el vault ordenado y los Estados al día |

## Semáforo de publicación
```
borrador ──► revisión de Agus ──► /revisar-cumplimiento ──► activo ──► web
```
Nada llega a un cliente sin pasar los cuatro pasos.

## Fases hasta el lanzamiento

### Fase 0: cimientos (2 semanas)
- [x] Plantilla de órgano y reglas (`16 Órganos/`).
- [ ] Pasar el marco de ChatGPT al vault (exportar → bandeja → `/procesar-bandeja`).
- [ ] Definir la lista única de objetivos del cliente (sale de los órganos).
- [ ] Contactar a un nutricionista (validar el test) y a un asesor legal (Ley 18.331 y claims).
- [ ] Crear las cuentas de Supabase y Vercel; cargar el número de WhatsApp en la web.

### Fase 1: mapa y núcleo (un órgano por semana)
Orden sugerido. Empieza por donde ya hay base en el vault:
1. **Ojos y cerebro** (ritmo circadiano y sueño: ya hay notas).
2. **Músculos** (proteína y movimiento).
3. **Hígado** (colina, huevo).
4. **Intestino** (digestión y microbiota).
5. **Corazón y vasos** (sodio, movimiento).
6. **Riñones** (agua y electrolitos).
7. Los que surjan del marco de Agus.

### Fase 2: lanzamiento local (Maldonado y Punta del Este)
- Catálogo inicial de 8 a 12 alimentos del núcleo `activo`.
- Test v1 con los objetivos de los órganos terminados.
- Web publicada, mensajes de WhatsApp y logística mínima.
- Primeros 20 a 50 clientes: escuchar, ajustar y medir la recompra.

### Fase 3: crecer
Contenido semanal desde el vault, blog, mapa del cuerpo interactivo, carrito y pagos, buscador por suscripción y nuevas zonas de reparto.

## Cómo medimos si funciona
| Qué | Métrica |
|---|---|
| Avance del sistema | Órganos terminados · alimentos del núcleo `activo` · tips publicables |
| Valor entregado | Personas que hacen el test · personas que dejan su contacto |
| Negocio | Pedidos por semana · tasa de recompra · ticket promedio |
| Caso 0 | Experimentos terminados · tips que Agus sostiene en el tiempo |

Volver a [[Inicio]].
