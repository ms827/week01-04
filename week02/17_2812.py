import sys
sys.stdin=open("input.txt", "rt")

n,k = map(int,input().split())
nums = list(map(int,input().strip()))
stack = []
rest = k
for i in range(n):
    while rest>0 and stack:
        if stack[len(stack)-1] < nums[i]:
            stack.pop()
            rest-=1
        else:
            break
    stack.append(nums[i])
for x in range(n-k):
    print(stack[x], end="")

