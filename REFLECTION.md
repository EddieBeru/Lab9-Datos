# Reflexión del laboratorio

Esta reflexión combina la experiencia aportada por el grupo con los resultados
verificables del laboratorio.

Nuestra experiencia fue que agy nos falló, así que nos fuimos a Codex y funcionó
«de 10». Agy duró demasiado y, según nuestra experiencia, se quedó sin tokens
con una espera de 120 horas. El inconveniente fue el tiempo y el límite de uso,
no un comportamiento que podamos atribuir a una especificación ambigua o a que
el agente ignorara instrucciones. Como comentario humorístico sobre el uso
de recursos, lo resumimos así: «Felicidades a OpenAI por drenar la represa de
Cartago para ayudar con este lab». La frase es una broma del grupo, no un hecho
comprobado sobre consumo de agua.

Se utilizó Codex con la integración de Spec Kit 1.2.3 y habilidades locales. El
laboratorio comenzó dentro de un repositorio que también contenía otros trabajos.
Tras la decisión del estudiante, se creó un repositorio independiente en lab9 con
rama main y se preservaron los materiales originales. Los archivos de README,
documentación y datos se reubicaron sin cambiar su contenido, comprobado con SHA-256.
Las fases quedaron en commits separados, con análisis y validaciones conservados.

La pregunta de comportamiento efectivamente formulada fue cómo tratar la fila
watch, de small-dag.csv. Se recomendó conservar watch como vértice aislado. El
estudiante respondió «todo eso recomendado»; las otras políticas se documentaron
como recomendaciones delegadas, sin inventar una serie de preguntas respondidas.
Se eligió unificar aristas repetidas, conservar ciclos y bucles al mostrar, recortar
espacios exteriores de nombres y distinguir mayúsculas. Un encabezado sin filas
representa un grafo vacío; un archivo sin encabezado, origen vacío o filas inválidas
produce error. La consulta show entrega JSON estable. En Feature 2, sort elige el
menor nombre disponible entre dependencias satisfechas y nunca devuelve un orden
parcial si existe un ciclo. Las decisiones están en Clarifications, requisitos y
escenarios de cada especificación.

Los archivos contienen cuatro particularidades relevantes. cs-curriculum.csv repite
Data Structures → Algorithms; el grafo conserva una sola arista y muestra 23 aristas
únicas. small-dag.csv contiene watch, y por ello muestra nueve vértices, incluido el
vértice aislado. build-with-cycle.csv conserva auth → session → user-profile → auth
y metrics → metrics al mostrar, pero sort termina con diagnóstico y estado 1. Su
carga no se rechaza por tener un ciclo: cargar y ordenar tienen contratos distintos.
Los tres CSV originales participan en pruebas y validaciones de ambas features.

La representación elegida fue un diccionario de conjuntos de vecinos. Mantiene los
vértices aislados como claves y unifica duplicados directamente. La memoria es
O(V+E), y la inserción y consulta de aristas tienen coste esperado constante. Se
rechazó una matriz por su memoria O(V²) y una lista de aristas porque complica las
consultas de vecinos y los aislados. La representación se sostuvo en Feature 2:
solo se añadieron grados de entrada temporales y un heap para el algoritmo propio
de Kahn, con tiempo O(E + V log V). DFS también permite detectar ciclos, pero no
expresa directamente el desempate acordado. NetworkX se usa exclusivamente como
oráculo de pruebas; la aplicación no importa bibliotecas de grafos.

Los informes de analyze registraron cero hallazgos CRITICAL o HIGH y cobertura
prevista de los escenarios mediante tareas de pruebas. Esto no garantizó ausencia
de errores: durante implementación de Feature 1 se descubrió que la especificación
y su prueba atribuían diez vértices a small-dag, aunque el archivo tiene nueve. Se
corrigieron primero especificación e investigación, se repitió analyze y se confirmó
la salida correcta. Ese error fue descubierto por pruebas, no por el análisis
inicial. En Feature 1 se observaron 24 pruebas fallidas antes de la lógica y luego
24 aprobadas. En Feature 2 hubo 14 fallos nuevos, conservando las 24 regresiones;
tras implementar el ordenamiento, las 38 pruebas aprobaron también sobre main.
Los dos DAG producen orden válido y el archivo con ciclo produce el error esperado.

No recordamos una decisión especialmente complicada. Delegamos las recomendaciones
al agente y revisamos el resultado mediante requisitos, pruebas y ejecución de la
CLI. El incidente que señalamos fue la demora y el agotamiento de tokens de agy;
no recordamos otro caso concreto de comportamiento inesperado atribuible a una
ambigüedad de la especificación. No inventamos un incidente adicional para cubrir
esa pregunta: el límite de esta respuesta es que el problema recordado fue de
recursos y tiempo, no de interpretación de un requisito.


En el extra se mantuvo la representación original de las primeras features y se añadió
un grafo ponderado separado, con diccionario de diccionarios de pesos enteros no negativos.
Así no hubo que reescribir show ni sort. Dijkstra usa heap y predecesores, devuelve
costes y caminos a todos los vértices y marca los inalcanzables con null. Los duplicados
conservan el menor peso. Los casos cero, ciclos y empates se comparan con NetworkX;
no se exige un camino único si hay empate. El análisis final no dejó CRITICAL/HIGH.
Las 20 pruebas nuevas fallaron antes de implementar; después pasaron las 58 pruebas,
incluidas las regresiones, también tras la fusión del extra en main.
