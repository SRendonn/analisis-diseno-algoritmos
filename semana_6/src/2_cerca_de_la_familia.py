from random import randint


def partition(lista, low, high):
    i = low - 1
    pivot = lista[high]

    for j in range(low, high):

        if lista[j] <= pivot:
            i += 1
            # swap
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    return i + 1


def quick_sort(lista: list, low, high):
    if len(lista) == 1:
        return lista
    if low < high:
        partition_i = partition(lista, low, high)
        quick_sort(lista, low, partition_i - 1)
        quick_sort(lista, partition_i + 1, high)


def get_best_house(lista):
    quick_sort(lista, 0, len(lista) - 1)
    arr_length = len(lista)
    best_index = arr_length // 2
    best_index = best_index if not arr_length % 2 else best_index - 1
    best_house = lista[best_index]

    dist = 0
    for house in lista:
        if house != best_house:
            dist += abs(best_house - house)
    return (best_house, dist)


N = int(input())
lista = []
for i in range(N):
    lista.append(int(input()))
print('{} {}'.format(*get_best_house(lista)))
