# Validación rápida

Con Python >=3.11, desde raíz:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[test]'
.venv/bin/python -m pytest -q
.venv/bin/python -m graph_lab sort data/small-dag.csv
.venv/bin/python -m graph_lab sort data/cs-curriculum.csv
.venv/bin/python -m graph_lab sort data/build-with-cycle.csv
```

Los dos primeros ordenan con estado 0, incluido watch. El tercero informa ciclo
por stderr y estado 1, sin stdout. Volver a ejecutar show para los tres: todos 0.
Verificar cada precedencia y comparar con oráculo; no asumir que los datos tengan
una sola solución matemática aunque el contrato haya fijado un desempate.
