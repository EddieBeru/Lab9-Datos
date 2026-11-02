# Contrato

python -m graph_lab shortest ARCHIVO ORIGEN
CSV: source,target,weight. Salida JSON distances y paths con claves ordenadas;
inalcanzables null. Cualquier camino mínimo en empates. Éxito 0 y stderr vacío.
Errores 1, stderr Error: línea N: DESCRIPCIÓN, Error: no se pudo leer ARCHIVO,
o Error: origen inexistente: NOMBRE, sin stdout parcial ni traceback. Uso 2, ayuda 0.
Show/sort conservan los formatos sin pesos y no aceptan CSV ponderado silenciosamente.
