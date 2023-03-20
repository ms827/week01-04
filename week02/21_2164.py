import sys
sys.stdin=open("input.txt", "rt")
from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

while(len(q) >1):
    q.popleft()
    move_num = q.popleft()
    q.append(move_num)
    
print(q[0])