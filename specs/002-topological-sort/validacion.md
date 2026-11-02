# Validación Feature 2

Python 3.12.3, pytest 9.1.1. Instalación actualizada mediante
`.venv/bin/python -m pip install -e '.[test]'`: éxito.
`.venv/bin/python -m pytest -q`: 38 passed, estado 0.

## Revisión manual por el agente

`.venv/bin/python -m graph_lab show data/small-dag.csv`
Estado 0.
```
{"vertices": ["belt", "jacket", "pants", "shirt", "shoes", "socks", "tie", "undershorts", "watch"], "edges": [["belt", "jacket"], ["pants", "belt"], ["pants", "shoes"], ["shirt", "belt"], ["shirt", "tie"], ["socks", "shoes"], ["tie", "jacket"], ["undershorts", "pants"], ["undershorts", "shoes"]]}
(stderr vacío)
```

`.venv/bin/python -m graph_lab sort data/small-dag.csv`
Estado 0.
```
{"order": ["shirt", "socks", "tie", "undershorts", "pants", "belt", "jacket", "shoes", "watch"]}
(stderr vacío)
```

`.venv/bin/python -m graph_lab show data/cs-curriculum.csv`
Estado 0.
```
{"vertices": ["Algorithms", "Calculus I", "Calculus II", "Capstone Project", "Compilers", "Computer Architecture", "Computer Networks", "Data Structures", "Databases", "Discrete Mathematics", "Distributed Systems", "Linear Algebra", "Machine Learning", "Object-Oriented Programming", "Operating Systems", "Probability and Statistics", "Programming Fundamentals", "Software Engineering", "Theory of Computation"], "edges": [["Algorithms", "Compilers"], ["Algorithms", "Machine Learning"], ["Calculus I", "Calculus II"], ["Calculus I", "Linear Algebra"], ["Calculus II", "Probability and Statistics"], ["Computer Architecture", "Operating Systems"], ["Computer Networks", "Distributed Systems"], ["Data Structures", "Algorithms"], ["Data Structures", "Databases"], ["Data Structures", "Operating Systems"], ["Databases", "Software Engineering"], ["Discrete Mathematics", "Data Structures"], ["Discrete Mathematics", "Theory of Computation"], ["Distributed Systems", "Capstone Project"], ["Linear Algebra", "Machine Learning"], ["Object-Oriented Programming", "Data Structures"], ["Object-Oriented Programming", "Software Engineering"], ["Operating Systems", "Distributed Systems"], ["Probability and Statistics", "Machine Learning"], ["Programming Fundamentals", "Computer Architecture"], ["Programming Fundamentals", "Object-Oriented Programming"], ["Software Engineering", "Capstone Project"], ["Theory of Computation", "Compilers"]]}
(stderr vacío)
```

`.venv/bin/python -m graph_lab sort data/cs-curriculum.csv`
Estado 0.
```
{"order": ["Calculus I", "Calculus II", "Computer Networks", "Discrete Mathematics", "Linear Algebra", "Probability and Statistics", "Programming Fundamentals", "Computer Architecture", "Object-Oriented Programming", "Data Structures", "Algorithms", "Databases", "Machine Learning", "Operating Systems", "Distributed Systems", "Software Engineering", "Capstone Project", "Theory of Computation", "Compilers"]}
(stderr vacío)
```

`.venv/bin/python -m graph_lab show data/build-with-cycle.csv`
Estado 0.
```
{"vertices": ["api", "auth", "config", "core", "logging", "metrics", "session", "storage", "user-profile", "utils", "web"], "edges": [["api", "web"], ["auth", "api"], ["auth", "session"], ["config", "core"], ["core", "auth"], ["core", "storage"], ["logging", "core"], ["metrics", "metrics"], ["session", "user-profile"], ["storage", "api"], ["user-profile", "auth"], ["utils", "config"], ["utils", "logging"]]}
(stderr vacío)
```

`.venv/bin/python -m graph_lab sort data/build-with-cycle.csv`
Estado 1.
```
(stdout vacío)
Error: el grafo contiene un ciclo; no existe orden topológico
```

## Cobertura

AS-201/202: ambos DAG originales; AS-203: vacío, desconectados, aislados y duplicado;
AS-204/205: archivo con ciclo y casos separados de ciclo y bucle, sin salida parcial;
AS-206: errores, ayuda y regresión show; AS-207: orden estable ante filas permutadas.
NetworkX confirma precedencias, cobertura, unicidad, desempate y presencia de ciclos.
Diez DAG generados con semilla fija amplían la comparación. Prueba de no mutación
confirma que ordenar dos veces conserva show. Todas las regresiones de Feature 1 pasan.
