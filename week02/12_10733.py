import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))

print("time :", time.time() - st)
