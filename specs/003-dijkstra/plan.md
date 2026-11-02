# Implementation Plan: Dijkstra

**Branch**: 003-dijkstra | **Date**: 2026-11-01 | **Spec**: [spec.md](spec.md)

## Summary

Implementar Dijkstra propio y lector ponderado separados, conservando Graph/reader
existentes. CLI añade shortest. Pesos enteros no negativos, sin dependencias runtime.

## Technical Context

Python >=3.11, csv/heapq/json estándar; pytest y NetworkX solo pruebas ya instalados.
Nueva WeightedGraph con dict[str,dict[str,int]]. Carga O(V+E), memoria O(V+E).
Dijkstra con entradas obsoletas: O((V+E) log(V+E)) como cota conservadora,
memoria adicional O(V+E). Reconstrucción de todas las rutas añade hasta O(V²)
de tiempo y salida. Sin objetivos artificiales de rendimiento ni pesos flotantes.

## Constitution Check

Antes/después del diseño: PASS. I: algoritmo propio, stdlib y representación
justificada en research.md. II: AS-301–306 con pytest y oráculo NetworkX en tests.
III: contrato shortest en spec y contracts/cli.md con estados 0/1/2.
IV: constitución 1.1.0, features 1/2 fusionadas antes de 003, fases en orden.
V: commits por fase, analyze antes de código, evidencia y revisión manual al cierre.
Alcance: solo Dijkstra aprobado; no expansión mínima ni cambio de CSV originales.

## Project Structure

Añadir src/graph_lab/weighted.py (modelo y algoritmo) y weighted_reader.py (lectura).
Modificar cli.py para despacho shortest. Tests: tests/test_shortest.py y
 tests/data/weighted.csv. Documentar uso y validación con datos ponderados y regresión.
Documentos de diseño: research.md, data-model.md, contracts/cli.md, quickstart.md.

## Complexity Tracking

Sin desviaciones. El modelo separado atiende un contrato diferente y evita reescribir
las dos features previas; no se añade herencia ni interfaces abstractas.
