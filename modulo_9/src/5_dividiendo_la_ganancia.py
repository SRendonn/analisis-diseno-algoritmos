def knapsack(values: list[int], weights: list[int], max_weight: int):
    cache = [[0 for x in range(max_weight + 1)]
                  for x in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for j in range(1, max_weight + 1):
            if (weights[i - 1] > j):
                cache[i][j] = cache[i - 1][j]
            else:
                with_item = values[i - 1] + \
                    cache[i - 1][j - weights[i - 1]]
                without_item = cache[i - 1][j]

                cache[i][j] = max(
                    with_item, without_item)

    return cache[-1][max_weight]

def split_earnings(coins: list[int], max_weight: int):
    ks = knapsack(coins, coins, max_weight // 2)
    return 10 * (max_weight - 2 * ks)

C = int(input())
for i in range(C):
    monedas = [int(x) // 10 for x in input().split()]
    print(split_earnings(monedas, sum(monedas)))