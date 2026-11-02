# Implementation Plan: Grafos dirigidos

**Branch**: 001-directed-graphs | **Date**: 2026-11-01 | **Spec**: [spec.md](spec.md)

## Summary

Cargar CSV validado completo y mostrar JSON estable, sin orden topológico ni pesos.

## Technical Context

Python >=3.11; biblioteca estándar csv, json, argparse, pathlib. Sin dependencias
runtime. Pruebas pytest; setuptools solo para empaquetar el paquete src/graph_lab.
Archivos locales UTF-8. Consola local; escala: archivos del laboratorio y casos límite,
sin objetivos artificiales de rendimiento. Carga O(V+E) esperado; salida ordenada
O(V log V + E log E); memoria O(V+E), además del resultado serializado.

## Constitution Check

Antes de investigación: PASS. Después de diseño: PASS.

| Regla | Evidencia de diseño |
| --- | --- |
| I: propia y simple | Graph con dict[str,set[str]], alternativas en research.md; solo stdlib |
| II: pruebas | AS-001–AS-009 cubiertas en tareas de pytest, CSV originales incluidos |
| III: consola | contracts/cli.md, salida y códigos de FR-004/005 |
| IV: fases | Constitución d5a518c; specify 977de19; clarify ee590de; sin código todavía |
| V: coherencia | Commits separados, analyze antes de implementar y validacion.md al cierre |
| Alcance y datos | Políticas explícitas en spec; sin pesos ni topológico |

## Project Structure

Documentación: spec.md, plan.md, research.md, data-model.md, contracts/cli.md,
quickstart.md, tasks.md, analisis.md, seguimiento.md, validacion.md.
Código previsto: src/graph_lab/{__init__,__main__,cli,reader,graph}.py.
Pruebas: tests/test_show.py, tests/test_reader.py; configuración en pyproject.toml.

Graph mantiene vértices y vecinos; reader valida y construye Graph o produce
ValueError con descripción para usuario; CLI convierte lectura y formato esperados
en errores stderr y serializa solo tras carga completa. argparse gestiona uso.
No se añaden capas de repositorio, persistencia ni interfaces abstractas.

## Complexity Tracking

Sin desviaciones. Investigación local delegada según speckit-plan; comparación
de tres representaciones registrada en research.md.
