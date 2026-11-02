# Auditoría de cierre — parcial

Fecha: 2026-11-01. Revisión de aplicación: main b0e25e5.
Este documento no declara el proyecto terminado. Se aplican los prompts auxiliares
de docs/prompts/cierre-proyecto.md sobre evidencia real; el extra sigue sin decisión.

| Entregable | Estado | Evidencia y siguiente acción |
| --- | --- | --- |
| Constitución | Completo | d5a518c, sin marcadores; docs/constitucion.md |
| Feature 1 | Completa localmente | specs/001-directed-graphs, merge 849f29a |
| Feature 2 | Completa localmente | specs/002-topological-sort, merge b0e25e5 |
| Fases y commits | Completos | git log, commits separados por fase, sin squash |
| Pruebas | Pasan | pytest 38 passed después del merge en main |
| CLI manual | Conforme | show/sort de tres CSV en validaciones y repetidos en main |
| Extra | Decisión pendiente | Se preguntó omitir, Dijkstra o expansión mínima |
| Reflexión | Borrador factual | REFLECTION.md; faltan respuestas personales |
| Publicación | Pendiente | Sin remoto; URL o nombre/visibilidad solicitados |
| Entrega | Pendiente | No existe enlace de entrega confirmado |

## Verificaciones ejecutadas

- Python 3.12.3, pytest 9.1.1; mínimo del paquete >=3.11.
- python3 -m venv .venv y .venv/bin/python -m pip install -e '.[test]': éxito;
  instalación actualizada para incorporar NetworkX de pruebas en Feature 2.
- .venv/bin/python -m pytest -q: 38 passed, estado 0 tras merge b0e25e5.
- .venv/bin/python -m pip check: No broken requirements found, estado 0.
- .venv/bin/python -m graph_lab show data/small-dag.csv: 0; 9 vértices, 9 aristas.
- .venv/bin/python -m graph_lab show data/cs-curriculum.csv: 0; 19 vértices, 23 aristas.
- .venv/bin/python -m graph_lab show data/build-with-cycle.csv: 0; 11 vértices, 13 aristas.
- .venv/bin/python -m graph_lab sort data/small-dag.csv: 0, orden completo válido.
- .venv/bin/python -m graph_lab sort data/cs-curriculum.csv: 0, orden completo válido.
- .venv/bin/python -m graph_lab sort data/build-with-cycle.csv: 1, stdout vacío,
  Error: el grafo contiene un ciclo; no existe orden topológico por stderr.
- Inspección AST de imports en src: sin bibliotecas de grafos prohibidas.
- pyproject.toml no declara dependencias runtime; NetworkX solo extra test.
- git merge-base --is-ancestor para ambas ramas contra main: éxito.
- Artefactos obligatorios presentes, Clarifications en ambas specs, ninguna tarea
  pendiente y sin marcadores de decisiones en especificaciones.
- Datos originales comprobados íntegros contra commit inicial en validación Feature 1.

## Evidencia y límites

Los comandos del agente se ejecutaron como habilidades Codex instaladas siguiendo
sus SKILL.md, con los prompts completos de las guías; los scripts auxiliares reales
se ejecutaron según sus procedimientos. No son comandos shell /speckit.*.
La constitución se ejecutó antes del primer commit; se conserva evidencia de esta
conversación, sin inventar un historial Git previo. Las políticas posteriores fueron
recomendaciones delegadas por «todo eso recomendado», no entrevistas ficticias.

El conteo inicial incorrecto de 10 vértices en small-dag se detectó durante pruebas,
se corrigió primero en spec y plan y se repitió analyze antes de continuar. Los
análisis no reportaron ese error inicialmente; no se les atribuye su descubrimiento.

Sin CRITICAL o HIGH pendientes. No se ha realizado push ni creado remoto. No se
ha inventado experiencia personal. Solo se conservan resultados realmente ejecutados.
Siguiente acción: recibir decisión del extra y datos de publicación/reflexión;
completar guía aplicable, reflexión y auditoría, commit final y push de ramas explícitas.
