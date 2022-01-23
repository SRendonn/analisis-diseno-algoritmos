def river_travelling(cost_matrix):
    N = len(cost_matrix)
    M = [[0 for x in range(N)] for x in range(N)]
    for steps in range(1, N):
        for i in range(N - steps):
            j = i + steps
            lowest = cost_matrix[i][j]
            for k in range(i + 1, j):
                lowest = min(lowest, M[k][j] + M[i][k])
            M[i][j] = lowest
    return M[0][-1]