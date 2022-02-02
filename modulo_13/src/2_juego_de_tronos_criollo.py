from collections import defaultdict
from queue import SimpleQueue


class graph:

    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def bfs(self, a):
        self.visited.add(a)

        q = SimpleQueue()
        q.put(a)
        while not q.empty():
            u = q.get()
            yield u
            for v in self.graph[u]:
                if v not in self.visited:
                    self.visited.add(v)
                    q.put(v)

    def connected_components(self):
        c = 0
        biggest_c = 0

        for u in self.graph:
            if u not in self.visited:
                bfs = self.bfs(u)

                c += 1

                S = sum(1 for x in bfs)
                if biggest_c < S:
                    biggest_c = S

        return (c, biggest_c)


C = int(input())

for c in range(C):
    R = int(input())
    g = graph()
    for r in range(R):
        u, v = [int(x) for x in input().split()]
        g.add_edge(u, v)
    print(*g.connected_components())
