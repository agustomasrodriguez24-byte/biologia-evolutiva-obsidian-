# Crudos

Los datos tal como salen de la fuente, con el nombre `aaaa-mm-<fuente>.<ext>`:

- `aaaa-mm-instagram.csv`: Meta Business Suite → Estadísticas → Contenido → últimos 90 días →
  Exportar. Lo lee `Áreas/Contenido/herramientas/analizar-instagram.py`
- `aaaa-mm-instagram.json`: solo si se conecta la API con un script propio

No se editan a mano. Se acumulan: el del mes pasado sirve para comparar.
