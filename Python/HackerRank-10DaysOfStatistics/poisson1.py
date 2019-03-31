from math import factorial as ft
from math import exp as exp

def poisson(k, l):
    return round((l**k * exp(-l))/ft(k),3)

l = float(input())
k = int(input())

print(poisson(k, l))

