import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n = int(input())
stack = []
ans = 0
bar = 0
for _ in range(n):
    stack.append(int(sys.stdin.readline()))
for i in range(n):
    pop = stack.pop()
    if pop > bar:
        bar = pop
        ans += 1
print(ans)



print("time :", time.time() - st)
