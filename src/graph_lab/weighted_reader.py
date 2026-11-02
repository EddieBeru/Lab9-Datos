"""Lector del contrato CSV ponderado, separado del formato original."""
import csv
from pathlib import Path

from .weighted import WeightedGraph


def read_weighted_graph(path):
    graph = WeightedGraph()
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.reader(stream, strict=True)
        try:
            if next(rows, None) != ['source', 'target', 'weight']:
                raise ValueError('línea 1: encabezado esperado source,target,weight')
            for row in rows:
                if row == []:
                    continue
                prefix = f'línea {rows.line_num}: '
                if len(row) != 3:
                    raise ValueError(prefix + 'se requieren tres columnas')
                source, target, weight = (field.strip() for field in row)
                if not source:
                    raise ValueError(prefix + 'origen vacío')
                graph.add_vertex(source)
                if not target:
                    if weight:
                        raise ValueError(prefix + 'aislado requiere peso vacío')
                    continue
                if not weight or any(c not in '0123456789' for c in weight):
                    raise ValueError(prefix + 'peso debe ser entero no negativo')
                try:
                    value = int(weight)
                except ValueError as exc:
                    raise ValueError(prefix + 'peso entero fuera del límite admitido') from exc
                graph.add_edge(source, target, value)
        except csv.Error as exc:
            raise ValueError(f'línea {rows.line_num}: CSV inválido') from exc
    return graph
