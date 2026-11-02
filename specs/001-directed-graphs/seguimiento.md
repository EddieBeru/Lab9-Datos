# Seguimiento factual de Feature 1

## Preparación

Repositorio independiente en lab9, rama base main. Material original reubicado
sin cambios de contenido, comprobado por SHA-256. No se importó el historial
ajeno del repositorio padre. Commit inicial: 3431ae8.
Constitución ejecutada y revisada en esta conversación; commit: d5a518c.
No existían especificaciones ni ramas previas de features en este repositorio.
No hay remoto configurado: se solicitó URL o nombre y visibilidad al usuario.

## Specify

Pendiente al inicio: no existía specs/001-*.
Se aplicó la habilidad Codex instalada speckit-specify con el prompt completo
de la sección 2 de docs/prompts/feature-1.md, conservado en prompt-specify.txt.
Se ejecutó resolve_template.py spec-template --json y se revisó su estructura;
se creó la rama 001-directed-graphs y el puntero local feature.json.
No hay extensions.yml ni hooks de especificación.
Se generaron spec.md y checklist; la revisión detectó tres grupos de decisiones
pendientes. No se afirma que estas decisiones estén acordadas.
Siguiente paso: commit de specify y aclaraciones de comportamiento.

## Estado de fases

| Fase | Estado | Evidencia |
| --- | --- | --- |
| Constitución | Completada | d5a518c, docs/constitucion.md |
| Specify | Borrador revisado | spec.md, checklist, prompt completo |
| Clarify | Pendiente | Políticas aún abiertas |
| Plan | Pendiente | Sin artefactos |
| Tasks | Pendiente | Sin artefactos |
| Analyze | Pendiente | Sin informe |
| Implement | Pendiente | Sin código ni pruebas |
| Validación | Pendiente | Sin ejecución de CLI |
| Commits | Parcial | Inicial y constitución guardados |
| Merge | Pendiente | Feature sin terminar |
| Push | Pendiente | Falta remoto |

## Clarify

Specify guardado en 977de19. Se ejecutó check_prerequisites.py --json --paths-only
y se leyó el prompt completo de la sección 4. La respuesta real del usuario
fue «todo eso recomendado»; se registró la decisión y se distinguieron las
recomendaciones delegadas de las preguntas históricas. Requisitos y escenarios
actualizados; revisión de checklist: 11/16 → 16/16. Sin hooks registrados.

## Plan

Se aplicó speckit-plan con el prompt íntegro de sección 5; setup_plan.py --json
resolvió y copió la plantilla. Investigación local delegada, diseño registrado
y revisión constitucional antes/después PASS. Sin hooks. No se creó aplicación.

## Tasks

Plan a996609. Se aplicó speckit-tasks con prompt completo de sección 6;
setup_tasks.py --json resolvió plantilla y documentos. Nueve tareas, todas
con ruta e ID, dos historias en secuencia y pruebas antes del código. Sin hooks.

## Analyze

Tasks 8623545. Análisis de solo lectura sobre esa revisión, informe emitido
en conversación y conservado posteriormente en analisis.md. CRITICAL/HIGH: 0.

## Corrección de especificación durante implement

Rojo: 24 fallos sobre paquete instalado. Primera implementación: 23 pasan,
1 falla por conteo incorrecto en AS-003. CSV inspeccionado: belt, jacket, pants,
shirt, shoes, socks, tie, undershorts, watch = 9 vértices. Se corrige primero spec;
la aplicación ya produce el resultado correcto. No se inventa un hallazgo de analyze:
este error fue descubierto por pruebas durante implement.
