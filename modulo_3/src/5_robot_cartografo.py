from itertools import product


def cartograph(map_graph: list[list[int]]):
    for k in range(1, len(map_graph) + 1):
        colors = [x for x in range(k)]
        combs = product(colors, repeat=len(map_graph))
        for c in combs:
            valid = True
            for i in range(len(map_graph)):
                for j in range(len(map_graph)):
                    if map_graph[i][j] == 1 and i != j and c[i] == c[j]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return k


P = int(input())

for casos in range(P):
    C = int(input())
    d_matrix = [[0] * C] * C
    for c in range(C):
        d_matrix[c] = [int(t) for t in input().split()]
    print(cartograph(d_matrix))
