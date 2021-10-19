def cribaErastotenes(p, q):
    primes = [True] * (q + 1)
    primes[0] = primes[1] = False
    dists = 0
    for i in range(q + 1):
        if primes[i]:
            if i >= p:
                dists += 1
            for j in range(i*i, q + 1, i):
                primes[j] = False
    print(dists)


N = int(input())

for i in range(N):
    items = input().split()
    cribaErastotenes(int(items[0]), int(items[1]))
