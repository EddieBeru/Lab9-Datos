# Feature Specification: Grafos dirigidos sin pesos

**Feature Branch**: `001-directed-graphs`
**Created**: 2026-11-01
**Status**: Aclarada
**Input**: Prompt completo de Specify en prompt-specify.txt; guía Feature 1.

## Clarifications

### Session 2026-11-01

- Pregunta efectivamente formulada: ¿cómo tratar watch,? → El usuario respondió
  «todo eso recomendado»; se aplica A: vértice aislado.
- El usuario autorizó resolver el resto mediante recomendaciones razonadas.
  Las siguientes son decisiones delegadas, no preguntas ni respuestas históricas:
  duplicados se unifican, ciclos y autoaristas se conservan (cargar no es ordenar);
  esto permite representar los archivos originales sin ocultar información.
- Recomendación aplicada: CSV UTF-8 (BOM permitido), encabezado exacto source,target,
  dos columnas; recortar espacios exteriores y conservar mayúsculas. Se descartan
  líneas físicamente vacías; un origen vacío o una fila incompleta se rechaza.
  Destino vacío significa vértice aislado. Archivo sin encabezado se rechaza;
  solo encabezado representa el grafo vacío.
- Recomendación aplicada: show ARCHIVO, salida JSON con vertices y edges ordenados
  lexicográficamente, sin datos parciales en errores; mensajes en español,
  éxito 0, errores de lectura/formato 1, argumentos inválidos 2.
  Un formato estructurado conserva nombres con comas y facilita validar resultados.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Consultar dependencias (Priority: P1)

Como usuario quiero cargar un archivo y ver sus vértices y aristas dirigidas.

**Why this priority**: Es la funcionalidad central.
**Independent Test**: Consultar un archivo y contrastar el resultado completo.

**Acceptance Scenarios**:

- **AS-001**: Dado CSV válido con a,b y b,c, al mostrarlo aparecen vertices
  [a,b,c] y edges [[a,b],[b,c]], con estado 0 y stderr vacío.
- **AS-002**: Dado cs-curriculum.csv, al mostrarlo aparecen 23 aristas distintas;
  Data Structures → Algorithms aparece una vez, con todos sus extremos presentes.
- **AS-003**: Dado small-dag.csv, al mostrarlo aparecen 9 vértices y 9 aristas;
  watch está presente sin aristas incidentes.
- **AS-004**: Dado build-with-cycle.csv, al mostrarlo aparecen sus 13 aristas,
  conservando el ciclo auth → session → user-profile → auth y metrics → metrics.
- **AS-008**: Dado encabezado sin filas, al mostrarlo aparecen vertices y edges
  vacíos con estado 0. Líneas vacías posteriores no cambian el resultado.
- **AS-009**: Dadas filas con espacios exteriores, etiquetas A y a, nombres con
  espacios internos o nombres entrecomillados con comas, al mostrar se recortan solo
  espacios exteriores; A y a siguen siendo distintos y las comas se conservan.

### User Story 2 - Entender errores de entrada (Priority: P2)

Como usuario quiero saber por qué una entrada no puede procesarse.

**Why this priority**: Permite corregir errores sin interpretar fallos internos.
**Independent Test**: Consultar entradas inválidas y revisar canales y estados.

**Acceptance Scenarios**:

- **AS-005**: Dada ruta inexistente, directorio o archivo ilegible, al mostrarlo
  stdout está vacío, stderr comienza por Error:, estado 1 y no hay traceback.
- **AS-006**: Dado archivo sin encabezado, encabezado distinto, número de columnas
  distinto de dos, origen vacío, comillas mal cerradas o bytes no UTF-8, al mostrar
  no hay resultado parcial; stderr comienza por Error:, estado 1 sin traceback.
  Los errores estructurales indican la línea; lectura/codificación identifica archivo.
- **AS-007**: Dada invocación sin comando, sin archivo o con argumentos desconocidos,
  se termina con estado 2, stdout vacío y ayuda de uso en stderr sin traceback.
  --help termina con estado 0 y ayuda en stdout.

### Edge Cases

Duplicados se unifican sin advertencia; ciclos y bucles se conservan.
Un origen vacío siempre es inválido, incluso si ambos extremos están vacíos.
Una línea sin campos se ignora; una fila con espacios o delimitadores se valida.
Los nombres quedan vacíos si solo contienen espacios exteriores.
Las filas válidas anteriores a un error nunca se imprimen parcialmente.
Se admiten saltos LF y CRLF y campos CSV entrecomillados; no se admiten comillas
mal cerradas. Los archivos se leen completos antes de producir resultados.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Cargar y mostrar todos los vértices y aristas source → target sin pesos.
- **FR-002**: Unificar aristas repetidas; aceptar ciclos y autoaristas; destino vacío
  declara únicamente el vértice origen, sin crear un vértice de nombre vacío.
- **FR-003**: Leer CSV UTF-8 con BOM opcional, encabezado exacto source,target,
  dos columnas, nombres recortados y sensibles a mayúsculas; ignorar líneas vacías,
  aceptar solo encabezado como grafo vacío y rechazar los errores de AS-006.
- **FR-004**: Ofrecer show ARCHIVO; resultado JSON con claves vertices y edges,
  vértices únicos y pares de aristas únicos ordenados lexicográficamente por nombre
  Unicode (aristas por origen y luego destino). --help explica el uso.
- **FR-005**: Resultados por stdout, errores por stderr sin traceback ni resultado
  parcial; éxito 0, lectura/formato 1, argumentos 2. Lectura/codificación usa
  Error: no se pudo leer ARCHIVO; estructura usa Error: línea N: DESCRIPCIÓN.
  La descripción explica encabezado, columnas, origen vacío o CSV inválido.
- **FR-006**: Cada escenario DEBE tener prueba automatizada trazable; validar los
  tres archivos originales sin modificarlos y comprobar canales y estados.

### Key Entities

- **Vértice**: nombre no vacío, recortado, sensible a mayúsculas.
- **Arista dirigida**: par origen-destino, único dentro del grafo.
- **Grafo**: vértices únicos y relaciones dirigidas, incluidos aislados y bucles.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Cada resultado incluye el 100 % de vértices y relaciones definidos.
- **SC-002**: Los tres archivos originales producen los resultados de AS-002 a AS-004.
- **SC-003**: El 100 % de los errores especificados respeta canales y estados,
  sin traceback ni salida parcial.

## Assumptions

Una invocación consulta un archivo local sin persistencia. Orden topológico y pesos
quedan fuera de esta feature. JSON es un contrato observable, no una representación
interna. Los nombres listados en escenarios denotan cadenas, no identificadores.
