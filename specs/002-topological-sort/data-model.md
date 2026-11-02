# Modelo de datos

Graph conserva dict[str,set[str]] y sus invariantes de Feature 1.
Grado de entrada temporal: número de orígenes distintos que apuntan a cada vértice.
Disponible: vértice con grado cero aún no emitido. Resultado: lista de todos los nombres.
Transición: copiar grados → emitir mínimo disponible → decrementar sucesores →
terminar con lista completa o ValueError con mensaje de ciclo sin devolver lista parcial.
Grafo original no se modifica. Bucle aporta grado uno y bloquea completar su componente.
