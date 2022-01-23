def longest_common_substr(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    matrix = [[0 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[-1][-1]