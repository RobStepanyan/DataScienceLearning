size = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

XW = [X[i]*W[i] for i in range(size)]
XW = sum(XW)

print(round(XW/sum(W),1))