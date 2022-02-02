from math import inf


def parentizacion(i, j, S):
    if i == j:
        return "M" + str(i)
    else:
        res = ""
        res += "("
        res += parentizacion(i, S[i][j], S)
        res += " x "
        res += parentizacion(1 + S[i][j], j, S)
        res += ")"
        return res


def get_matrix(p):
    N = len(p)
    m = [[0 for x in range(N)] for y in range(N)]
    S = [[0 for x in range(N)] for y in range(N)]

    for matrices in range(1, N):
        for i in range(N - matrices):
            j = i + matrices
            menor = inf
            for k in range(i, j):
                Q = 0
                if (i == 0):
                    Q = m[i][k] + m[k + 1][j] + p[k] * p[j]
                else:
                    Q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                if Q < menor:
                    menor = Q
                    S[i][j] = k
            m[i][j] = menor
    return parentizacion(1, N - 1, S)


C = int(input())

for i in range(C):
    p = [int(x) for x in input().split()]
    print(get_matrix(p))
