"""Grafo ponderado propio y caminos mínimos de Dijkstra."""
import heapq


class WeightedGraph:
    def __init__(self):
        self.neighbors: dict[str, dict[str, int]] = {}

    def add_vertex(self, name):
        self.neighbors.setdefault(name, {})

    def add_edge(self, source, target, weight):
        self.add_vertex(source)
        self.add_vertex(target)
        old = self.neighbors[source].get(target)
        self.neighbors[source][target] = weight if old is None else min(old, weight)

    def shortest_paths(self, source):
        if source not in self.neighbors:
            raise ValueError(f'origen inexistente: {source}')
        distances = {source: 0}
        previous = {}
        pending = [(0, source)]
        while pending:
            distance, vertex = heapq.heappop(pending)
            if distance != distances[vertex]:
                continue
            for target, weight in self.neighbors[vertex].items():
                candidate = distance + weight
                if target not in distances or candidate < distances[target]:
                    distances[target] = candidate
                    previous[target] = vertex
                    heapq.heappush(pending, (candidate, target))
        paths = {}
        for target in sorted(self.neighbors):
            if target not in distances:
                paths[target] = None
                continue
            path = [target]
            while path[-1] != source:
                path.append(previous[path[-1]])
            paths[target] = list(reversed(path))
        return {'distances': {v: distances.get(v) for v in sorted(self.neighbors)},
                'paths': paths}
