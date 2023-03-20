import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")
from itertools import combinations

n = [int(input()) for _ in range(9)]
data = list(combinations(n,7))


for i in data:
    if sum(i) == 100:
        ans = list(i)
        ans.sort()
        break
		

for j in ans:
	print(j)

	

print("time :", time.time() - st)