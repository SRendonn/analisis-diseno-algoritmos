def str_alignment(X, Y, alpha = 1, beta = 1):
    m = len(X) + 1
    n = len(Y) + 1
    P = [[0 for x in range(n)] for x in range(m)]
    for i in range(m):
        P[i][0] = i * alpha
    for j in range(n):
        P[0][j] = j * alpha
    for i in range(1, m):
        for j in range(1, n):
            a = P[i - 1][j - 1] + beta if X[i - 1] != Y[j - 1] else P[i - 1][j - 1]
            b = P[i][j - 1] + alpha
            c = P[i - 1][j] + alpha
            P[i][j] = min(a, b, c)
    return P[-1][-1]