def str_alignment(X, Y):
    m = len(X) + 1
    P = [[0 for x in range(m)] for x in range(m)]
    for i in range(m):
        P[i][0] = i
        P[0][i] = i
    for i in range(1, m):
        for j in range(1, m):
            a = P[i - 1][j - 1] + 1 if X[i - 1] != Y[j - 1] else P[i - 1][j - 1]
            b = P[i][j - 1] + 1
            c = P[i - 1][j] + 1
            P[i][j] = min(a, b, c)
    return P[-1][-1] // 2

N = int(input())

for i in range(N):
    word = input()
    print(str_alignment(word, word[::-1]))