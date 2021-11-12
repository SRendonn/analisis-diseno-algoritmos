import heapq


def huffman_encode(case: dict[str, int]):
    heap = [[weight, [symbol, '']] for symbol, weight in case.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        for value in low[1:]:
            value[1] = '0' + value[1]

        for value in high[1:]:
            value[1] = '1' + value[1]

        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: p[1])


C = int(input())

for i in range(C):
    N = int(input())
    case = {}
    for j in range(N):
        line = [x for x in input().split()]
        case[line[0]] = int(line[1])
    print('caso', str(i + 1) + ':')
    huffman_code = huffman_encode(case)
    for char in huffman_code:
        print(char[0], char[1])
