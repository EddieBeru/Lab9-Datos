# Contrato CLI

`python -m graph_lab show ARCHIVO`
Éxito: JSON {"vertices": [...], "edges": [[origen, destino], ...]}, salto de línea,
Unicode conservado, claves indicadas, listas ordenadas lexicográficamente. Estado 0,
stderr vacío. --help muestra uso por stdout y estado 0.
Lectura/codificación: Error: no se pudo leer ARCHIVO por stderr y estado 1.
Estructura: Error: línea N: DESCRIPCIÓN por stderr y estado 1.
Argumentos inválidos: uso y error argparse en stderr, estado 2.
Sin traceback para errores esperados ni datos parciales.
