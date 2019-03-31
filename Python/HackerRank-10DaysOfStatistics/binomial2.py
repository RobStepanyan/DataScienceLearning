from math import factorial as ft


def binomial(x1, x2, n, p):
    q = 1 - p
    b = 0
    for x in range(x1, x2 + 1):
        b += (ft(n) / (ft(x) * ft(n - x))) * p ** x * q ** (n - x)

    return round(b, 3)


pn = list(map(int, input().split()))

p = pn[0]/100
n = pn[1]

print(binomial(0, 2, n, p))
print(binomial(2, 10, n, p))
