mod_term = 999999937


def fib(n: int):
    _, _, _, d = fib_mrp(1, 1, 1, 0, n)
    return d


def fib_mrp(a_0, b_0, c_0, d_0, n):
    if n == 1:
        return (1, 1, 1, 0)
    elif n % 2 == 0:
        a, b, c, d = fib_mrp(a_0, b_0, c_0, d_0, n // 2)
        aa = a * a
        bc = b * c
        dd = d * d
        return ((aa + bc) % mod_term, (b*(a + d)) % mod_term, (c*(a + d)) % mod_term, (dd + bc) % mod_term)
    else:
        a, b, c, d = fib_mrp(a_0, b_0, c_0, d_0, (n-1) // 2)
        aa = a * a
        bc = b * c
        dd = d * d
        return ((aa + bc + b*(a + d)) % mod_term, (aa + bc) % mod_term, (c*(a + d) + dd + bc) % mod_term, (c*(a + d)) % mod_term)


C = int(input())

for i in range(C):
    N = int(input())
    print(fib(N))
