
counter = 0


def partition(lista, low, high):
    i = low
    for j in range(low + 1, high + 1):
        if lista[j] < lista[low]:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i], lista[low] = lista[low], lista[i]
    return i


def quick_sort(lista: list, low, high):
    global counter
    if low < high:
        counter += 1
        partition_i = partition(lista, low, high)
        quick_sort(lista, low, partition_i - 1)
        quick_sort(lista, partition_i + 1, high)


C = int(input())

for i in range(C):
    lista = [int(x) for x in input().split()]
    quick_sort(lista, 0, len(lista) - 1)
    print(counter)
    counter = 0
