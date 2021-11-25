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


def quick_sort(lista: list, low, high):
    if len(lista) == 1:
        return lista
    if low < high:
        partition_i = partition(lista, low, high)
        quick_sort(lista, low, partition_i - 1)
        quick_sort(lista, partition_i + 1, high)
        return lista
