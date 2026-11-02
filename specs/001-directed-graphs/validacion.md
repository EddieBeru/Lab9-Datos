# Validación Feature 1

Revisión de código: 1184fee. Python 3.12.3, pytest 9.1.1.

Instalación ejecutada: `python3 -m venv .venv` y
`.venv/bin/python -m pip install -e '.[test]'`: éxito.

Suite: `.venv/bin/python -m pytest -q`: 24 passed (estado 0).

## Revisión manual por el agente de los CSV originales

`.venv/bin/python -m graph_lab show data/small-dag.csv`
Estado 0; stderr ''.
```json
{"vertices": ["belt", "jacket", "pants", "shirt", "shoes", "socks", "tie", "undershorts", "watch"], "edges": [["belt", "jacket"], ["pants", "belt"], ["pants", "shoes"], ["shirt", "belt"], ["shirt", "tie"], ["socks", "shoes"], ["tie", "jacket"], ["undershorts", "pants"], ["undershorts", "shoes"]]}
```

`.venv/bin/python -m graph_lab show data/cs-curriculum.csv`
Estado 0; stderr ''.
```json
{"vertices": ["Algorithms", "Calculus I", "Calculus II", "Capstone Project", "Compilers", "Computer Architecture", "Computer Networks", "Data Structures", "Databases", "Discrete Mathematics", "Distributed Systems", "Linear Algebra", "Machine Learning", "Object-Oriented Programming", "Operating Systems", "Probability and Statistics", "Programming Fundamentals", "Software Engineering", "Theory of Computation"], "edges": [["Algorithms", "Compilers"], ["Algorithms", "Machine Learning"], ["Calculus I", "Calculus II"], ["Calculus I", "Linear Algebra"], ["Calculus II", "Probability and Statistics"], ["Computer Architecture", "Operating Systems"], ["Computer Networks", "Distributed Systems"], ["Data Structures", "Algorithms"], ["Data Structures", "Databases"], ["Data Structures", "Operating Systems"], ["Databases", "Software Engineering"], ["Discrete Mathematics", "Data Structures"], ["Discrete Mathematics", "Theory of Computation"], ["Distributed Systems", "Capstone Project"], ["Linear Algebra", "Machine Learning"], ["Object-Oriented Programming", "Data Structures"], ["Object-Oriented Programming", "Software Engineering"], ["Operating Systems", "Distributed Systems"], ["Probability and Statistics", "Machine Learning"], ["Programming Fundamentals", "Computer Architecture"], ["Programming Fundamentals", "Object-Oriented Programming"], ["Software Engineering", "Capstone Project"], ["Theory of Computation", "Compilers"]]}
```

`.venv/bin/python -m graph_lab show data/build-with-cycle.csv`
Estado 0; stderr ''.
```json
{"vertices": ["api", "auth", "config", "core", "logging", "metrics", "session", "storage", "user-profile", "utils", "web"], "edges": [["api", "web"], ["auth", "api"], ["auth", "session"], ["config", "core"], ["core", "auth"], ["core", "storage"], ["logging", "core"], ["metrics", "metrics"], ["session", "user-profile"], ["storage", "api"], ["user-profile", "auth"], ["utils", "config"], ["utils", "logging"]]}
```

Ruta inexistente: `.venv/bin/python -m graph_lab show missing.csv`: estado 1,
stdout vacío, stderr Error: no se pudo leer missing.csv, sin traceback.

CSV originales íntegros contra commit inicial. AS-001–009 cubiertos por tests;
los archivos ilegibles se prueban por PermissionError simulado porque los permisos
del proceso pueden permitir lectura aun sin bits de acceso.

Comparación: small-dag 9 vértices/9 aristas, watch aislado; curriculum 23 aristas
únicas; build conserva sus 13 aristas, ciclo y autoarista. Todos conformes.
Sin revisión interactiva del estudiante atribuida al historial.
