# Tasks: Grafos dirigidos

**Input**: spec.md, plan.md, research.md, data-model.md, contracts/cli.md.
Pruebas obligatorias; ejecución secuencial salvo indicación explícita.

## Phase 1: Setup

- [ ] T001 Configurar Python >=3.11 y extra test pytest en pyproject.toml; crear src/graph_lab/__init__.py y __main__.py mínimos para arranque (FR-004/006).

## Phase 2: Foundational

- [ ] T002 Escribir tests/test_reader.py y tests/test_show.py con AS-001–AS-009, pruebas de canales y códigos, y ejecutar rojo antes de lógica (FR-001–FR-006).

## Phase 3: User Story 1 (P1)

Objetivo: mostrar todas las relaciones; validación independiente con los tres CSV.

- [ ] T003 [US1] Implementar src/graph_lab/graph.py con vértices no vacíos, destinos presentes y aristas únicas, incluidos aislados, ciclos y bucles (FR-001/002, AS-001–004).
- [ ] T004 [US1] Implementar carga válida en src/graph_lab/reader.py: UTF-8-sig, dos columnas, nombres recortados sensibles a mayúsculas y encabezado exacto; destino vacío crea aislado (FR-003, AS-001–004/008/009).
- [ ] T005 [US1] Implementar show y JSON ordenado en src/graph_lab/cli.py y arranque __main__.py (FR-004, AS-001–004/008/009).

## Phase 4: User Story 2 (P2)

Objetivo: errores comprensibles sin salida parcial; prueba independiente con entradas inválidas.

- [ ] T006 [US2] Completar src/graph_lab/reader.py con rechazo de encabezado, columnas, origen vacío, CSV malformado y codificación; errores con línea según FR-005 (AS-005/006).
- [ ] T007 [US2] Completar src/graph_lab/cli.py con stderr, códigos 1/2, ayuda 0, sin traceback ni salida parcial para errores esperados (FR-005, AS-005–007).

## Phase 5: Polish

- [ ] T008 Ejecutar suite y revisar manualmente CLI con tres CSV originales; guardar comandos y resultados en specs/001-directed-graphs/validacion.md (FR-006, SC-001–003).
- [ ] T009 Documentar instalación y uso en docs/USAGE.md y decisiones/evidencia en specs/001-directed-graphs/seguimiento.md para REFLECTION.md.

## Dependencies & Execution Order

T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008 → T009.
US2 depende de infraestructura de carga/CLI de US1; sus errores son comprobables por separado.
Sin marcas P: pruebas de ambos archivos se ejecutan juntas antes de la lógica.
Ejemplo de paralelismo futuro: edición de docs/USAGE.md y lectura de validacion.md,
solo después de T008 y sin delegación adicional implícita.

## Implementation Strategy

MVP US1, completar errores US2, suite y revisión manual. Verificar fallos iniciales
por comportamientos ausentes, no por imports o instalación rotos. No hacer merge
dentro de implement. Cobertura: T002 prueba todos AS; T003–007 implementan FR-001–005;
T008 verifica FR-006 y SC-001–003. No hay tareas sin requisito o necesidad constitucional.
