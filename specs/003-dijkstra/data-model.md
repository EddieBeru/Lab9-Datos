# Modelo ponderado

WeightedGraph.neighbors: nombre no vacío → (destino → entero >=0).
Todo destino existe como clave. Duplicado conserva mínimo; aislado tiene mapa vacío.
El lector recorta nombres y pesos, exige origen, tres campos y encabezado exacto.
Fila origen,, declara aislado, sin peso. Ciclos y bucles no negativos válidos.

Distancias internas: entero o ausencia, no float infinito. Predecesores solo para
mejoras estrictas. Salida: distances y paths ordenados por nombre; inalcanzables null;
origen 0 y [origen]. Validar origen antes de buscar. No se muta grafo al consultar.
