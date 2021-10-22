import math


def divisores(n: int):

    factores = 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            if n != i**2:
                factores += 1
            factores += 1
    return factores


secuencia = [1, 2, 4, 7, 9, 12]
Dx = 12
while(Dx < 100000):
    Dx = Dx + divisores(Dx)
    secuencia.append(Dx)

enumSecuencia = enumerate(secuencia)

N = int(input())

for i in range(N):
    items = input().split()
    a = int(items[0])
    b = int(items[1])

    j = 0
    while a > secuencia[j]:
        j += 1
    k = j
    while b > secuencia[k]:
        k += 1
    if secuencia[k] > b:
        k -= 1
    print(k - j + 1)
