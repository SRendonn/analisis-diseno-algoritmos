from bisect import bisect_left


def meeseeks(heights: list[int], lover):
    idx = bisect_left(heights, lover)
    if idx == len(heights):
        return 'la pareja mas cercana mide ' + str(heights[len(heights) - 1])
    elif heights[idx] == lover:
        return 'hay por lo menos una pareja perfecta'
    elif idx == 0:
        return 'la pareja mas cercana mide ' + str(heights[0])
    else:
        second_candidate = heights[idx]
        first_candidate = heights[idx - 1]
        if abs(first_candidate - lover) < abs(second_candidate - lover):
            return 'la pareja mas cercana mide ' + str(first_candidate)
        elif abs(second_candidate - lover) < abs(first_candidate - lover):
            return 'la pareja mas cercana mide ' + str(second_candidate)
        else:
            return 'las parejas mas cercanas miden {} y {}'.format(first_candidate, second_candidate)


n, s = [int(x) for x in input().split()]

heights = [None] * n

for i in range(n):
    heights[i] = int(input())

num_heights = len(heights) - 1
heights.sort()
for i in range(s):
    num = int(input())
    print(meeseeks(heights, num))
