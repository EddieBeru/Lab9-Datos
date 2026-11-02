# Feature Specification: Caminos mínimos con Dijkstra

**Feature Branch**: 003-dijkstra
**Created**: 2026-11-01
**Status**: Borrador
**Input**: Prompt íntegro en prompt-specify.txt; elección real del usuario: dijkstra.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Consultar caminos mínimos (Priority: P1)

Usuario consulta desde un origen el coste mínimo y camino hasta cada vértice.
**Why this priority**: Resuelve el extra elegido.
**Independent Test**: Grafo ponderado con un camino indirecto más barato.

**Acceptance Scenarios**:

- AS-301: Dado a→b coste 5, a→c coste 1 y c→b coste 2, desde a se obtiene
  distancia b=3 y camino [a,c,b], distancia c=1 y origen a=0 con camino [a].
- AS-302: Con vértice aislado z, resulta inalcanzable desde a; con pesos cero,
  ciclos, bucles y empates, los caminos devueltos son válidos y mínimos.
- AS-303: Repetir a→b con distintos pesos conserva el menor coste.

### User Story 2 - Comprender entradas inválidas (Priority: P2)

**Why this priority**: Dijkstra requiere pesos compatibles.
**Independent Test**: Rechazar peso negativo sin producir salida parcial.

**Acceptance Scenarios**:

- AS-304: Peso negativo, ausente en arista, no numérico o fila malformada genera
  error con línea, estado 1, stderr y sin salida parcial ni traceback.
- AS-305: Origen inexistente o grafo vacío genera error de origen; archivo ilegible
  y uso incorrecto conservan estados 1/2. Ayuda termina con estado 0.
- AS-306: show y sort mantienen los resultados de los tres CSV originales.

### Edge Cases

Cero, negativos, decimales, infinito, duplicados con pesos distintos, aislados,
desconexión, ciclos, autoaristas, grafo vacío y origen inexistente.

## Requirements *(mandatory)*

### Functional Requirements

- FR-301: Devolver distancias mínimas y caminos válidos desde un origen a todos
  los vértices de un grafo dirigido ponderado; origen distancia cero.
- FR-302: [NEEDS CLARIFICATION: formato de pesos y tratamiento de duplicados/aislados.]
- FR-303: [NEEDS CLARIFICATION: invocación, salida e inalcanzables/empates.]
- FR-304: Rechazar pesos negativos y entradas inválidas sin resultado parcial;
  conservar canales y estados de errores 1/2 de funcionalidades previas.
- FR-305: Conservar show/sort y comprobar escenarios con oráculo solo en pruebas,
  fixtures ponderados nuevos y regresiones de los tres CSV originales sin alterarlos.

### Key Entities

Arista ponderada: origen, destino y coste. Camino: secuencia dirigida desde origen.
Distancia: mínimo coste acumulado, o ausencia de camino si es inalcanzable.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- SC-301: Todas las distancias y caminos comprobados coinciden en coste con el oráculo.
- SC-302: Todos los casos inválidos definidos tienen error observable sin traceback.
- SC-303: Todas las regresiones de show/sort siguen pasando.

## Assumptions

Solo Dijkstra, sin expansión mínima, sin modificar el formato de las primeras features.
