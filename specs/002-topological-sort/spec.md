# Feature Specification: Orden topológico

**Feature Branch**: 002-topological-sort
**Created**: 2026-11-01
**Status**: Aclarada
**Input**: Prompt completo en prompt-specify.txt, sobre Feature 1 fusionada en 849f29a.

## Clarifications

### Session 2026-11-01

El usuario autorizó «todo eso recomendado» para decisiones de comportamiento;
estas son recomendaciones delegadas, no una lista ficticia de preguntas respondidas.

- Integración: sort ARCHIVO mantiene show y lectura de Feature 1, sin cambios.
- Determinismo: elegir el menor nombre Unicode entre vértices cuyas dependencias
  ya aparecieron; hace reproducible la salida. Se conserva la dirección source → target.
- Formato: JSON con clave order y lista de nombres; éxito 0, stderr vacío.
- Ciclos y bucles: estado 1, stdout vacío y mensaje Error: el grafo contiene un ciclo;
  no existe orden topológico. No se exige identificar un ciclo concreto ni se devuelve
  un orden parcial; evita presentar una secuencia incompleta como solución.
- Desconexión y aislados: incluir todos; grafo vacío produce order vacío, estado 0.
  Errores de lectura/formato y argumentos mantienen estados 1/2 y canales de Feature 1.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Obtener una secuencia válida (Priority: P1)

Como usuario quiero procesar cada dependencia antes de sus dependientes.
**Why this priority**: Es el objetivo de la segunda funcionalidad.
**Independent Test**: Ordenar un grafo acíclico y comprobar toda precedencia.

**Acceptance Scenarios**:

- **AS-201**: Dado small-dag.csv, al ordenar con sort aparecen sus 9 vértices una vez,
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

- **AS-204**: Dado build-with-cycle.csv, al ordenar no se imprime stdout;
  stderr contiene el mensaje exacto de FR-203 y el estado es 1.
- **AS-205**: Dados solo un ciclo o solo una autoarista, al ordenar se informa
  imposibilidad con el mismo mensaje y estado de FR-203 y sin salida parcial,
  incluso si existen también componentes acíclicos.
- **AS-206**: Dada entrada inválida o invocación incorrecta, al ordenar se conserva
  la política de errores de Feature 1 (lectura/formato 1, uso 2, sin traceback).
  show sigue aceptando ciclos y bucles; sort --help termina en 0 y muestra ayuda.

- **AS-207**: Dados b,c y a,c, al ordenar se obtiene order [a,b,c] en
  ejecuciones repetidas y con filas permutadas: entre nombres disponibles se elige
  el menor. Los demás escenarios exitosos también producen JSON con clave order,
  estado 0 y stderr vacío.

### Edge Cases

Múltiples órdenes válidos, grafo vacío, componentes desconectados, aislados,
duplicados, ciclos y bucles, ausencia de resultado parcial y errores de lectura.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-201**: Obtener un orden con todos los vértices exactamente una vez y con
  origen anterior a destino para cada arista; preservar lectura y show de Feature 1.
- **FR-202**: Ofrecer sort ARCHIVO; JSON {"order": [nombres]} por stdout con
  salto de línea. Elegir siempre el menor nombre Unicode disponible según las
  dependencias ya satisfechas; éxito 0 y stderr vacío. Grafo vacío: {"order": []}.
- **FR-203**: Si existe cualquier ciclo o autoarista, terminar con estado 1,
  stdout vacío, sin traceback y stderr exactamente:
  Error: el grafo contiene un ciclo; no existe orden topológico (con salto final).
  No producir salida parcial ni exigir identificar un recorrido concreto.
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
pertenecen al plan. Las recomendaciones delegadas están reflejadas arriba en requisitos y escenarios.
