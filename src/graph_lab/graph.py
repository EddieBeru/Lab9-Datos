"""Representación propia de un grafo dirigido sin pesos."""


class Graph:
    def __init__(self):
        self.neighbors: dict[str, set[str]] = {}

    def add_vertex(self, name: str):
        self.neighbors.setdefault(name, set())

    def add_edge(self, source: str, target: str):
        self.add_vertex(source)
        self.add_vertex(target)
        self.neighbors[source].add(target)

    def as_dict(self):
        return {
            'vertices': sorted(self.neighbors),
            'edges': [[source, target] for source in sorted(self.neighbors)
                      for target in sorted(self.neighbors[source])],
        }
