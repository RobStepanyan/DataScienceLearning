def g(n, p):
    q = 1-p
    b = 0
    for i in range(1, n+1):
        b += q**(i-1) * p
    return round(b,3)

l = list(input().split())
p = int(l[0])/int(l[1])
n = int(input())

print(g(n, p))