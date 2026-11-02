# Investigación de Dijkstra

Decisión: WeightedGraph separado, vecinos dict[str,dict[str,int]]. Conserva Graph
sin pesos intacto; duplicados se actualizan con mínimo coste. Cambiar Graph a pesos
opcionales complicaría contratos sin necesidad; una lista de aristas hace costoso
recorrer vecinos y una matriz requiere O(V²) memoria. Investigación local delegada
según speckit-plan, sin necesidad de información externa.

Decisión: Dijkstra con heapq, distancias enteras y predecesores. Relajar solo mejoras
estrictas; descartar entradas de heap cuyo coste ya no sea el mejor. Esto evita que
ciclos de peso cero creen ciclos en predecesores. Reconstruir caminos al terminar.
Alternativa: barrido O(V²+E), menos apropiado para grafo disperso; no se necesita
Bellman-Ford porque negativos se rechazan. Costes completos en plan.md, incluidos
heap obsoleto y rutas devueltas O(V²).

Decisión: lector separado con csv.reader(strict=True), UTF-8-sig, validación ASCII
de dígitos antes de int. No float: evita NaN, infinitos y redondeos. NetworkX confirma
costes y pruebas propias verifican inicio/fin y suma de pesos de cada recorrido.
