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

Para obtener un orden topológico:

```sh
.venv/bin/python -m graph_lab sort data/small-dag.csv
.venv/bin/python -m graph_lab sort data/cs-curriculum.csv
.venv/bin/python -m graph_lab sort data/build-with-cycle.csv
```

`sort` devuelve JSON con `order`, incluyendo vértices aislados y componentes
desconectados. Elige el menor nombre Unicode entre los disponibles en cada paso.
Los dos primeros ejemplos terminan en 0. El tercero termina en 1, sin stdout,
con diagnóstico de ciclo en stderr; también se rechazan autoaristas para ordenar.
`show` sigue aceptando ciclos. Un grafo vacío produce `{"order": []}`.
NetworkX se instala solo mediante el extra de pruebas y actúa como oráculo;
la aplicación implementa su propio algoritmo y no lo importa.

Extra Dijkstra, grafos dirigidos con pesos enteros no negativos:

```sh
.venv/bin/python -m graph_lab shortest tests/data/weighted.csv a
```

Usa otro CSV con encabezado `source,target,weight`. Una fila `z,,` declara un
vértice aislado. Los duplicados conservan el menor peso. Se admiten cero, ciclos
y bucles; se rechazan negativos, decimales y pesos ausentes en aristas.
La salida incluye `distances` y `paths` para todos los vértices, con `null` para
inalcanzables; el origen tiene distancia 0 y camino de un solo vértice. En empates
se devuelve cualquier camino mínimo válido. Origen inexistente genera error 1.
Los CSV sin pesos originales siguen usándose exclusivamente con `show` y `sort`.
