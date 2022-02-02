def find_tuple(num_set: list[int], k: int):
    first_index, second_index = divmod(k, len(num_set))
    first_index -= 1 if (second_index == 0) else 0
    first_number = num_set[first_index]
    second_number = num_set[second_index - 1]
    return (first_number, second_number)


N, k = [int(x) for x in input().split()]

num_set = [None] * N
for i in range(N):
    num_set[i] = int(input())

num_set.sort()
print(*find_tuple(num_set, k))
