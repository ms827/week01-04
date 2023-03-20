import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n, k=map(int, input().split())
levels=[]

for _ in range(n):  
    levels.append(int(input()))

lt = min(levels)
rt = min(levels)+k
ans = 0
while lt <= rt:
    mid = (lt+rt)//2
    t = 0
    for level in levels:
        if level < mid:
            t = t + (mid-level)

    if t <= k:
        ans = max(mid,ans)
        lt = mid + 1
    else:
        rt = mid - 1


print(ans)

print("time :", time.time() - st)
