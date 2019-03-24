from statistics import median

size = int(input())
elements = list(map(int, input().split()))
frequency = list(map(int, input().split()))

nums = []
for i in range(size):
    nums.extend([elements[i]]*frequency[i])

nums = sorted(nums)

if len(nums) % 2 == 1:
    q1 = median(nums[:len(nums) // 2])
    q3 = median(nums[(len(nums) // 2)+1:])
else:
    q1 = median(nums[:(len(nums) // 2)])
    q3 = median(nums[len(nums) // 2:])

print(float(q3-q1))