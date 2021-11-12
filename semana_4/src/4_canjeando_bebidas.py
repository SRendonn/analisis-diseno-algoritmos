def canje_bebidas(tapas: list[int]):
    bebidas = 0


C = int(input())

for i in range(C):
    N = int(input())
    tapas = [0 * N]
    for j in range(N):
        tapas[j] = int(input())
    canje_bebidas(tapas)
