import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

t = int(input())

for i in range(t):
    stack = []
    ps = list(input())
    if ps[0] == ')':
        print('NO')
        continue
    if ps[-1] == '(':
        print('NO')
        continue

    for j in range(len(ps)):
        if ps[j] == '(':
            stack.append('(')
        else:
            if len(stack)>0:
                stack.pop()
            else:
                print('NO')
                stack.append(')')
                break
    if len(stack) == 0:
        print('YES')
    elif stack.pop() == ')':
         continue
    else:
        print('NO')



print("time :", time.time() - st)
