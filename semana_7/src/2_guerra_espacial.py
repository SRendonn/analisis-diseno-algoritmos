from functools import total_ordering
from math import dist, inf, isinf


@total_ordering
class planet():
    def __init__(self, x: int, y: int, liga: str):
        self.x = x
        self.y = y
        self.liga = liga

    def coords(self):
        return (self.x, self.y)

    def __lt__(self, other):
        return (self.x, self.y, self.liga) < (other.x, other.y, self.liga)

    def __eq__(self, other):
        return (self.x, self.y, self.liga) == (other.x, other.y, self.liga)

    def __str__(self):
        return '{} {} {}'.format(self.x, self.y, self.liga)


def closest_split_pair(start: int, end: int, delta: int, P: list[planet]):
    x = P[(start + end) // 2].x
    S: list[planet] = []
    for i in range(start, end + 1):
        current_planet = P[i]
        if (abs(current_planet.x - x) < delta):
            S.append(current_planet)
    S.sort(key=lambda p: p.y)
    min_d = delta
    for p in range(len(S)):
        q = p + 1
        while q < len(S) and q <= p + 7:
            if S[p].liga != S[q].liga:
                current_d = dist(S[p].coords(), S[q].coords())
                if current_d < min_d:
                    min_d = current_d
            q += 1
    return round(min_d, 1)


def closest_pair(start: int, end: int, p: list[planet]):
    if start == end:
        return inf
    elif end - start == 1:
        if p[start].liga != p[end].liga:
            return dist(p[start].coords(), p[end].coords())
        else:
            return inf
    else:
        dL = closest_pair(start, (start + end) // 2, p)
        dR = closest_pair(1 + ((start + end) // 2), end, p)
        delta = min(dL, dR)
        return closest_split_pair(start, end, delta, p)


N = int(input())

while N != 0:
    planets: list[planet] = []
    for i in range(N):
        x, y, liga = [j for j in input().split()]
        planets.append(planet(int(x), int(y), liga))
    planets.sort()
    res = closest_pair(0, len(planets) - 1, planets)
    print('INF' if isinf(res) else res)
    N = int(input())
