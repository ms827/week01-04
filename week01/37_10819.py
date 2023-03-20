import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
ans = 0

for data in permutations(arr, n):
    tmp = 0
    for i in range(n-1):
        tmp += abs(data[i] - data[i+1])
    ans = max(ans, tmp)

print(ans)        

print("time :", time.time() - st)
