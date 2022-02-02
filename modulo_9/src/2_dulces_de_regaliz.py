def resolver_precio(longitudes: list[int], length):
    prices_min = [None for i in range(length)]
    prices_max = [None for i in range(length)]
    prices_min[0] = longitudes[0]
    prices_max[0] = longitudes[0]
    for i in range(1, length):
        prices_min[i] = longitudes[i]
        prices_max[i] = longitudes[i]
        for j in range(i):
            i_prima = i - j - 1
            prices_min[i] = min(prices_min[i], longitudes[j] + prices_min[i_prima])
            prices_max[i] = max(prices_max[i], longitudes[j] + prices_max[i_prima])
    return str(prices_min[-1]) + ' ' + str(prices_max[-1])

C = int(input())

for i in range(C):
    case = [int(x) for x in input().split()]
    length = case[0]
    longitudes = case[1:]
    print(resolver_precio(longitudes, length))