import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")
from collections import deque
import heapq

N=int(sys.stdin.readline())

leftHeap=[]
rightHeap=[]
answer=[]
for i in range(N):

    inputNum=int(sys.stdin.readline())

    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, (-inputNum, inputNum))
        print(leftHeap)
    else:
        heapq.heappush(rightHeap, (inputNum, inputNum))
        print(rightHeap)
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min=heapq.heappop(rightHeap)[0]
        max=heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    answer.append(leftHeap[0][1])
    
for j in answer:
    print(j)
