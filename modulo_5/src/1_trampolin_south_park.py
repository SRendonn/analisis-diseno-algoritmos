
def min_pataleta(kids: list[tuple[int, int]]):
    pataleta = 0
    tiempos = [0 for x in kids]

    for i in range(len(kids)):
        wanted_time = kids[i][1] // 10
        actual_time = wanted_time
        if not tiempos[actual_time]:
            tiempos[actual_time] = 1
        else:
            actual_time -= 1
            while actual_time >= 0:
                if not tiempos[actual_time]:
                    tiempos[actual_time] = 1
                    break
                actual_time -= 1
            if actual_time == -1:
                actual_time = len(kids) - 1
                while actual_time > wanted_time:
                    if not tiempos[actual_time]:
                        tiempos[actual_time] = 1
                        pataleta += kids[i][0]
                        break
                    actual_time -= 1
    print(pataleta)


C = int(input())

for i in range(C):
    N = int(input())
    kids: list[tuple[int, int]] = []
    for j in range(N):
        aux = [int(x) for x in input().split()]
        kids.append((aux[1], aux[0]))
    min_pataleta(sorted(kids, reverse=True))
