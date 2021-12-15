def tomo_o_salto(casillas: list[int]):
    if len(casillas) == 0:
        return 0
    elif len(casillas) == 1:
        return casillas[0]
    elif len(casillas) == 2:
        return max(casillas)
    else:
        best = [casillas[0], max(casillas[0], casillas[1])]
        for i in range(2, len(casillas)):
            take = best[i - 2] + casillas[i]
            best_item = max(take, best[i - 1])
            best.append(best_item)
        return best[-1]
C = int(input())

for i in range(C):
    N = int(input())
    casillas = [None] * N
    for j in range(N):
        casillas[j] = int(input())
    print(tomo_o_salto(casillas))