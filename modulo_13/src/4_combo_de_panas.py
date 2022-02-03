graph = {}
stack = []
t = 0


def dfs1(u):
    global graph
    global stack
    global t

    node = graph[u]
    node['v2'] = True
    for v in node['adj2']:
        new_node = graph[v]
        if not new_node['v2']:
            dfs1(v)

    stack[t] = u
    t += 1


def dfs2(u):
    global graph

    node = graph[u]
    node['v'] = True
    for v in node['adj']:
        new_node = graph[v]
        if not new_node['v']:
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
        if not node['v2']:
            dfs1(u)

    scc = 0

    for u in reversed(stack):
        if not graph[u]['v']:
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
                "v": False,
                "adj": set(),
                "v2": False,
                "adj2": set()
            }
        if g.get(v) == None:
            g[v] = {
                'v': False,
                'adj': set(),
                'v2': False,
                'adj2': set()
            }

        g[u]['adj'].add(v)
        g[v]['adj2'].add(u)

    results.append(kosaraju(g))
    C = int(input())

for r in results:
    print(r)
