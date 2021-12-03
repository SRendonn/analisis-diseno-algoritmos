def strassen(X: list[list[int]], Y: list[list[int]], N: int):
    if N == 2:
        Q = X[0][0]*Y[0][0] + X[0][1]*Y[1][0] + X[0][0]*Y[0][1] + \
            X[0][1]*Y[1][1] + X[1][0]*Y[0][0] + X[1][1] * \
            Y[1][0] + X[1][0]*Y[0][1] + X[1][1]*Y[1][1]
        print(Q)
        return Q
    else:
        mid = N // 2
        A = [x[:mid] for x in X[:mid]]
        B = [x[mid:] for x in X[:mid]]
        C = [x[:mid] for x in X[mid:]]
        D = [x[mid:] for x in X[mid:]]

        E = [y[:mid] for y in Y[:mid]]
        F = [y[mid:] for y in Y[:mid]]
        G = [y[:mid] for y in Y[mid:]]
        H = [y[mid:] for y in Y[mid:]]

        P1 = strassen(A, E, mid)
        P2 = strassen(B, G, mid)
        P3 = strassen(A, F, mid)
        P4 = strassen(B, H, mid)
        P5 = strassen(C, E, mid)
        P6 = strassen(D, G, mid)
        P7 = strassen(C, F, mid)
        P8 = strassen(D, H, mid)

        Q = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8
        print(Q)
        return Q


C = int(input())

for i in range(C):
    N = int(input())
    X = []
    Y = []
    for j in range(N):
        X.append([int(x) for x in input().split()])
    for j in range(N):
        Y.append([int(y) for y in input().split()])
    print('caso {}:'.format((i + 1)))
    strassen(X, Y, N)
