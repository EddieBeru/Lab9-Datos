# Modelo de datos

Graph: neighbors, diccionario de nombres a conjuntos de nombres destino.
Invariante: todo destino también existe como clave. Nombre: cadena no vacía,
recortada y sensible a mayúsculas. Aristas: únicas; bucles y ciclos permitidos.
Vértice aislado: clave con conjunto vacío; no existe vértice de nombre vacío.

Carga: archivo → encabezado validado → filas validadas → grafo completo → salida.
Cualquier fallo invalida toda la consulta; no hay estado persistente ni salida parcial.
El lector registra línea física con csv.reader.line_num para errores estructurales.
