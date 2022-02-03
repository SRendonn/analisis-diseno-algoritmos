graph = {}
stack = []
t = 0


def dfs1(u):
    global graph
    global stack
    global t

    node = graph[u]
    node['explored2'] = True
    for v in node['adjacent2']:
        new_node = graph[v]
        if not new_node['explored2']:
            dfs1(v)

    stack[t] = u
    t += 1


def dfs2(u):
    global graph

    node = graph[u]
    node['explored'] = True
    for v in node['adjacent']:
        new_node = graph[v]
        if not new_node['explored']:
            dfs2(v)


def kosaraju(g):
    global graph
    global stack
    global t

    graph = g
    stack = [None for _ in range(len(graph))]
    t = 0

    for u in graph:
        node = graph[u]
        if not node['explored2']:
            dfs1(u)

    scc = 0
    stack.reverse()

    for u in stack:
        if not graph[u]['explored']:
            dfs2(u)
            scc += 1
    return scc


C = int(input())
results = []
while C:
    g = {}
    for c in range(C):
        u, v = input().split()

        if g.get(u) == None:
            g[u] = {
                "explored": False,
                "adjacent": set(),
                "explored2": False,
                "adjacent2": set()
            }
        if g.get(v) == None:
            g[v] = {
                'explored': False,
                'adjacent': set(),
                'explored2': False,
                'adjacent2': set()
            }

        g[u]['adjacent'].add(v)
        g[v]['adjacent2'].add(u)

    results.append(kosaraju(g))
    C = int(input())

for r in results:
    print(r)
