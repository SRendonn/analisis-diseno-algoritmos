def knapsack(songs: list[int], gym_stay: int):
    val_matrix = [[0 for x in range(gym_stay + 1)]
                  for x in range(len(songs) + 1)]

    for i in range(1, len(songs) + 1):
        for j in range(1, gym_stay + 1):

            if (songs[i - 1] > j):
                val_matrix[i][j] = val_matrix[i - 1][j]
            else:
                with_item = songs[i - 1] + \
                    val_matrix[i - 1][j - songs[i - 1]]
                without_item = val_matrix[i - 1][j]

                val_matrix[i][j] = max(
                    with_item, without_item)

    return val_matrix[len(songs)][gym_stay]


N = int(input())
for i in range(N):
    aux_in = input().split()
    songs = [int(aux_in[j]) for j in range(1, len(aux_in))]
    gym_stay = int(aux_in[0])

    print(gym_stay - knapsack(songs, gym_stay))
