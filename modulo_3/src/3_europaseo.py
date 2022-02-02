from itertools import permutations


def tsp(dists: list[list[int]]):
    C = len(dists)
    perms = permutations([x for x in range(C)])
    best = 10000
    for p in perms:
        total = 0
        for i in range(C - 1):
            if (dists[p[i]][p[i + 1]] != None):
                total += dists[p[i]][p[i + 1]]
            else:
                total = 10000
                break
        if total < best:
            best = total
    return round(best / 10) if best < 10000 else "imposible"


P = int(input())

for casos in range(P):
    C = int(input())
    d_matrix = [[0] * C] * C
    for c in range(C):
        d_matrix[c] = [int(t) if t != "n.a" else None for t in input().split()]
    print(tsp(d_matrix))
