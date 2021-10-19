def cribaErastotenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    dists = 1
    for i in range(n + 1):
        if primes[i]:
            if not n % i:
                dists += 1

            for j in range(i*i, n + 1, i):
                if primes[j]:
                    primes[j] = False
                    if not n % j:
                        dists += 1
    print(dists)


N = int(input())

for i in range(N):
    n = int(input())
    cribaErastotenes(n)
