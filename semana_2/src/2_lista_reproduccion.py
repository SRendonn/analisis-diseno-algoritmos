def knapsack(gym_stay: int, songs: list[int]):
    pass


N = int(input())
for i in range(N):
    aux_in = input().split()
    songs = [int(aux_in[j]) for j in range(1, len(aux_in))]
    gym_stay = int(aux_in[0])

    knapsack(gym_stay, songs)
