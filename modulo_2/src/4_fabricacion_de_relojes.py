# algoritmo de euclides
def mcd(a: int, b: int):
    if b != 0:
        return mcd(b, a % b)
    else:
        return a


N = int(input())

for i in range(N):
    items = input().split()
    sym1 = int(items[0])
    sym2 = int(items[1])
    sym3 = int(items[2])
    max_cd = mcd(mcd(sym1, sym2), sym3)
    print((sym1 + sym2 + sym3)//max_cd)
