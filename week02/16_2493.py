import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")


n = int(input())
lst = list(map(int, input().split()))

stack = [(lst[0], 0)]

ans = [0]

for i in range(1, n):
    while stack:
        if stack[-1][0] > lst[i]:
            ans.append(stack[-1][1] + 1)
            break
        stack.pop()
    if not stack:
        ans.append(0)
    stack.append((lst[i], i))

print(" ".join(map(str, ans)))



print("time :", time.time() - st)
