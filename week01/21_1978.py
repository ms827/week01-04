import sys
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
lst = list(map(int,input().split()))
ans = 0


for i in lst:
    sosu = False
    if i == 2:
        ans += 1
    for j in range(2,i):
        if i % j == 0:
            sosu = False
            break
        else:
            sosu = True
    if sosu == True:
        ans += 1
    
print(ans)