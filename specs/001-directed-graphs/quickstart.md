# Validación rápida

Desde la raíz con Python 3.11+:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[test]'
.venv/bin/python -m pytest -q
.venv/bin/python -m graph_lab show data/small-dag.csv
.venv/bin/python -m graph_lab show data/cs-curriculum.csv
.venv/bin/python -m graph_lab show data/build-with-cycle.csv
```

Todos los show terminan en 0; contrastar resultados con AS-002–AS-004 y contracts/cli.md.
Para errores, consultar ruta inexistente y verificar stderr, stdout vacío y estado 1.
