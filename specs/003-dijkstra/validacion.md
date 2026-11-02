# Validación Dijkstra

Python 3.12.3. `.venv/bin/python -m pytest -q`: 58 passed, estado 0.
Oráculo NetworkX confirma coste mínimo y validez de cada recorrido, incluidos
ocho grafos generados con ciclos, bucles, pesos cero y desconexión.

## Revisión manual de CLI por el agente

`.venv/bin/python -m graph_lab shortest tests/data/weighted.csv a`
Estado 0; stderr vacío.
```json
{"distances": {"a": 0, "b": 3, "c": 1, "z": null}, "paths": {"a": ["a"], "b": ["a", "c", "b"], "c": ["a", "c"], "z": null}}
```

`.venv/bin/python -m graph_lab show data/small-dag.csv`: estado 0, sin traceback.
`.venv/bin/python -m graph_lab sort data/small-dag.csv`: estado 0, sin traceback.
`.venv/bin/python -m graph_lab show data/cs-curriculum.csv`: estado 0, sin traceback.
`.venv/bin/python -m graph_lab sort data/cs-curriculum.csv`: estado 0, sin traceback.
`.venv/bin/python -m graph_lab show data/build-with-cycle.csv`: estado 0, sin traceback.
`.venv/bin/python -m graph_lab sort data/build-with-cycle.csv`: estado 1, sin traceback.

AS-301/303: fixture indirecto y duplicado; AS-302: cero, empate, aislado,
ciclos y autoaristas; AS-304: 15 variantes de errores; AS-305: origen inexistente,
vacío, ruta inexistente, uso y ayuda; AS-306: seis invocaciones originales y rechazo
de su esquema por shortest. No se comparan caminos exactos cuando hay empate.
Los CSV originales siguen íntegros. Las pruebas comprueban estados y canales.
No se atribuye revisión interactiva al estudiante.
