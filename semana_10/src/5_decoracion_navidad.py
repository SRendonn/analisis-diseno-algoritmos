from math import inf


def arbolizacion(i, j, level, S, items):

    res = ""
    node = S[i][j]

    if node < j:
        res += arbolizacion(node + 1, j, level + 1, S, items)

    res += '\t'*level
    res += items[node][0]
    res += '\n'

    if node > i:
        res += arbolizacion(i, node - 1, level + 1, S, items)
    return res


def get_tree(items):
    N = len(tree_lights)

    C = [[0 for x in range(N)] for y in range(N)]
    S = [[0 for x in range(N)] for y in range(N)]
    sumP = [[0 for x in range(N)] for y in range(N)]

    for i in range(N):
        suma = 0
        C[i][i] = items[i][1]
        for j in range(i, N):
            suma += items[j][1]
            sumP[i][j] = suma
    for nodos in range(1, N + 1):
        for i in range(N - nodos + 1):
            j = i + nodos - 1
            menor = inf
            for r in range(i, j + 1):
                Q = 0
                if N == 1:
                    Q = sumP[i][j]
                elif r == 0:
                    Q = C[r + 1][j] + sumP[i][j]
                elif r == N - 1:
                    Q = C[i][r - 1] + sumP[i][j]
                else:
                    Q = C[i][r - 1] + C[r + 1][j] + sumP[i][j]

                if (Q < menor):
                    menor = Q
                    S[i][j] = r
            C[i][j] = menor
    return arbolizacion(0, N - 1, 0, S, items)


C = int(input())

results = ['' for x in range(C)]
for i in range(C):
    casos = input().split()
    tree_lights = []
    for case in casos:
        values = case.split(':')
        tree_lights.append((values[0], int(values[1])))
    tree_lights.sort()
    print('caso {}:'.format(i + 1), end="\n\n")
    print(get_tree(tree_lights))
