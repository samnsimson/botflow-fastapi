from typing import List, Dict


class Traverse:
    def dfs(self, graph: Dict[str, List], start_node: str, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        for neighbour in graph[start_node]:
            if neighbour not in visited:
                self.dfs(graph, neighbour, visited)
        return visited
