def cribaErastotenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    dists = 1
    for i in range(n + 1):
        if primes[i]:
            if n % i == 0:
                dists += 1

            for j in range(i*i, n, i):
                if not n % j and primes[j]:
                    dists += 1
                primes[j] = False
    print(dists)


N = int(input())

for i in range(0, N):
    n = int(input())
    cribaErastotenes(n)
