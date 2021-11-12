def canje_bebidas(tapas: list[int]):
    if len(tapas) <= 3:
        return sum(tapas) // 1000

    bebidas = 0
    tapas = sorted(tapas)
    current_count = 0
    while len(tapas) >= 2:
        max_tapa = tapas.pop()
        for i in range(len(tapas)):
            current_count = max_tapa + tapas[i]
            if (current_count >= 1000):
                bebidas += 1
                tapas = tapas[i + 1:]
                break
    print(bebidas)


C = int(input())

for i in range(C):
    N = int(input())
    tapas = []
    for j in range(N):
        tapas.append(int(input()))
    canje_bebidas(tapas)
