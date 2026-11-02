# Feature Specification: Orden topológico

**Feature Branch**: 002-topological-sort
**Created**: 2026-11-01
**Status**: Borrador
**Input**: Prompt completo en prompt-specify.txt, sobre Feature 1 fusionada en 849f29a.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Obtener una secuencia válida (Priority: P1)

Como usuario quiero procesar cada dependencia antes de sus dependientes.
**Why this priority**: Es el objetivo de la segunda funcionalidad.
**Independent Test**: Ordenar un grafo acíclico y comprobar toda precedencia.

**Acceptance Scenarios**:

- **AS-201**: Dado small-dag.csv, al ordenar aparecen sus 9 vértices una vez,
  incluido watch, y cada origen precede a su destino.
- **AS-202**: Dado cs-curriculum.csv, al ordenar aparecen sus 19 vértices una vez
  y se respetan las 23 dependencias únicas; el duplicado no añade restricciones.
- **AS-203**: Dados componentes desconectados, aislados o grafo vacío,
  al ordenar se incluyen todos los vértices una vez o una lista vacía respectivamente.

### User Story 2 - Detectar orden imposible (Priority: P2)

Como usuario quiero saber si mis dependencias impiden obtener un orden.
**Why this priority**: Un orden inválido induciría a procesar mal las dependencias.
**Independent Test**: Ordenar un ciclo y comprobar el error.

**Acceptance Scenarios**:

- **AS-204**: Dado build-with-cycle.csv, al ordenar se informa que no existe orden.
- **AS-205**: Dados solo un ciclo o solo una autoarista, al ordenar se informa
  imposibilidad incluso si existen también componentes acíclicos.
- **AS-206**: Dada entrada inválida o invocación incorrecta, al ordenar se conserva
  la política de errores de Feature 1. show sigue aceptando ciclos y bucles.

### Edge Cases

Múltiples órdenes válidos, grafo vacío, componentes desconectados, aislados,
duplicados, ciclos y bucles, ausencia de resultado parcial y errores de lectura.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-201**: Obtener un orden con todos los vértices exactamente una vez y con
  origen anterior a destino para cada arista; preservar lectura y show de Feature 1.
- **FR-202**: [NEEDS CLARIFICATION: comando, formato y determinismo del orden.]
- **FR-203**: [NEEDS CLARIFICATION: diagnóstico de ciclo, detalle y salida parcial.]
- **FR-204**: Admitir aislados, desconexión y grafo vacío según AS-203; unificar
  duplicados antes de ordenar conforme a la política de Feature 1.
- **FR-205**: Probar escenarios, errores y regresiones, incluidos tres CSV originales.

### Key Entities

Orden: secuencia completa de nombres. Dependencia: relación dirigida source → target.
Ciclo: recorrido dirigido que vuelve a su origen, incluido bucle de longitud uno.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-201**: Toda salida exitosa satisface el 100 % de las precedencias.
- **SC-202**: Todos los grafos con ciclos comprobados se reportan como imposibles.
- **SC-203**: Todos los escenarios de Feature 1 conservan su comportamiento.

## Assumptions

Sin pesos ni modificación de CSV originales. La representación y algoritmo
pertenecen al plan. Las decisiones pendientes se resolverán antes de diseñar.
