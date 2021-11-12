def merca_mas_mas(precios: list[int]):
    ahorro = 0
    precios = sorted(precios, reverse=True)
    products = len(precios)
    current_third = 2
    while current_third < products:
        ahorro += precios[current_third]
        current_third += 3
    print(ahorro)


C = int(input())

for i in range(C):
    precios = [int(x) for x in input().split()]
    merca_mas_mas(precios)
