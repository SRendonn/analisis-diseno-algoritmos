def binary_search(fichas: list[int], num, low, high):
    if low > high:
        print(str(num), 'no se encuentra')
        return None

    mid = (low + high) // 2

    if num == fichas[mid]:
        print(str(num), 'se encuentra en', mid + 1)
        return None

    if num < fichas[mid]:
        binary_search(fichas, num, low, mid - 1)
    else:
        binary_search(fichas, num, mid + 1, high)


n, q = [int(x) for x in input().split()]

fichas = [0] * n

for i in range(n):
    fichas[i] = int(input())

numFichas = len(fichas) - 1
fichas.sort()
for i in range(q):
    num = int(input())
    binary_search(fichas, num, 0, numFichas)
