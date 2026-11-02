# Feature Specification: Caminos mínimos con Dijkstra

**Feature Branch**: 003-dijkstra
**Created**: 2026-11-01
**Status**: Aclarada
**Input**: Prompt íntegro en prompt-specify.txt; elección real del usuario: dijkstra.

## Clarifications

### Session 2026-11-01

Recomendaciones delegadas por la autorización previa «todo eso recomendado»;
no son preguntas históricas inventadas. La elección Dijkstra sí fue explícita.

- CSV separado source,target,weight, UTF-8 con BOM opcional, dos extremos y peso
  entero no negativo en notación decimal ASCII (dígitos 0–9); cero permitido.
  Se recortan espacios. Decimales, signos, NaN, infinito y negativos se rechazan.
- Fila source,, declara aislado; requiere peso vacío. Origen vacío, otra cantidad
  de columnas o peso ausente en arista se rechaza con línea. Líneas vacías se ignoran.
  Encabezado exacto; solo encabezado permite grafo vacío. Mayúsculas distinguen nombres.
- Aristas dirigidas; duplicados usan mínimo peso, ciclos y bucles no negativos válidos.
  Un contrato ponderado separado evita cambiar show/sort o asumir pesos de CSV antiguos.
- shortest ARCHIVO ORIGEN devuelve JSON distances y paths con todos los nombres
  ordenados; inalcanzables null en ambos, origen 0 y [origen]. Éxito 0, stderr vacío.
  No se exige un camino único en empates: cualquier recorrido mínimo válido sirve.
- Origen inexistente, también en vacío: Error: origen inexistente: NOMBRE, estado 1.
  Formato/lectura conserva Error: línea N: DESCRIPCIÓN o Error: no se pudo leer ARCHIVO;
  argumentos inválidos 2; errores sin stdout parcial ni traceback; ayuda 0.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Consultar caminos mínimos (Priority: P1)

Usuario consulta desde un origen el coste mínimo y camino hasta cada vértice.
**Why this priority**: Resuelve el extra elegido.
**Independent Test**: Grafo ponderado con un camino indirecto más barato.

**Acceptance Scenarios**:

- AS-301: Dado a→b coste 5, a→c coste 1 y c→b coste 2, desde a se obtiene
  distancia b=3 y camino [a,c,b], distancia c=1 y origen a=0 con camino [a].
- AS-302: Con vértice aislado z, resulta inalcanzable desde a; con pesos cero,
  ciclos, bucles y empates, los caminos devueltos son válidos y mínimos;
  z tiene null en distances y paths.
- AS-303: Repetir a→b con distintos pesos conserva el menor coste.

### User Story 2 - Comprender entradas inválidas (Priority: P2)

**Why this priority**: Dijkstra requiere pesos compatibles.
**Independent Test**: Rechazar peso negativo sin producir salida parcial.

**Acceptance Scenarios**:

- AS-304: Peso negativo, ausente en arista, no numérico o fila malformada genera
  error con línea, estado 1, stderr y sin salida parcial ni traceback. Se prueban
  también decimales, infinito, origen vacío, comillas inválidas, UTF-8 inválido,
  encabezado erróneo y peso presente en aislado; codificación usa error de lectura.
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
- FR-302: Leer source,target,weight con las reglas de Clarifications: enteros ASCII
  no negativos, aislados mediante fila de tres campos con destino y peso vacíos; mínimos duplicados, nombres recortados sensibles
  a mayúsculas, ciclos/bucles permitidos, encabezado obligatorio y líneas vacías ignoradas.
  La notación source,, significa exactamente tres campos, dos vacíos tras el origen.
- FR-303: shortest ARCHIVO ORIGEN devuelve JSON distances y paths con claves
  ordenadas, valores null para inalcanzables, origen 0/[origen], cualquier camino
  mínimo en empate. Origen inexistente: Error: origen inexistente: NOMBRE, estado 1.
  Ayuda 0; contratos de formato/lectura y uso según Clarifications.
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
