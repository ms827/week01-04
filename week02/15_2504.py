import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

# https://hongcoding.tistory.com/114

bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)








'''
lst = list(input())

stack = [lst[0]]
while len(stack) > 0:
    for i in range(1,len(lst)):
        
        if lst[i] == '(':
            stack.append(lst[i])

        elif lst[i] =='[':
            stack.append(lst[i])

        else:
            if len(stack) == 0:
                print(0)
                exit(0)
            if stack[-1] == '[' and lst[i] == ']':

                stack.pop()
            elif stack[-1] == '(' and lst[i] == ')':

                stack.pop()
            else:
                print(0)
                exit(0)


print(stack)        



'''




print("time :", time.time() - st)
