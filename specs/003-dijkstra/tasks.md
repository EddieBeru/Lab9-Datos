# Tasks: Dijkstra

**Input**: spec, plan, research, data-model y contrato de esta feature.

## Phase 1: Setup

- [x] T001 Añadir tests/data/weighted.csv con ruta indirecta, duplicados y aislado (FR-301/302).

## Phase 2: Foundational

- [x] T002 Escribir tests/test_shortest.py para AS-301–306 con oráculo y ejecutar rojo antes de lógica (FR-301–305).

## Phase 3: User Story 1 (P1)

Objetivo: caminos mínimos; comprobación independiente con fixture ponderado.

- [x] T003 [US1] Implementar src/graph_lab/weighted.py con enteros >=0, mínimo duplicado, Dijkstra y reconstrucción de rutas sin mutar (FR-301/302, AS-301–303).
- [x] T004 [US1] Implementar src/graph_lab/weighted_reader.py y shortest en cli.py, origen y salida distances/paths/null (FR-302/303, AS-301–303).

## Phase 4: User Story 2 (P2)

Objetivo: errores comprobables con una entrada inválida.

- [x] T005 [US2] Completar validación de pesos, columnas, encabezado, aislados y errores sin salida parcial en weighted_reader.py/cli.py (FR-304, AS-304/305).

## Phase 5: Polish

- [ ] T006 Ejecutar suite con oráculo y regresiones originales, revisión manual; guardar specs/003-dijkstra/validacion.md y actualizar docs/USAGE.md (FR-305, AS-306, SC-301–303).

## Dependencies & Execution Order

T001 → T002 → T003 → T004 → T005 → T006; sin P porque se comparten archivos.
US2 depende del despacho de US1, pero se verifica con entradas inválidas.
Ejemplo paralelo posible tras terminar código: revisión de docs y lectura de resultados,
sin modificar archivos compartidos ni delegar implícitamente.

## Implementation Strategy

MVP caminos y distancias, completar errores, oráculo y regresiones, validación manual.
T002 cubre todos AS, T003/004 FR-301–303, T005 FR-304 y T006 FR-305/SC-301–303.
