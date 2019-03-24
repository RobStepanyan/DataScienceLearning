from statistics import median

size = int(input())
nums = sorted(list(map(int, input().split())))

q2 = median(nums)
if len(nums) % 2 == 1:
    q1 = median(nums[:size // 2])
    q3 = median(nums[(size // 2) + 1:])
else:
    q1 = median(nums[:(size // 2) + 1])
    q3 = median(nums[size // 2:])

print(int(q1))
print(int(q2))
print(int(q3))
