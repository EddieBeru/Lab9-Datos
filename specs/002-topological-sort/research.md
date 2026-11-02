# Investigación: algoritmo y validación

Decisión: Kahn con grados de entrada y heap mínimo de vértices disponibles.
Razón: expresa directamente el desempate de FR-202. Cada arista se visita una vez,
cada vértice se inserta/extrae una vez: O(E + V log V), memoria O(V) adicional
al grafo O(V+E). No necesita ordenar los conjuntos de vecinos.
Ciclo si la cantidad procesada es menor que V; no se usa el residuo como si fuera
un ciclo exacto porque puede incluir dependientes. La spec solo pide diagnóstico.

Alternativa: DFS con colores, O(V+E), detecta ciclos y permite reconstruir recorrido,
pero inversión del postorden no garantiza el menor vértice disponible y la versión
recursiva añade límites de profundidad. No es necesaria para el diagnóstico acordado.
Alternativa: Kahn con cola, O(V+E), no satisface el desempate lexicográfico exigido.
No se cambia dict[str,set[str]]: aislados y destinos ya existen como claves, duplicados
ya unificados; grados temporales no modifican el grafo ni show.

Decisión: NetworkX solo en extra test y tests/test_sort.py, para comprobar existencia
de orden e igualdad con lexicographical_topological_sort, más comprobaciones propias
de unicidad/cobertura/precedencias. Nunca se importa en src ni es dependencia runtime.
