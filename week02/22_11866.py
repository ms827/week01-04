import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")
from collections import deque


n,k = map(int, input().split())
lst = []
for i in range(1,n+1):
    lst.append(i)
ans = []

q=deque(lst)
for j in range(n):
    q.rotate(-k)
    q_lst = list(q)
    ans.append(q_lst.pop())
    q=deque(q_lst)



print("<",end='')
for i in range(len(ans)-1):
    print("%d, "%ans[i], end='')
print(ans[-1], end='')
print(">")
    
print("time :", time.time() - st)
