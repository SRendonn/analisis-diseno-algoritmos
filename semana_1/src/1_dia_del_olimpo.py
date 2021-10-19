# algoritmo de euclides
def mcd(a, b):
    if b != 0:
        return mcd(b, a % b)
    else:
        return a


def mcm(a, b):
    max_cd = mcd(a, b)
    return a*b // max_cd if max_cd > 0 else 0


N = int(input())
for i in range(0, N):
    min_cm = 1
    items = input().split()
    for item in items:
        a = int(item)
        min_cm = mcm(a, min_cm)
    print(min_cm)
