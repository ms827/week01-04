import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

nums.sort()

def search(value, start, end):
    if start > end:
        return False
    
    median = (start + end) // 2
    if nums[median] > value:
        return search(value, start, median - 1)
    elif nums[median] < value:
        return search(value, median + 1, end)
    else:
        return True
    
for find in finds:
    if search(find, 0, n - 1):
        print (1)
    else:
        print (0)

print("time :", time.time() - st)
