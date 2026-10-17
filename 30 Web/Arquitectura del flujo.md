---
tipo: web
fecha_revision: 2026-10-03
---

# Arquitectura del flujo

Cómo viaja la información desde que Agus la tiene hasta que un cliente la ve en la web.

```
ChatGPT (información acumulada)
   │  exportar conversaciones o pegar prompts
   ▼
Claude Code en el vault  ── /procesar-bandeja ──►  Obsidian (ordenado, con fuente y evidencia)
                                                         │
                                           GitHub (respaldo y versiones del vault)
                                                         │
                                    Proceso de publicación (automático)
                                    · toma solo notas con estado: activo
                                    · genera datos del mapa, catálogo y fichas
                                    · genera el índice de búsqueda
                                                         │
                                                         ▼
Web ── el suscriptor pregunta ──► API de Claude + índice ──► respuesta con fuente y nivel
   │
   └── búsquedas sin respuesta ──► vuelven al vault como preguntas abiertas
```

## Por qué así
- **Claude Code** es la herramienta de trabajo de Agus: ordena y actualiza el vault desde su computadora.
- **La web no usa Claude Code** para responder: llama a la **API de Claude** con un índice de notas publicadas. Claude Code no está pensado para atender a muchos usuarios a la vez, y darle a cualquier visitante un agente con acceso a archivos es inseguro (alguien podría intentar manipularlo).
- **Filtro de publicación**: los borradores nunca llegan a un cliente que paga.
- **Ciclo de mejora**: lo que los clientes buscan y no encuentran le dice al sistema qué investigar.

## Importar desde ChatGPT
Lo más eficiente es exportar todo de una vez (ChatGPT → Configuración → Controles de datos → Exportar), dejar el archivo en `13 Bandeja de entrada/` y pedir `/procesar-bandeja`. Claude lista las conversaciones y Agus elige cuáles importar.

Ver también: [[Especificación web]] · [[Hoja de ruta web]] · [[Decisiones]].
