"""Lectura y validación del contrato CSV del laboratorio."""
import csv
from pathlib import Path

from .graph import Graph


def read_graph(path: str | Path) -> Graph:
    graph = Graph()
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.reader(stream, strict=True)
        try:
            if next(rows, None) != ['source', 'target']:
                raise ValueError('línea 1: encabezado esperado source,target')
            for row in rows:
                if row == []:
                    continue
                if len(row) != 2:
                    raise ValueError(f'línea {rows.line_num}: se requieren dos columnas')
                source, target = (name.strip() for name in row)
                if not source:
                    raise ValueError(f'línea {rows.line_num}: origen vacío')
                graph.add_vertex(source)
                if target:
                    graph.add_edge(source, target)
        except csv.Error as exc:
            raise ValueError(f'línea {rows.line_num}: CSV inválido') from exc
    return graph
