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
