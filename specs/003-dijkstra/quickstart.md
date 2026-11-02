# Validación rápida

```sh
.venv/bin/python -m pip install -e '.[test]'
.venv/bin/python -m pytest -q
.venv/bin/python -m graph_lab shortest tests/data/weighted.csv a
```

Esperado: a=0, c=1, b=3, z=null; camino b=[a,c,b]. Reejecutar show/sort sobre
los tres CSV originales; solo sort del archivo con ciclo tiene estado 1 esperado.
