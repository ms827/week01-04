import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    s = sys.stdin.readline().split()
    order = s[0]
    
    #order가 push라면 스택에 정수를 삽입
    if order =="push":
        num = s[1]
        stack.append(num)
    
    #order가 pop이라면 스택 가장 위에 있는 정수를 빼고 그 수를 출력 스택이 비어있다면 -1 출력
    elif order=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    
    #order가 size라면 스택에 들어있는 정수의 개수 출력
    elif order=="size":
        print(len(stack))
    
    #order가 empty일때 스택이 비어있으면 1, 아니면 0
    elif order=="empty":
        if len(stack)==0:
            print(1)
        else: 
            print(0)
    
    #order가 top이라면 스택의 가장 위에 있는 정수 출력, 비어있다면 -1 출력
    elif order=="top": 
        if len(stack)==0: 
            print(-1)
        else: 
            print(stack[-1])


print("time :", time.time() - st)
