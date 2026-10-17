---
tipo: sistema
fecha_revision: 2026-10-03
---

# Guía de propiedades

## Comunes a todas las notas de conocimiento

| Propiedad | Valores | Uso |
|---|---|---|
| `tipo` | `concepto` `mecanismo` `fuente` `intervencion` `protocolo` `metrica` `producto` `experimento` `contenido` `hipotesis` `pregunta` `entrada` `pilar` `alimento` `nutriente` `organo` `tesis` | Obligatoria. Define plantilla y carpeta |
| `pilar` | lista: `biologia` `nutricion` `hidratacion` `cronobiologia` `movimiento` `mente` `metabolica` `digestiva` `entorno` `proposito` | Hace aparecer la nota en el MOC del pilar |
| `subpilar` | texto libre (ej. `metabolismo energético`) | Agrupa dentro del pilar |
| `estado` | `borrador` `activo` `revisar` `obsoleto` | Ciclo de vida |
| `nivel_evidencia` | `A` `B` `C` `D` `E` `F` | Ver [[Niveles de evidencia]] |
| `fecha_creacion` | fecha | |
| `fecha_revision` | fecha | La auditoría marca notas de más de 180 días |
| `fuentes` | lista de enlaces a `04 Fuentes/` | La auditoría marca conceptos sin fuente |
| `relacionados` | lista de enlaces | Relaciones reales, no decorativas |

## Específicas por tipo

- **fuente**: `tipo_fuente` (`revision-sistematica` `metaanalisis` `ensayo-clinico` `observacional` `mecanistico` `animal` `guia-oficial` `institucional` `libro` `profesional` `tradicion` `experiencia` `comercial`), `autor`, `anio`, `url`, `doi`, `poblacion`.
- **protocolo**: `intervenciones`, `metricas`, `riesgo` (`bajo` `medio` `alto`).
- **intervencion**: `mecanismos`, `riesgo`.
- **metrica**: `unidad`, `como_medir`.
- **producto**: `categoria` (`alimento` `herramienta`), `estado_tienda` (`evaluando` `aprobado` `aprobado-con-condiciones` `rechazado`), `necesidad`, `alineacion` (conceptos/protocolos), `ingrediente`, `evidencia_ingrediente`, `evidencia_producto`, `nivel_promesa`, `contenido` (video de valor), `proveedor`, `url`. Ver [[Criterios de la tienda]].
- **alimento**: `grupo`, `porcion_g`, `densidad` `digestibilidad` `biodisponibilidad` `utilizacion` (1–5), `diaas`, `nutrientes_clave`, `antinutrientes`, `preparacion`, `en_nucleo` (casilla), `productos`. Ver [[Matriz de Cobertura Nutricional]].
- **nutriente**: `clase` (`macronutriente` `vitamina` `mineral` `acido-graso` `bioactivo` `otro esencial`), `ingesta_referencia`, `unidad`, `poblacion_referencia`, `estado_cobertura` (`cubierto` `parcial` `hueco` `contexto`).
- **organo**: `sistema` (ej. `nervioso` `digestivo` `musculoesqueletico` `cardiovascular` `renal`), `objetivos` (objetivos del cliente que toca), `legos` (enlaces a nutrientes, conceptos e intervenciones), `alimentos`, `productos`. Ver [[Modelo Nutrición Evolutiva]].
- **habito** (`18 Sistema de salud/`): `semana` (0–18), `etapa`, `cuerpo` (`reloj` `vegetal` `animal` `yo` `todos`), `objetivos` (los 5 del cliente: Dormir, Presión, Fuerza, Digestión, Nutrición), `organos`, `legos`, `productos`. Ver [[Sistema de salud Nutrición Evolutiva]].
- **tesis**: `referentes` (lista de nombres de los referentes que la alimentan). Ver [[Información madre]].
- **experimento**: `estado` (`planificado` `en-curso` `terminado`), `fecha_inicio`, `fecha_fin`, `metricas`.
- **contenido**: `formato` (`reel` `tiktok` `youtube` `podcast` `carrusel` `newsletter` `vsl` `curso` `guia` `campana`), `estado` (`idea` `guion` `producido` `publicado`), `conceptos`. Las campañas suman `producto`, `angulos`, `fecha_inicio` y `presupuesto_diario` (ver [[Dirección creativa]]).
- **pregunta**: `estado` (`abierta` `investigando` `resuelta`), `prioridad` (`alta` `media` `baja`).
- **entrada**: `estado` (`pendiente` `procesada` `descartada`), `origen`, `url`.

Los tipos de propiedad (lista, fecha, texto) ya están configurados en `.obsidian/types.json`.

Volver a [[Inicio]].
