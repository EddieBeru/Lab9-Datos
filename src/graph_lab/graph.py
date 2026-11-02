"""Representación propia de un grafo dirigido sin pesos."""


import heapq


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

    def topological_order(self) -> list[str]:
        """Kahn con el menor nombre disponible; no modifica el grafo."""
        indegree = {vertex: 0 for vertex in self.neighbors}
        for targets in self.neighbors.values():
            for target in targets:
                indegree[target] += 1
        available = [vertex for vertex, degree in indegree.items() if degree == 0]
        heapq.heapify(available)
        order = []
        while available:
            vertex = heapq.heappop(available)
            order.append(vertex)
            for target in self.neighbors[vertex]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    heapq.heappush(available, target)
        if len(order) != len(self.neighbors):
            raise ValueError('el grafo contiene un ciclo; no existe orden topológico')
        return order
