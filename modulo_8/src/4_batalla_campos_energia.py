from math import dist, inf


def closest_split_pair(start: int, end: int, delta: int, P: list[tuple[int, int]]):
    x = P[(start + end) // 2][0]
    S: list[tuple[int, int]] = []
    for i in range(start, end + 1):
        current_point = P[i]
        if (abs(current_point[0] - x) < delta):
            S.append(current_point)
    S.sort(key=lambda p: p[1])
    min_d = delta
    for p in range(len(S)):
        q = p + 1
        while q < len(S) and q <= p + 7:
            current_d = dist(S[p], S[q])
            if current_d < min_d:
                min_d = current_d
            q += 1
    return round(min_d, 1)

# requires p to be sorted by x coordinate first


def closest_pair(start: int, end: int, P: list[tuple[int, int]]):
    if start == end:
        return inf
    elif end - start == 1:
        return dist(P[start], P[end])
    else:
        dL = closest_pair(start, (start + end) // 2, P)
        dR = closest_pair(1 + ((start + end) // 2), end, P)
        delta = min(dL, dR)
        return closest_split_pair(start, end, delta, P)


C = int(input())
for i in range(C):
    N = int(input())
    robots = [tuple([int(x) for x in input().split()]) for _ in range(N)]
    robots.sort()
    print(int(closest_pair(0, len(robots) - 1, robots)))
