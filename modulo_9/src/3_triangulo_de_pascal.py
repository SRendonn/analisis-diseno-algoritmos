pascal_triangle = [[1], [1, 1]]
# max val in level
pascal_max = [1, 1]
# current max level of the triangle for caching
max_level = 2
def max_pascaliano(h: int):
    create_pascal_triangle(h)
    global pascal_max
    return pascal_max[h - 1] % 999999937

def create_pascal_triangle(h: int):
    global max_level
    if h <= max_level:
        return None
    else:
        global pascal_triangle
        global pascal_max
        for i in range(max_level - 1, h - 1):
            current_row = pascal_triangle[i]
            next_row = [1] * (i + 2)
            max_row = 0
            for j in range(1, len(current_row)):
                current_sum = current_row[j - 1] + current_row[j]
                max_row = max(max_row, current_sum)
                next_row[j] = current_sum
            pascal_triangle.append(next_row)
            pascal_max.append(max_row)
        max_level = h

C = int(input())

for i in range(C):
    h = int(input())
    print(max_pascaliano(h))