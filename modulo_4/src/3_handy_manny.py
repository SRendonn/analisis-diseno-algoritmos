def min_fine(N: int, times: list[int], fines: list[int]):
    weights: list[tuple[float, int]] = []
    for i in range(N):
        weight = fines[i]/times[i]
        weights.append((weight, i))

    weights = sorted(weights, reverse=True)

    time = 0
    delay = 0
    fine = 0

    for weight in weights:
        time = time + times[weight[1]]
        delay = time - times[weight[1]]
        fine = fine + delay * fines[weight[1]]

    return fine


C = int(input())

for i in range(C):
    N = int(input())
    times = []
    fines = []

    for j in range(N):
        aux_list = [int(x) for x in input().split()]
        times.append(aux_list[0])
        fines.append(aux_list[1])

    print(min_fine(N, times, fines))
