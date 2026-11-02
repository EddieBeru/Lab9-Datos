# Cierre del proyecto y ejecución completa

El laboratorio exige completar y fusionar las Features 1 y 2. La Feature 3 es opcional. No exige un comando adicional de Spec Kit para cerrar: estos prompts auxiliares comprueban entregables, reflexión y publicación. No sustituyen las fases obligatorias de cada feature.

## Instrucciones para poner todo en marcha

1. Abre con el otro agente la raíz de este laboratorio, donde están `README.md`, `docs/` y `data/`.
2. Comprueba que puede leer estos cuatro MD y que su integración de Spec Kit está disponible. El diagnóstico de Feature 1 cubre la configuración faltante.
3. Pega el prompt de arranque siguiente. Si ya sabes qué extra quieres, añade esa decisión al final; si no quieres el extra, indícalo.
4. Responde las preguntas de comportamiento y de reflexión cuando aparezcan. El agente continúa el resto del trabajo autorizado sin confirmaciones entre fases.
5. Si la herramienta no puede encadenar comandos, envía el bloque completo del siguiente paso pendiente con la sintaxis de su integración. Los `/speckit.*` son comandos del agente, no del shell.

## Prompt de arranque: ejecutar todas las guías

```text
Actúa como el agente ejecutor de este laboratorio. Recorre estas guías:
1. docs/prompts/feature-1.md
2. docs/prompts/feature-2.md
3. docs/prompts/feature-3-extra.md, solo si se acuerda realizar el extra.
4. docs/prompts/cierre-proyecto.md

Lee primero README.md y docs/APPROACH.md. Sus instrucciones tienen
prioridad sobre la documentación general de GitHub Spec Kit. Respeta
la constitución y las decisiones aprobadas; si chocan con el lab,
expón el conflicto antes de cambiar acuerdos.

Te autorizo a ejecutar el flujo completo descrito en esas guías:
preparación, documentos, pruebas, código, commits por fase, fusiones
y pushes normales de las ramas del laboratorio. No me pidas permiso
para pasar de una fase a otra ni te detengas solo para entregar un plan.

Antes de cada fase, realiza la verificación previa indicada en su MD.
Revisa artefactos, contenido, historial, rama y vigencia. No repitas
trabajo completo ni crees features duplicadas. Distingue entre resultado
existente y comando cuya ejecución esté comprobada; no inventes evidencia.

Invoca realmente cada comando de Spec Kit pendiente con el prompt
completo de su guía y mediante la sintaxis admitida por tu integración.
No basta con escribir su nombre, resumirlo o generar documentos por
tu cuenta para afirmar que lo ejecutaste. Si no puedes invocarlo,
indica el impedimento y la solución necesaria; no simules su ejecución.

Ejecuta una fase a la vez, revisa su resultado y crea el commit de esa
fase antes de continuar. analyze es de solo lectura: conserva su
informe en el paso auxiliar posterior y corrige fuera del comando.
Resuelve CRITICAL y HIGH y repite analyze antes de implementar.
Si un cambio invalida fases posteriores, actualízalas y verifícalas.

Continúa automáticamente en el trabajo autorizado, pero espera mis
respuestas cuando clarify requiera decisiones de comportamiento que
no estén acordadas. No inventes mis respuestas ni mis experiencias
para REFLECTION.md. Formula las preguntas en el formato y con los
límites que exija el comando. Pregunta si se realizará el extra y
qué alternativa, salvo que ya exista una decisión explícita.

Respeta las aprobaciones técnicas exigidas por el entorno. No
descartes cambios ajenos, no reescribas historial ni uses force push.
Si la raíz Git incluye otras carpetas, limita rutas y ramas al lab.
No hagas pushes globales de todas las ramas de ese repositorio.

No inicies Feature 2 antes de terminar y fusionar Feature 1 en main.
Haz lo mismo antes del extra. Si se omite el extra, pasa al cierre.

Mantén evidencia factual del progreso en los archivos de seguimiento
de las guías y da actualizaciones breves al cambiar de fase. Cuando
necesites mi respuesta, indica la pregunta y qué queda pendiente;
retoma al recibirla sin perder el objetivo.

Termina con la auditoría de cierre, pruebas, REFLECTION.md, commits,
publicación y enlace de entrega. Informa los resultados reales y
cualquier impedimento pendiente. No declares el proyecto terminado
mientras falten requisitos obligatorios.
```

## Recorrido del cierre

Ejecuta los siguientes pasos después de las features. Las instrucciones internas del laboratorio prevalecen sobre la documentación general de GitHub. Verifica cada paso antes de repetirlo y conserva evidencia factual en `docs/cierre.md`. Un informe de cierre ya existente no demuestra que la suite siga pasando. No vuelvas a ejecutar el prompt de arranque desde dentro del cierre.

## 1. Auditar entregables y proceso

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

Lee README.md, docs/APPROACH.md, constitución, especificaciones,
registros de análisis y validaciones de las features realizadas.

Comprueba:
- .specify/memory/constitution.md completo.
- specs/001-*/ y specs/002-*/ con spec.md, Clarifications, plan.md,
  research.md, data-model.md, tasks.md y demás archivos generados.
- Si se hizo el extra, los mismos artefactos de specs/003-*/.
- CLI funcional y pruebas de cada escenario de aceptación.
- Coherencia entre decisiones, requisitos, diseño, código y pruebas.
- Evidencia de cada fase y commits separados, incluyendo analyze.
- Features terminadas y fusionadas en main, sin borrar sus ramas.

Distingue contenido existente de comandos históricamente comprobados.
No fabriques preguntas, respuestas, informes ni commits retrospectivos.
No reescribas el historial para aparentar el proceso. Si falta evidencia
histórica irrecuperable, repórtala como tal.

Guarda la auditoría factual en docs/cierre.md con estado por entregable,
evidencia, pendientes y siguiente acción. Si el extra no se realizó,
márcalo como no aplicable: no bloquea la entrega obligatoria.
```

## 2. Resolver pendientes y volver a analizar si corresponde

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

A partir de la auditoría, completa cada pendiente en su fase y
feature de origen usando el prompt correspondiente de su guía.

Si cambia comportamiento, pregunta lo no acordado y actualiza primero
la especificación. Si cambian spec, plan o tasks, revisa los artefactos
dependientes, repite /speckit.analyze y resuelve CRITICAL y HIGH antes
de continuar la implementación. Conserva el informe fuera de analyze.

Si los cambios son de una feature ya fusionada, usa una rama de
corrección propia y conserva el historial de las ramas originales.
Haz commits identificables por fase afectada, verifica y fusiona
la corrección sin squash. No crees otra feature numerada por un arreglo.

No inventes tareas para aparentar trabajo ni marques pendientes como
completos sin comprobarlos. Actualiza la auditoría con evidencia real.
```

## 3. Verificación final sobre main

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

Comprueba que main incluya las features realizadas y sus correcciones.
Ejecuta el procedimiento documentado de instalación y la suite completa
con Python 3.11+ en un entorno adecuado. Revisa que bibliotecas de grafos
sean exclusivamente dependencias y herramientas de pruebas, no parte
del código de aplicación.

Ejecuta la CLI para cargar y mostrar los tres CSV originales y para
ordenarlos topológicamente según sus especificaciones. Comprueba
resultados, errores y códigos de retorno. No presupongas que los tres
deban producir éxito. Si se hizo el extra, ejecuta también fixtures
con pesos y las comprobaciones de oráculo correspondientes.

Comprueba cobertura de todos los escenarios de aceptación y las
regresiones. Verifica que las instrucciones de uso funcionen tal
como están escritas y que no dependan de rutas locales del agente.

Registra comandos, versiones relevantes, resultados, códigos de
retorno y limitaciones en docs/cierre.md. No declares pruebas ejecutadas
si solo las inspeccionaste. Corrige fallos y repite las verificaciones
afectadas hasta que pasen o informa el impedimento real.
```

## 4. Preparar REFLECTION.md sin inventar experiencias

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

Crea o completa REFLECTION.md con extensión aproximada de 1–2 páginas,
respondiendo todas las preguntas del README:

1. Agente usado, qué ayudó y qué dificultó el trabajo.
2. Preguntas de clarificación y decisiones de cada feature; cuál fue
   la decisión más difícil y por qué.
3. Particularidades de los CSV y tratamiento de cada una.
4. Representación del grafo, alternativas rechazadas y si se sostuvo
   al implementar Feature 2 o tuvo que cambiar.
5. Qué reportó analyze en cada feature y qué se corrigió.
6. Un momento en que el agente hizo algo diferente de lo esperado:
   si la causa fue ambigüedad de la spec o ignorar sus instrucciones.

Usa artefactos, historial y resultados reales para los hechos
verificables. Si se hizo el extra, incorpora su experiencia relevante.

Para las valoraciones personales y experiencias que no consten,
pregunta al estudiante en una sola consulta concisa y espera su
respuesta. No inventes anécdotas, dificultades ni preferencias.
Si no recuerda un incidente, registra su respuesta honesta sin
fabricar uno y señala la limitación frente al requisito del README.

Un borrador con preguntas pendientes no cuenta como reflexión completa.
Contrasta la versión final con la evidencia y conserva la voz del autor.
```

## 5. Commit final y revisión de archivos

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

Revisa el diff y la auditoría. Confirma que las correcciones ya tengan
los commits correspondientes y que REFLECTION.md esté completa.

Antes de añadir archivos, inspecciona su contenido para evitar
publicar secretos, credenciales, entornos virtuales, caches o
artefactos innecesarios. No imprimas valores sensibles al informar.
Respeta cambios ajenos y usa rutas explícitas dentro del laboratorio.

Si los documentos finales tienen cambios, crea el commit de cierre;
si ya están comprometidos y vigentes, no crees otro. El commit final
no reemplaza los commits por fase de cada feature.

Confirma que no queden cambios propios sin guardar ni pendientes
obligatorios. Si solo cambió documentación de cierre después de la
suite, no la repitas sin motivo; si cambió código o configuración
relevante, vuelve al paso de verificación.
```

## 6. Publicar ramas y confirmar entrega

```text
Antes de actuar, revisa los artefactos, rama activa e historial de
Git. Clasifica este paso como completado, parcial, pendiente o no
verificable y cita evidencia. No asumas ejecución histórica por la
existencia de un archivo. Omite lo completado y vigente, completa
solo lo pendiente y explica la evidencia que falte antes de regenerar.
Si cambió lo relevante desde la última verificación, vuelve a validarlo.

Identifica el remoto real y las ramas de main y de todas las features
realizadas. Comprueba con el historial qué commits faltan en el remoto.

Publica main, ramas de features y ramas de corrección del laboratorio
mediante nombres explícitos y push normal. No uses force push ni
push global de todas las ramas si el repositorio incluye otros
trabajos. Si ya están sincronizadas, no repitas operaciones innecesarias.

Confirma que las features estén fusionadas en main y que sus ramas
permanezcan publicadas. No hagas squash ni elimines evidencia del proceso.

Si faltan remoto, autenticación o permisos, informa el impedimento
y pide solo el dato o permiso necesario. No marques publicación como
completada cuando falle. Comprueba que el enlace de entrega apunta al
repositorio y a la ubicación correcta del lab si es un monorepositorio.

Entrega un informe breve con:
- Enlace del repositorio y ruta del laboratorio cuando corresponda.
- Features realizadas y situación del extra.
- Suite y verificaciones manuales con sus resultados reales.
- Ubicación de REFLECTION.md y los artefactos obligatorios.
- Estado de ramas, fusiones y publicación.
- Cualquier pendiente o limitación de evidencia histórica.

Declara el proyecto terminado solo si los requisitos obligatorios
están satisfechos; distingue un bloqueo de publicación de trabajo local
ya completado.
```

## Fuentes y navegación

- [Requisitos del laboratorio](../../README.md) y [guía interna](../APPROACH.md): autoridad para el trabajo.
- [Feature 1](feature-1.md), [Feature 2](feature-2.md), [extra](feature-3-extra.md).
- [GitHub Spec Kit](https://github.github.com/spec-kit/): referencia secundaria. No agregues fases nuevas únicamente porque una versión reciente las ofrezca; cumple primero el flujo exigido por el laboratorio.

