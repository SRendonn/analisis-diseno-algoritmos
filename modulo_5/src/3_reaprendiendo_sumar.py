import heapq


def min_cost(precios: list[int]):
    cost = 0
    current_length = len(precios)
    while current_length >= 2:
        primer_prod = heapq.heappop(precios)
        seg_prod = heapq.heappop(precios)
        cost += primer_prod + seg_prod
        heapq.heappush(precios, primer_prod + seg_prod)
        current_length = len(precios)
    print(cost)


N = int(input())

while N != 0:
    nums = []
    heapq.heapify(nums)
    for i in range(N):
        heapq.heappush(nums, int(input()))
    min_cost(nums)
    N = int(input())
