def partition(lista, low, high):
    i = low
    pivot = lista[high]

    for j in range(low, high):

        if lista[j] <= pivot:
            # swap
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[high] = lista[high], lista[i]
    return i


counter = 0


def quick_sort(lista: list, low, high):
    global counter
    if len(lista) == 1:
        return lista
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
