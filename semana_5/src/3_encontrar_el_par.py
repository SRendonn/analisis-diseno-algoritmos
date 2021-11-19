def find_tuple(num_set: list[int], k: int):
    pass


N, k = [int(x) for x in input().split()]

num_set = [None] * N
for i in range(N):
    num_set[i] = int(input())

num_set.sort()
find_tuple(num_set, k)
