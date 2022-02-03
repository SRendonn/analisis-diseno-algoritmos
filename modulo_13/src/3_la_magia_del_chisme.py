from collections import defaultdict
from queue import SimpleQueue


class graph:

    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        self.days = defaultdict(lambda: 0)

    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def bfs(self, a):
        self.visited = set()
        self.days = defaultdict(lambda: 0)

        self.visited.add(a)

        q = SimpleQueue()
        q.put((0, a))
        while not q.empty():
            dia, u = q.get()
            self.days[dia] += 1
            for v in self.graph[u]:
                if v not in self.visited:
                    self.visited.add(v)
                    q.put((dia + 1, v))


P = int(input())

g = graph()
for p in range(P):
    line = [int(x) for x in input().split()]
    if line[0] == -1:
        continue
    for l in line:
        g.add_edge(p, l)
test_cases = [int(x) for x in input().split(", ")]

for tc in test_cases:
    g.bfs(tc)

    if len(g.days) == 1:
        print(0)
    else:
        best_day = 1
        most_gossip = 0
        for day in range(1, len(g.days)):
            if most_gossip < g.days[day]:
                most_gossip = g.days[day]
                best_day = day
        print(best_day, most_gossip)
