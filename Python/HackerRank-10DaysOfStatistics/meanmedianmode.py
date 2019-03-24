import numpy as np
from scipy import stats

length = int(input())
lst = list(map(int, input().split()))

print(np.mean(lst))
print(np.median(lst))
print(int(stats.mode(lst)[0]))
