counter = 0


def merge_sort(lista: list[int]):
    global counter
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                counter += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
        return counter
    else:
        return counter


M, N = [int(x) for x in input().split()]
lista = []
for i in range(M):
    sec = input()
    lista.append((merge_sort(list(sec)), sec))
    counter = 0
lista.sort()
for i in range(N):
    print(lista[i][1])
