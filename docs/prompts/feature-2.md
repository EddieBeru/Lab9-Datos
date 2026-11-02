# Feature 2: Ordenamiento topológico

Guía autocontenida para el agente que ejecuta el laboratorio. Los bloques con `/speckit.*` invocan comandos del agente; los demás son prompts auxiliares, no comandos de terminal. Si la integración usa otra sintaxis, identifica su equivalente instalado sin inventarlo.

## Cómo recorrer esta guía

- Ejecuta los pasos en orden y retoma desde el primero pendiente. No vuelvas a crear una feature existente.
- Usa las instrucciones internas del laboratorio como autoridad sobre la documentación general de GitHub.
- Después de cada fase, revisa su resultado y ejecuta el prompt de commit de la sección 10 antes de pasar a la siguiente.
- El análisis es de solo lectura. Su evidencia se guarda después, en un paso auxiliar separado.
- Con autorización para ejecutar la guía completa, continúa sin pedir permiso entre fases. Espera las respuestas a decisiones de comportamiento y requisitos explícitos de aprobación del entorno; no las inventes.
- Mantén un registro factual en `specs/002-*/seguimiento.md` cuando exista la carpeta: fase, estado, evidencia, resultado y siguiente paso. No lo uses como sustituto de verificar los artefactos. Registra el hash del commit en la siguiente actualización para evitar modificar el registro tras cada commit.

## 0. Diagnóstico y preparación

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Lee los tres CSV de data/ línea por línea y anota lo inusual sin
decidir todavía su tratamiento. Revisa README.md y docs/APPROACH.md.

Identifica la raíz real del laboratorio y la raíz Git. Inspecciona
rama, remotos, worktree y commits sin tocar cambios ajenos. Si Git
abarca directorios superiores, limita todas las operaciones al lab.
No inicialices un repositorio anidado ni cambies su raíz en silencio.
Si esa estructura impide el flujo de ramas o la entrega, consúltalo.

Comprueba si Spec Kit está inicializado, si existe la constitución y
qué comandos ofrece la integración del agente. No reinstales ni
reinicialices una configuración válida. Si falta configuración,
identifica el agente disponible y el procedimiento compatible con
la versión instalada; configura solo lo necesario. No inventes flags
ni borres archivos existentes. Si no puedes invocar un comando, informa
el impedimento sin afirmar que lo ejecutaste.

Verifica que Feature 1 esté terminada y fusionada en main
antes de crear esta especificación. Busca specs/002-*/ y su rama.
Si no hay una feature existente, prepara main actualizado mediante
avance rápido cuando sea posible. No sobrescribas trabajo local.

Presenta una tabla de fases con estado, evidencia y pendientes:
constitución, specify, clarify, plan, tasks, analyze, implement,
validación, commits, merge y push. Distingue resultado existente de
ejecución históricamente comprobada.

Prepara la rama de la feature solo cuando corresponda. Si specify
instalado crea la rama, deja que lo haga; de lo contrario créala
conforme a las convenciones y numeración del lab. Evita ramas duplicadas
y confirma la ruta specs/002-*/ antes de continuar.

Este diagnóstico no inicia la implementación de la aplicación.
```

## 1. Comprobación de la constitución

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Lee la constitución vigente y contrástala con esta feature y las
restricciones del lab. No la recrees solo por empezar otra feature.

Si no requiere cambios, registra la comprobación y continúa. Si
requiere una enmienda, explica la necesidad; para modificar un principio
o comportamiento acordado, obtén la decisión del usuario. Después usa
/speckit.constitution con el contexto específico, actualiza los
documentos afectados y haz un commit separado de esa enmienda.
No debilites la prohibición de bibliotecas de grafos en la aplicación.
```

## 2. Specify

```text
/speckit.specify

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Extender la CLI existente para calcular un orden topológico: cada
vértice debe aparecer antes que todos los vértices a los que apunta.
Trabaja sobre la Feature 1 terminada y fusionada en main, no sobre
una implementación hipotética. Conserva su comportamiento acordado.

Genera o completa specs/002-*/spec.md y los checklists que correspondan,
sin duplicar una especificación válida. Usa el procedimiento instalado
de /speckit.specify y verifica la rama y numeración.

Describe qué puede hacer el usuario y qué resultados observa, sin
adelantar estructuras de datos, módulos ni decisiones de algoritmo que
pertenezcan a plan. Usa requisitos identificables, historias de usuario,
criterios de éxito y escenarios de aceptación verificables.

Incluye escenarios basados en los tres CSV cuando corresponda. Para el
extra, añade fixtures con pesos previstos en lugar de presuponer que los
CSV originales ya tengan ese formato. No alteres los datos originales.

Marca las decisiones de comportamiento pendientes para clarify; no
presentes suposiciones como respuestas del usuario. Revisa el checklist
de calidad y reporta brechas antes de continuar.

No avances automáticamente a plan: primero revisa la spec, registra
evidencia y ejecuta el commit de specify.
```

## 3. Revisión previa a clarify

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Revisa la especificación producida y los CSV. Enumera las preguntas
abiertas, incluidas las que no tengan marcador NEEDS CLARIFICATION.
Contrasta requisitos, escenarios, alcance y reglas del laboratorio.

Aclara integración con la CLI existente, dirección de las dependencias,
múltiples órdenes válidos, determinismo, componentes desconectados,
vértices aislados, grafo vacío, ciclos y autoaristas. Define cómo se
comunica la inexistencia de un orden, si se necesita identificar el
ciclo, si se permite salida parcial, y los códigos de retorno.

Si cambia comportamiento de la Feature 1, consulta la decisión y
actualiza primero la especificación afectada. No selecciones aquí
el algoritmo.

Separa lo ya decidido de lo pendiente. Usa esta lista para evaluar
después la cobertura de clarify. No implementes código ni conviertas
decisiones técnicas en requisitos de comportamiento.
```

## 4. Clarify

```text
/speckit.clarify

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Lee la spec activa y los CSV antes de formular preguntas. Contrasta
la lista de preguntas abiertas de la revisión anterior.

Aclara integración con la CLI existente, dirección de las dependencias,
múltiples órdenes válidos, determinismo, componentes desconectados,
vértices aislados, grafo vacío, ciclos y autoaristas. Define cómo se
comunica la inexistencia de un orden, si se necesita identificar el
ciclo, si se permite salida parcial, y los códigos de retorno.

Si cambia comportamiento de la Feature 1, consulta la decisión y
actualiza primero la especificación afectada. No selecciones aquí
el algoritmo.

Pregunta solo lo no resuelto, una pregunta por vez, con alternativas
concretas y recomendación justificada. Respeta los límites de la
versión instalada del comando. Espera mi respuesta antes de registrar
una elección; nunca inventes decisiones ni preguntas históricas.

Registra respuestas en Clarifications y propágalas a requisitos y
escenarios afectados. Revisa al terminar la lista inicial de brechas.
Si aún quedan decisiones importantes, informa cuáles y ejecuta otra
sesión enfocada del mismo comando respetando sus límites.

No continúes a plan con decisiones bloqueantes. Cuando la spec sea
coherente y revisada, ejecuta el commit de clarify.
```

## 5. Plan

```text
/speckit.plan

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Lee la spec aclarada, constitución, datos y código existente. Diseña
solo la feature activa. Si falta una decisión de comportamiento que
bloquea el diseño, vuelve a clarify sin inventarla.

Usa Python 3.11+ y algoritmos propios; prohíbe bibliotecas de grafos
en la aplicación, incluido graphlib. Respeta framework y estructura
acordados, y mantén la CLI proporcional al laboratorio.

Compara algoritmos de ordenamiento topológico y justifica la elección
según detección de ciclos, información de error y determinismo exigidos.
Explica complejidad temporal y espacial con la representación existente.
Evalúa si esta representación requiere cambios y registra por qué.

Usa una biblioteca de grafos como oráculo exclusivamente en pruebas.
Verifica que cada vértice aparezca una vez y que para cada arista
u -> v, u preceda a v. Compara secuencias exactas solo cuando la spec
lo exija. Contrasta también los casos sin orden y preserva regresiones
de la Feature 1.

Genera plan.md, research.md y data-model.md y los demás artefactos
aplicables del procedimiento instalado, como contratos y quickstart.
Si una plantilla omite research.md o data-model.md, complétalos con
contenido pertinente: son entregables internos obligatorios.

Documenta CLI, flujo de datos, errores y estrategia de pruebas para
todos los escenarios de aceptación. Completa la revisión constitucional.
No cambies requisitos silenciosamente ni implementes código.
Revisa los resultados y ejecuta el commit de plan antes de tasks.
```

## 6. Tasks

```text
/speckit.tasks

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Genera o actualiza tasks.md desde la spec aclarada y los artefactos
del plan, conforme al formato instalado de Spec Kit.

Cubre cada requisito funcional y cada escenario de aceptación con
tareas identificables. Incluye pruebas automatizadas antes del código
que verifican, dependencias, archivos afectados y resultado verificable.
Marca como paralelas solo tareas realmente independientes; esa marca
no autoriza por sí sola a delegar en otros agentes.

Incluye errores, casos especiales, ejecución de CLI y regresiones de
features existentes cuando correspondan. Mantén trazabilidad entre
requisitos, escenarios, pruebas y tareas. No añadas alcance nuevo.

Incluye la verificación manual con los datos aplicables y la ejecución
de toda la suite. Si faltan decisiones o diseño, vuelve al documento
de origen antes de crear tareas especulativas.
No implementes. Revisa cobertura y ejecuta el commit de tasks.
```

## 7. Analyze (solo lectura)

```text
/speckit.analyze

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Analiza constitución, spec.md, plan.md y tasks.md de la feature, usando
los artefactos complementarios y los datos como contexto.

Busca contradicciones, ambigüedades, duplicaciones, requisitos sin
tareas, escenarios sin pruebas, decisiones de Clarifications no
propagadas y desviaciones del alcance. Comprueba justificación del
diseño, contrato CLI y restricciones de bibliotecas.

Presenta hallazgos con ID, severidad, ubicación y corrección propuesta,
más cobertura y recomendación sobre si puede implementarse.

No modifiques ningún archivo durante este comando, ni siquiera el
registro de seguimiento. Devuelve el informe para conservarlo en el
paso auxiliar siguiente. No avances a implement con CRITICAL o HIGH
pendientes.
```

## 7.1. Conservar evidencia del análisis

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Fuera de /speckit.analyze, conserva su informe real más reciente en
specs/002-*/analisis.md, indicando alcance, fecha, hallazgos, cobertura
y revisión analizada. No inventes un informe si se perdió la salida:
vuelve a ejecutar analyze.

Si ya existe evidencia equivalente y vigente, no la dupliques.
Actualiza el registro factual y ejecuta el commit de analyze antes
de corregir documentos. Conserva el primer diagnóstico y sus
correcciones relevantes para REFLECTION.md, además del resultado final.
```

## 7.2. Corregir hallazgos y repetir el análisis

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Ejecuta este paso solo si existen hallazgos pendientes.

Corrige todos los CRITICAL y HIGH del último análisis en su documento
de origen. Actualiza o regenera los artefactos dependientes mediante
los comandos de Spec Kit que correspondan. Si hay una nueva decisión
de comportamiento, consulta al usuario y espera la respuesta.

No cambies código de aplicación antes de implement. No rebajes
severidades ni debilites la constitución para hacer pasar el análisis.

Revisa también los otros hallazgos: resuélvelos o documenta por qué no
bloquean. Registra correcciones y sus commits por fase afectada.
Después vuelve a ejecutar exactamente el prompt /speckit.analyze de
esta guía y conserva el nuevo resultado mediante el paso 7.1.

Repite hasta que no haya CRITICAL ni HIGH pendientes. Si un impedimento
externo bloquea el progreso, informa la causa y no repitas sin cambios.
```

## 8. Implement

```text
/speckit.implement

Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Comprueba que spec, plan y tasks estén completos y que el último
análisis corresponda a sus versiones vigentes y no tenga CRITICAL ni
HIGH pendientes. Revisa los checklists según el comando instalado.
No marques tareas como hechas solo porque ya aparezcan marcadas.

Implementa exclusivamente las tareas de esta feature y respeta sus
dependencias. Escribe y ejecuta las pruebas antes del código que
verifican, comprobando que el fallo inicial corresponda al comportamiento
ausente y no a un entorno roto. Implementa hasta hacerlas pasar.

No reescribas código ya correcto para recrear artificialmente un ciclo
de pruebas. Al retomar, verifica lo existente y completa solo pendientes.

Mantén bibliotecas de grafos exclusivamente en tests, si el plan usa
un oráculo. Actualiza tasks.md al completar realmente cada tarea.

Si hay discrepancias entre spec y código, identifica cuál está mal.
Actualiza primero los documentos cuando corresponda; si el cambio
requiere decidir un comportamiento nuevo, consulta antes de actuar.
Actualiza artefactos dependientes y repite analyze si los cambias.

Ejecuta las pruebas pertinentes y toda la suite. No ocultes fallos ni
declares comprobaciones que no ejecutaste. Revisa los cambios y haz
el commit de implement. No hagas merge ni inicies otra feature dentro
de este comando; usa los siguientes pasos de la guía.
```

## 9. Validación y aceptación

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Prioriza README.md y docs/APPROACH.md, después la constitución y las
decisiones aprobadas de la feature. Si se contradicen, informa el
conflicto y pide la decisión necesaria; no cambies acuerdos en silencio.
La documentación general de GitHub Spec Kit es referencia secundaria.
Usa los comandos instalados de Spec Kit y respeta su procedimiento
compatible con el laboratorio. No simules su ejecución.

Verifica la implementación real contra cada requisito y escenario,
no solo que tasks.md tenga casillas marcadas. Ejecuta toda la suite y
los comandos documentados de instalación y uso en un entorno adecuado.
No introduzcas dependencias de grafos en tiempo de ejecución.

Ejecuta el ordenamiento con los tres CSV originales y compara éxito,
errores y salida con la especificación. Comprueba con el oráculo que
los órdenes sean válidos y que los casos sin orden se detecten.
Ejecuta también la carga y visualización de Feature 1 y toda su suite.

Registra comandos exactos, resultados, códigos de retorno y casos
cubiertos en specs/002-*/validacion.md, sin incluir datos sensibles.
Una validación antigua no basta si cambiaron código, dependencias o
datos relevantes desde entonces.

Comprueba que existan spec.md con Clarifications, plan.md, research.md,
data-model.md, tasks.md y los demás artefactos generados pertinentes.
Verifica que no queden tareas incompletas ni decisiones bloqueantes.

Si falla algo, corrige primero el documento de origen cuando sea
necesario y luego la implementación; actualiza tareas, repite analyze
si cambian sus entradas, y vuelve a ejecutar las verificaciones
afectadas. No marques la feature como aceptada mientras haya fallos.

Conserva evidencia útil para la reflexión: decisiones, anomalías de los
datos, alternativas de diseño y hallazgos corregidos. No inventes la
experiencia personal del estudiante. Haz commit de las correcciones
y de la evidencia de validación antes del merge.
```

## 10. Commit de cada fase (reutilizable)

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Revisa si esta fase ya tiene un commit correspondiente. Si lo tiene
y no hay cambios nuevos propios de la fase, no crees otro.

Si falta, revisa el diff y crea un commit identificando feature y fase,
incluyendo exclusivamente sus archivos. Usa rutas explícitas, nunca
git add . ni git add -A desde una raíz que incluya trabajos ajenos.
Si una fase de solo lectura no dejó cambios, conserva su informe real
como evidencia antes del commit. No fabriques evidencia de ejecuciones
pasadas ni reescribas la historia para aparentar commits por fase.

No incluyas secretos, archivos generados innecesarios ni cambios ajenos.
No hagas push ni merge en este paso. Informa el hash y las rutas incluidas.
Si el historial ya agrupó varias fases, reporta el incumplimiento;
no lo ocultes con commits vacíos.
```

## 11. Fusionar y publicar la feature

```text
Antes de actuar, revisa esta fase en los artefactos, rama activa e
historial de Git. Clasifícala como completada, parcial, pendiente o
no verificable y cita evidencia. Un archivo existente no prueba que
el comando se ejecutó ni que la fase esté completa. Si está completa
y vigente, omítela; si es parcial, termina solo lo pendiente. Si no
es verificable, explica qué evidencia falta antes de regenerar.
Comprueba si cambios anteriores invalidaron sus resultados.

Comprueba aceptación, suite, evidencia y commits de esta feature.
Identifica rama, main y remoto reales. No fusiones una feature
incompleta ni incluyas cambios ajenos.

Comprueba si la rama ya fue fusionada mediante historial y contenido;
si lo fue, no repitas el merge. Si está pendiente, integra en main
preservando los commits de cada fase: no uses squash ni reescribas
historial. No borres las ramas del laboratorio.

Antes de cambiar de rama, protege el trabajo existente sin descartarlo
ni guardarlo automáticamente con cambios ajenos. Actualiza main por
avance rápido cuando sea posible. Resuelve conflictos rutinarios
conservando los contratos; pregunta si hay una decisión de comportamiento.
Verifica de nuevo la suite sobre el resultado del merge.

Publica mediante push normal main y esta rama de feature en el remoto
correcto. Comprueba primero si ya están publicadas y sincronizadas.
Publica las ramas del laboratorio mediante nombres explícitos, no
todas las ramas de un repositorio superior. No uses force push.
Si falta remoto, autenticación o acceso de escritura, informa el
impedimento y solicita solo el dato o permiso necesario.

Informa hashes, ramas y resultado de pruebas tras la fusión. Confirma
que la siguiente feature podrá partir de main con esta ya integrada.
```

## Resultado y siguiente paso

La feature termina cuando sus documentos, código y pruebas concuerdan, no quedan hallazgos bloqueantes, existen los commits requeridos y su rama está fusionada y publicada. Un push bloqueado debe quedar como pendiente explícito, nunca como realizado.

Si vas a realizar el extra, continúa con [Feature 3](feature-3-extra.md). Si no, pasa al [cierre](cierre-proyecto.md).

## Fuentes

- [Requisitos del laboratorio](../../README.md).
- [Guía interna del proceso](../APPROACH.md).
- [GitHub Spec Kit](https://github.github.com/spec-kit/), referencia secundaria; los comandos disponibles dependen de la integración instalada.

