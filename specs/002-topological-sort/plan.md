# Implementation Plan: Orden topológico

**Branch**: 002-topological-sort | **Date**: 2026-11-01 | **Spec**: [spec.md](spec.md)

## Summary

Añadir sort sobre lectura y representación de Feature 1 sin cambiar show.
Kahn propio con heap de nombres disponibles; sin orden parcial en ciclos.

## Technical Context

Python >=3.11, stdlib heapq. Runtime sin dependencias externas. pytest y NetworkX
solo en extra test; NetworkX se usa como oráculo independiente exigido por la guía.
Memoria O(V+E), tiempo O(E + V log V); grafo en dict[str,set[str]] existente.
Archivos locales, escala y requisitos iguales a Feature 1. No pesos.

## Constitution Check

Antes de investigación PASS; después del diseño PASS.

| Regla | Evidencia |
| --- | --- |
| I propia/simplicidad | Kahn propio, heapq no es biblioteca de grafos; misma representación |
| II pruebas | AS-201–207 en tests/test_sort.py, oráculo NetworkX solo tests |
| III consola | sort ARCHIVO, JSON order, estados y canales en contracts/cli.md |
| IV fases | Constitución d5a518c compartida; Feature 1 fusionada 849f29a; clarify ffccd8c |
| V evidencia | Fases separadas, suite/regresión y revisión manual antes del merge |
| Alcance/datos | Ciclos, bucles, aislados y duplicados explícitos, sin pesos |

## Project Structure

Documentos: spec.md, research.md, data-model.md, contracts/cli.md, quickstart.md,
tasks.md y evidencia de analyze, implementación y validación.
Modificar src/graph_lab/graph.py (topological_order), cli.py (sort) y pyproject.toml
(extra test NetworkX); añadir tests/test_sort.py y actualizar docs/USAGE.md.
Reader y show conservan su contrato. No crear servicios ni abstracciones adicionales.

## Complexity Tracking

Sin desviaciones constitucionales. Investigación local delegada conforme al skill.
