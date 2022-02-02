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
