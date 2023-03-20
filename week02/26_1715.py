import sys
sys.stdin=open("input.txt", "rt")
from collections import deque
import heapq


n = int(input())
heap = []

for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)
    

if len(heap) == 1: 
    print(0)
else:
    ans = 0
    while len(heap) > 1:
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap) 
        merge = tmp1 + tmp2  
        ans += merge
        heapq.heappush(heap, merge) 

    print(ans)
