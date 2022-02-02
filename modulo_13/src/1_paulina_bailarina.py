from collections import defaultdict
from queue import SimpleQueue


def INF():
    return "INF"


class graph:

    def __init__(self):
        self.graph = defaultdict(set)
        self.distances = defaultdict(INF)

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def bfs(self, a):
        visited = set()
        visited.add(a)

        q = SimpleQueue()
        q.put((a, 0))
        while not q.empty():
            u, dist = q.get()
            self.distances[u] = dist
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.put((v, dist + 1))


C = int(input())

for c in range(C):
    I, B = [int(x) for x in input().split(",")]
    g = graph()
    for b in range(B):
        a, b = [int(x) for x in input().split(" ")]
        g.add_edge(a, b)

    print("fiesta {}:".format(c + 1))
    g.bfs(0)
    for i in range(1, I):
        print(i, g.distances[i])
    print("")
