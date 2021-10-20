def divisores(x):
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    dists = 1
    for i in range(x + 1):
        if primes[i]:
            if not x % i:
                dists += 1

            for j in range(i*i, x + 1, i):
                if primes[j]:
                    primes[j] = False
                    if not x % j:
                        dists += 1
    return dists


secuencia = [1, 2, 4, 7, 9, 12]
Di = 5
Dx = 1
while(Dx < 100000):
    Dx = Dx + divisores(Dx)
    Di += 1
    secuencia.append(Dx)


N = int(input())

for i in range(N):
    items = input().split()
    a = int(items[0])
    b = int(items[1])
