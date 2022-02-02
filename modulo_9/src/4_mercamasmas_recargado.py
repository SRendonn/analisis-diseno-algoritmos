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

    return cache

C = int(input())
prices = [None] * C
weights = [None] * C

for i in range(C):
    line = input().split()
    prices[i] = int(line[0])
    weights[i] = int(line[1])

P = int(input())
peso_max = 0
pesos_fam = [None] * P
for j in range(P):
    pesos_fam[j] = int(input())
    peso_max = max(peso_max, pesos_fam[j])

ks = knapsack(prices, weights, peso_max)
prices_sum = 0
for p in pesos_fam:
    prices_sum += ks[-1][p]
print(prices_sum)