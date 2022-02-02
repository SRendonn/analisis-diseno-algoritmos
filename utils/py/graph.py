from collections import defaultdict
from queue import SimpleQueue


class graph:

    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def dfs(self, a):
        visited = set()

        stack = [a]

        while len(stack):
            u = stack.pop()
            if u not in visited:
                yield u
                visited.add(u)
                for v in self.graph[u]:
                    stack.append(v)

    def bfs(self, a):
        visited = set()
        visited.add(a)

        q = SimpleQueue()
        q.put(a)
        while not q.empty():
            u = q.get()
            yield u
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.put(v)
