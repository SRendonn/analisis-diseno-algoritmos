def binary_search(fichas: list[int], num, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if num == fichas[mid]:
        return -1

    if num < fichas[mid]:
        return binary_search(fichas, num, low, mid - 1)
    else:
        return binary_search(fichas, num, mid + 1, high)
