from math import inf

def get_min_coins(amount, coins):
    matrix = [[0 if i == 0 else inf for i in range(amount + 1)]] * len(coins)
    for i in range(1, len(coins)):
        for j in range(1, amount + 1):
            if coins[i] <= j:
                k = j - coins[i]
                matrix[i][j] = min(1 + matrix[i][k], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[-1][-1]

C = int(input())

for i in range(C):
    line = [int(x) for x in input().split()]
    amount = line[0]
    line[0] = 0
    print(get_min_coins(amount, line))