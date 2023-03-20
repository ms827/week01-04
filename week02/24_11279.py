import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")
from collections import deque
import heapq

n = int(input())

heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1)*x)
        print(heap)
     
    
print("time :", time.time() - st)
