from math import factorial as ft

def binomial(x, n, p):
    q = 1-p
    b = 0
    for i in range(x, n+1):
        b = b + (ft(n) / (ft(i)*ft(n-i))) * p**i * q**(n-i)
    return round(b,3)



bg = list(map(float, input().split()))
br = bg[0]
gr = int(bg[1])

n = 6
p = 1.09/2.09
x = 3

print(binomial(x, n, p))