# Tasks: Orden topológico

**Input**: spec.md, plan.md, research.md, data-model.md, contracts/cli.md.

## Phase 1: Setup

- [x] T001 Añadir NetworkX solo al extra test en pyproject.toml e instalar entorno (FR-205).

## Phase 2: Foundational

- [x] T002 Escribir tests/test_sort.py para AS-201–207, oráculo y regresión; ejecutar rojo antes de lógica (FR-201–205).

## Phase 3: User Story 1 (P1)

Objetivo y prueba independiente: orden válido y determinista para DAG, incluidos aislados.

- [x] T003 [US1] Añadir topological_order propio a src/graph_lab/graph.py usando grados y heap sin mutar el grafo (FR-201/202/204, AS-201–203/207).
- [x] T004 [US1] Añadir sort ARCHIVO y JSON order en src/graph_lab/cli.py preservando show (FR-201/202, AS-201–203/207).

## Phase 4: User Story 2 (P2)

Objetivo y prueba independiente: no devolver orden parcial para ciclos o bucles.

- [x] T005 [US2] Detectar ciclo por cantidad emitida en src/graph_lab/graph.py y convertirlo en mensaje exacto, stderr y estado 1 en cli.py; preservar errores 1/2 y ayuda 0 (FR-203, AS-204–206).

## Phase 5: Polish

- [x] T006 Actualizar docs/USAGE.md y ejecutar suite, regresiones y revisión manual sort/show sobre los tres CSV; registrar specs/002-topological-sort/validacion.md (FR-205, SC-201–203).

## Dependencies & Execution Order

T001 → T002 → T003 → T004 → T005 → T006. Sin tareas P porque comparten archivos.
US2 usa CLI y grafo US1; se valida de forma independiente con un ciclo.
Ejemplo de paralelismo futuro: documentación de uso y revisión del informe ya generado
tras T006, sin cambios al código y sin delegación implícita.

## Implementation Strategy

MVP orden DAG, luego errores completos y suite con oráculo, finalmente revisión manual.
T002 cubre todos AS; T003/004 cubren FR-201/202/204; T005 cubre FR-203;
T001/002/006 cubren FR-205 y SC-201–203. Sin tareas fuera de alcance.
