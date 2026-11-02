# Investigación: representación y herramientas

Decisión: dict[str, set[str]], cada vértice es clave incluso si no tiene vecinos.
Razón: memoria O(V+E), insertar vértice/arista y consultar arista O(1) esperado,
carga O(V+E), recorrido O(V+E); conjuntos unifican duplicados y permiten bucles.
Ordenar solo al mostrar añade O(V log V + E log E).
Alternativa: lista de aristas más vértices aparte, consulta O(E), deduplicación
sin índice O(E²); complica aislados y recorrido de vecinos.
Alternativa: matriz, memoria y recorrido O(V²), requiere índices para nombres;
no se justifica para dependencias dispersas. Recomendación investigada por el
subagente graph_representation conforme al procedimiento de plan.
La representación permite calcular grados en O(V+E) en el futuro, sin implementar
topológico ahora. No se anticipan pesos.

Decisión: csv.reader(strict=True), UTF-8-sig y newline vacío para CSV con BOM,
comillas y saltos válidos; validación propia de encabezado y dos columnas.
Alternativa: split por comas rompe nombres entrecomillados. No se necesita pandas.
Decisión: argparse y json para contrato CLI; pytest para escenarios y subprocess
para canales/estados reales. Setuptools empaqueta src; ninguna dependencia runtime.

Resultados derivados por inspección: small-dag 9 vértices/9 aristas y watch aislado;
curriculum 23 aristas únicas; build 13 aristas con ciclo y bucle conservados.
