from operator import truediv


def tsp(dists: list[list[int]]) -> int:
    cry = True
    pass


P = int(input())

for casos in range(P):
    C = int(input())
    d_matrix = [[0] * C] * C
    for c in range(C):
        d_matrix[c] = [int(t) if t != "n.a" else None for t in input().split()]
    r = tsp(d_matrix)
    print(r)
