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


def find_k(lista: list, low, high, k):
    if low == high:
        return lista[low]
    else:
        p_index = partition(lista, low, high)
        p_value = lista[p_index]
        if k == p_index:
            return p_value
        elif k > p_index:
            return find_k(lista, p_index + 1, high, k)
        else:
            return find_k(lista, low, p_index - 1, k)


def get_best_house(lista):
    k = (len(lista) // 2)
    if not len(lista) % 2:
        k -= 1
    best_house = find_k(lista, 0, len(lista) - 1, k)
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
