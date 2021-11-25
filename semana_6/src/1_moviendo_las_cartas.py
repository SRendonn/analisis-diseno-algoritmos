counter = 0


def merge_sort(lista: list[int]):
    global counter
    if len(lista) > 1:
        left = lista[:len(lista) // 2]
        right = lista[len(lista) // 2:]
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


N = int(input())
while N != 0:
    lista = []
    for i in range(N):
        lista.append(int(input()))
    counter = 0
    winner = merge_sort(lista)
    print('Empate' if winner == 0 else 'Pedro' if winner %
          2 == 0 else 'Susana')
    N = int(input())
