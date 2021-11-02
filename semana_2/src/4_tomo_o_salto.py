from itertools import product


def take_or_jump(game: list[int]):

    if len(game) <= 2:
        return max(game)

    prod = product([0, 1], repeat=len(game) - 2)
    best = 0
    for picked in prod:
        res = game[0]
        for i in range(0, len(game) - 2):
            if i == 0:
                if picked[0]:
                    res += game[1] - res
            elif picked[i]:
                res += game[i + 1] - game[i] * picked[i - 1]
            else:
                res += game[i + 1] * picked[i]
        if not picked[len(game) - 3]:
            res += game[len(game) - 1]
        elif game[len(game) - 2] < game[len(game) - 1]:
            res += game[len(game) - 1] - game[len(game) - 2]
        if best < res:
            best = res
    return best


C = int(input())

for _ in range(C):
    juego = [int(d) for d in input().split()]
    print(take_or_jump(juego))
