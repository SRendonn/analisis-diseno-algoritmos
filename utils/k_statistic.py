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
        if k == p_value:
            return p_value
        elif k > p_value:
            return find_k(lista, p_index + 1, high, k)
        else:
            return find_k(lista, low, p_index - 1, k)
