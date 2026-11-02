# Uso del laboratorio

Requiere Python 3.11 o superior. Desde la raíz:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[test]'
.venv/bin/python -m graph_lab show data/small-dag.csv
.venv/bin/python -m pytest -q
```

`show ARCHIVO` devuelve JSON con vértices y aristas ordenados. CSV UTF-8,
BOM opcional, encabezado exacto `source,target`, dos columnas. Se recortan
espacios exteriores; las mayúsculas distinguen nombres. Destino vacío declara
un vértice aislado. Se unifican aristas repetidas y se conservan ciclos y bucles.
Solo encabezado es un grafo vacío; archivo vacío, origen vacío o fila malformada
son errores. Las líneas vacías se ignoran. Se admiten comillas según CSV.

Resultados por stdout; errores por stderr sin traceback para errores esperados.
Estado 0: éxito; 1: lectura/formato; 2: argumentos inválidos. `--help` muestra uso.
No se imprime resultado parcial ante errores. Sin dependencias de grafos en ejecución.
