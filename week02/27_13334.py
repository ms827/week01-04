import sys
sys.stdin=open("input.txt", "rt")
from collections import deque
import heapq

n = int(sys.stdin.readline())
rail = []
heap = []
ans=0
for i in range(n):
    h, o = map(int, sys.stdin.readline().split())
    if h > o:
        rail.append([o, h])
    else:
        rail.append([h, o])
# print(rail)

d = int(input())

rail.sort(key=lambda x: (x[1], x[0]))

# print(rail)

for i in range(n):
    start = rail[i][0]
    end = rail[i][1]

    if end-start <= d:
        heapq.heappush(heap, start)
    else:
        continue
    while len(heap) != 0:
        if end - d > heap[0]:
            heapq.heappop(heap)
        else:
            break
    ans = max(ans,len(heap))

print(ans)