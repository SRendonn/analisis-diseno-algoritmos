from itertools import permutations

C = int(input())
for i in range(C):
    mudas_aux = input().split()
    n_mudas = 0

    mudas = [int(mudas_aux[j]) for j in range(10)]
    a = mudas[0]

    perms = permutations(mudas[1:])

    for p in perms:
        n_mudas += (1 if p[0] + p[1] + p[2] + p[3] == a and p[3] + p[4] +
                    p[5] + p[6] == a and p[6] + p[7] + p[8] + p[0] == a else 0)

    print(n_mudas)
