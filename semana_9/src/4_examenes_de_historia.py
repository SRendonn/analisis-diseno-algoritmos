def grade_answers(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    matrix = [[0 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return int(round(matrix[-1][-1] / (m - 1) * 100, 0))

C = int(input())

for i in range(C):
    E = int(input())
    perfect_score = [int(x) for x in input().split()]
    grades = [0 for x in range(E)]
    for j in range(E):
        answers = [int(x) for x in input().split()]
        grades[j] = grade_answers(perfect_score, answers)
    print('caso {}:'.format(i + 1))
    for j in range(E):
        print(grades[j])
    print('')