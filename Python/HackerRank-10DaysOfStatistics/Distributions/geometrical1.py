def g(n, p):
    q = 1-p
    return q**(n-1) * p

l = list(input().split())
p = int(l[0])/int(l[1])
n = int(input())

print(round(g(n, p), 3))