def partition(lista: list[int], low: int, high: int) -> int:
    i = low
    pivot = lista[high]

    for j in range(low, high):

        if lista[j] <= pivot:
            # swap
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[high] = lista[high], lista[i]
    return i


def find_k(lista: list[int], low: int, high: int, k: int) -> int:
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


N, i = [int(x) for x in input().split()]
lista = []
for j in range(N):
    lista.append(int(input()))
print(abs(find_k(lista, 0, len(lista) - 1, N - i) -
      find_k(lista, 0, len(lista) - 1, i - 1)))
