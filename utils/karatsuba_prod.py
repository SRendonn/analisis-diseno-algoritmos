def karatsuba(n: int, x: str, y: str):
    if n == 1:
        res = int(x) * int(y)
        return res
    else:
        n_mid = n // 2
        a = x[:n_mid]
        b = x[n_mid:]
        c = y[:n_mid]
        d = y[n_mid:]

        P1 = karatsuba(n_mid, a, c)
        P2 = karatsuba(n_mid, a, d)
        P3 = karatsuba(n_mid, b, c)
        P4 = karatsuba(n_mid, b, d)

        res = 10**n*P1 + 10**n_mid*(P2 + P3) + P4
        return res
