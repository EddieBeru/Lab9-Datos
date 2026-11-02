# Feature Specification: Grafos dirigidos sin pesos

**Feature Branch**: `001-directed-graphs`
**Created**: 2026-11-01
**Status**: Draft — pendiente de aclaraciones de comportamiento
**Input**: Prompt completo de Specify, sección 2 de docs/prompts/feature-1.md.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Consultar dependencias (Priority: P1)

Como usuario quiero cargar un archivo y ver sus vértices y aristas dirigidas.

**Why this priority**: Es la funcionalidad central del laboratorio.
**Independent Test**: Ejecutar la consulta de un archivo y contrastar vértices y aristas.

**Acceptance Scenarios**:

1. **AS-001 Given** un archivo con encabezado source,target y aristas válidas,
   **When** se carga y muestra, **Then** aparecen todos sus vértices y aristas,
   conservando la dirección de origen a destino.
2. **AS-002 Given** cs-curriculum.csv, **When** se consulta,
   **Then** se aplica a Data Structures,Algorithms la política de duplicados
   pendiente de aclarar en FR-002 y se muestra el resultado definido por ella.
3. **AS-003 Given** small-dag.csv, **When** se consulta,
   **Then** se aplica a watch, la política de extremos vacíos de FR-002.
4. **AS-004 Given** build-with-cycle.csv, **When** se consulta,
   **Then** se aplica al ciclo auth → session → user-profile → auth y al bucle
   metrics → metrics la política de FR-002, sin calcular un orden topológico.

### User Story 2 - Entender errores de entrada (Priority: P2)

Como usuario quiero conocer por qué mi archivo no puede procesarse.

**Why this priority**: Permite corregir entradas sin interpretar errores internos.
**Independent Test**: Consultar una ruta inexistente y comprobar el error observable.

**Acceptance Scenarios**:

1. **AS-005 Given** una ruta inexistente o sin permiso de lectura,
   **When** se intenta consultar, **Then** se informa el error por stderr,
   se termina con estado distinto de cero y no se muestra traceback.
2. **AS-006 Given** un archivo vacío, de solo encabezado o con filas malformadas,
   **When** se consulta, **Then** se aplica la política pendiente de FR-003.
3. **AS-007 Given** una invocación incorrecta,
   **When** se ejecuta, **Then** se informa por stderr y se termina con estado
   distinto de cero sin traceback, según el contrato pendiente de FR-004.

### Edge Cases

La revisión previa a clarify debe resolver: duplicados, destino u origen vacío,
ciclos, autoaristas, vértices aislados, archivo vacío, encabezado incorrecto,
columnas faltantes o adicionales, comillas, líneas vacías, codificación,
espacios y mayúsculas, orden de salida y rutas inexistentes o ilegibles.
Los escenarios anteriores son borradores hasta convertir estas políticas en
resultados concretos; no están listos para implementar.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El usuario DEBE poder cargar desde archivo un grafo dirigido sin pesos
  y consultar todos sus vértices y aristas, respetando la dirección source → target.
- **FR-002**: [NEEDS CLARIFICATION: definir tratamiento de aristas duplicadas,
  extremos vacíos, vértices aislados, ciclos y autoaristas en los tres CSV.]
- **FR-003**: [NEEDS CLARIFICATION: definir formato admitido, encabezado, identidad
  de nombres, espacios, mayúsculas, filas inválidas y archivos vacíos.]
- **FR-004**: [NEEDS CLARIFICATION: definir invocación, formato y orden de salida,
  mensajes y códigos concretos de terminación.]
- **FR-005**: Los resultados DEBEN ir a stdout; los errores a stderr con estado
  distinto de cero, sin traceback para errores esperados del usuario.
- **FR-006**: Cada escenario de aceptación DEBE validarse automáticamente;
  la validación DEBE incluir los tres archivos originales sin modificarlos.

### Key Entities

- **Vértice**: elemento identificado por un nombre, con identidad pendiente de aclarar.
- **Arista dirigida**: relación desde un vértice origen hasta un vértice destino.
- **Grafo**: conjunto de vértices y relaciones dirigidas sin pesos.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Para cada entrada aceptada, el usuario puede consultar el 100 % de los
  vértices y relaciones definidos por las reglas aclaradas.
- **SC-002**: Los tres archivos originales tienen resultados observables explícitos
  y comprobados conforme a sus escenarios de aceptación.
- **SC-003**: El 100 % de los errores especificados respeta los canales y estados
  acordados y no expone un traceback.

## Assumptions

- Se consulta un archivo local; no se requiere servicio externo ni persistencia.
- Orden topológico y pesos quedan fuera de Feature 1.
- Las políticas marcadas son decisiones pendientes, no respuestas atribuidas al usuario.
