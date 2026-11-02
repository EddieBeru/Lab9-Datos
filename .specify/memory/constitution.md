# Constitución del laboratorio de grafos

## Principios fundamentales

### I. Implementación propia y simplicidad

La aplicación DEBE usar Python 3.11 o superior, con un paquete pequeño en `src/graph_lab/`
y pruebas en `tests/`. DEBE separar las responsabilidades de CLI, lectura de archivos y
operaciones del grafo. El proyecto DEBE implementar su grafo y sus algoritmos.
Se PROHÍBE usar bibliotecas de grafos en el código de aplicación, incluidas NetworkX,
igraph, graph-tool, `graphlib` y `scipy.sparse.csgraph`; únicamente se permiten en pruebas
como oráculos, sin convertirse en dependencias de ejecución.

Cada plan DEBE justificar la representación del grafo y documentar en `research.md` las
alternativas descartadas y sus costes para las operaciones requeridas. La constitución no
elige representación ni algoritmo topológico. Cada dependencia añadida y abstracción DEBE
responder a una necesidad concreta de las funcionalidades actuales y justificarse en el plan;
se DEBE mantener el mínimo necesario para evitar complejidad sin utilidad verificable.

### II. Pruebas trazables

Cada escenario de aceptación DEBE tener al menos una prueba automatizada con pytest,
identificable mediante una referencia entre escenario y prueba. Las pruebas DEBEN verificar
comportamiento observable, entradas válidas, casos límite y errores definidos en la
especificación. Los tres archivos proporcionados DEBEN participar en la validación de cada
funcionalidad, con resultados esperados derivados de su especificación.

Las pruebas de orden topológico DEBEN comprobar que aparecen todos los vértices exactamente
una vez y que cada arista respeta la precedencia requerida. No DEBEN asumir una única
respuesta salvo que la especificación exija un orden determinista. También DEBEN comprobar
el comportamiento especificado cuando no existe orden topológico. Las tareas de pruebas
DEBEN preceder a la implementación correspondiente; las pruebas no son opcionales.

### III. Contrato de consola

La aplicación DEBE ejecutarse mediante `python -m graph_lab`. Los resultados DEBEN ir a
stdout y los errores a stderr. Ante un error, el proceso DEBE terminar con un código distinto
de cero; los errores esperados del usuario NO DEBEN mostrar traceback. Las especificaciones
DEBEN definir los subcomandos, mensajes concretos y códigos específicos, y sus pruebas DEBEN
verificar los canales de salida y el estado de terminación correspondientes.

### IV. Desarrollo guiado por especificaciones

Se DEBE seguir la secuencia constitución → specify → clarify → plan → tasks → analyze →
implement. La constitución es compartida y se redacta una vez, con enmiendas cuando proceda;
cada funcionalidad DEBE recorrer las fases restantes en su propia rama. La segunda
funcionalidad solo DEBE especificarse después de terminar y fusionar la primera.

Las especificaciones DEBEN describir comportamiento observable; los planes DEBEN contener
las decisiones técnicas. Toda aclaración DEBE reflejarse tanto en los requisitos y escenarios
de aceptación afectados como en la sección `Clarifications`. Antes de implementar se DEBEN
resolver todos los hallazgos CRITICAL y HIGH de analyze en los documentos correspondientes,
actualizar los documentos dependientes y repetir el análisis para confirmar su resolución.
Ningún flujo abreviado de herramientas permite omitir estas fases.

### V. Coherencia y evidencia del proceso

Ante discrepancias entre especificación y código, se DEBE determinar y registrar cuál es
incorrecto. Cuando corresponda cambiar el comportamiento especificado, se DEBE actualizar
primero la especificación y sus documentos dependientes, y después el código y las pruebas.
Nunca se DEBE cerrar una funcionalidad con discrepancias pendientes.

El historial DEBE contener al menos un commit por fase de cada funcionalidad; la adopción
constitucional compartida DEBE quedar referenciada en ambas. Esta regla no autoriza al agente
a crear commits ni publicar cambios sin autorización explícita. Al terminar cada funcionalidad
se DEBE revisar manualmente la CLI con los tres archivos y contrastar los resultados con sus
escenarios. Se DEBEN registrar decisiones y resultados para `REFLECTION.md`, incluido el
agente utilizado, aclaraciones y motivos, anomalías, alternativas técnicas, hallazgos de
analyze y correcciones, y diferencias entre la intención y lo producido por el agente.
Se PROHÍBE incorporar secretos a los archivos o al historial del proyecto.

## Alcance y datos

La primera funcionalidad carga y muestra grafos dirigidos sin pesos; la segunda añade un
orden topológico sobre la primera ya terminada y fusionada. La tercera funcionalidad, aprobada explícitamente por el usuario, añade grafos
ponderados y caminos mínimos con Dijkstra. No incluye árboles de expansión mínima.
Los contratos sin pesos de las dos primeras funcionalidades DEBEN conservarse.

El material del laboratorio está en la raíz de su repositorio independiente:
`README.md`, `docs/APPROACH.md` y `data/` son las referencias existentes; la instalación
de Spec Kit se encuentra en esa misma raíz. No se DEBEN duplicar ni alterar los datos
para ocultar casos que requieren una decisión explícita.

Las especificaciones DEBEN definir y probar el tratamiento de estas situaciones en las
operaciones de cada funcionalidad:

- `cs-curriculum.csv`: arista `Data Structures,Algorithms` duplicada en las líneas 11 y 25.
- `small-dag.csv`: fila `watch,` con destino vacío en la línea 11.
- `build-with-cycle.csv`: ciclo auth → session → user-profile → auth en las líneas 8–10.
- `build-with-cycle.csv`: bucle metrics → metrics en la línea 14.

Esta constitución no establece su aceptación, rechazo, normalización ni representación.
Esas decisiones DEBEN quedar explícitas en requisitos, escenarios y pruebas de las
especificaciones correspondientes, sin anticipar la especificación de la segunda funcionalidad.

## Revisión y evidencia

Cada `plan.md` DEBE completar `Constitution Check` antes de la investigación y revisarlo
tras el diseño, con evidencia o referencias para cada uno de los cinco principios, el alcance
y las decisiones pendientes sobre los datos. DEBE comprobar versión de Python, estructura,
separación de responsabilidades, dependencias, alternativas de representación, trazabilidad
de pruebas, contrato de consola, secuencia de fases y evidencia prevista de validación.

Cada funcionalidad DEBE conservar `spec.md`, `plan.md`, `research.md`, `data-model.md` y
`tasks.md`, además de los documentos generados que correspondan. Las tareas DEBEN cubrir
los requisitos y escenarios e incluir pruebas obligatorias con pytest. El cierre DEBE
registrar comandos realmente ejecutados, resultados, revisión manual de los tres archivos y
hallazgos resueltos. No se DEBE afirmar que una prueba o revisión se ejecutó sin evidencia.

## Gobernanza

Esta constitución prevalece sobre ejemplos y recomendaciones genéricas de las herramientas.
En particular, las menciones genéricas a pruebas opcionales no se aplican a este laboratorio.
Un plan no puede dispensar una prohibición constitucional mediante una justificación de
complejidad: una excepción requiere una enmienda explícita previa.

Para modificarla se DEBE documentar el motivo, las reglas afectadas, las consecuencias y,
cuando corresponda, la transición necesaria; obtener aprobación explícita del responsable
del proyecto y revisar especificaciones, planes, tareas, pruebas, plantillas y comandos
afectados. Se DEBEN sincronizar únicamente los documentos que necesiten cambios y generar
el informe de sincronización exigido por el flujo de constitución instalado.

La versión DEBE seguir MAJOR.MINOR.PATCH: MAJOR para eliminar o redefinir reglas de forma
incompatible; MINOR para añadir principios o ampliar materialmente obligaciones; PATCH para
aclaraciones sin cambio normativo. Cada enmienda DEBE actualizar versión y fecha de última
modificación en formato ISO, preservando la fecha original de ratificación. La versión 1.0.0
representa la adopción inicial de estas reglas.

Cada plan y revisión de cierre DEBE comprobar cumplimiento y registrar desviaciones;
las desviaciones constitucionales DEBEN corregirse antes de implementar o cerrar la
funcionalidad, según corresponda.

**Versión**: 1.1.0 | **Ratificación**: 2026-11-01 | **Última modificación**: 2026-11-01
