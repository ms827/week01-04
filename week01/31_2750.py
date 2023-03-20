import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

for j in array:
    print(j)

"""
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))


for i in range(0, len(nums) - 1):
    min_idx = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_idx]:
            min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]

for k in nums:
    print(k)
"""
print("time :", time.time() - st)
