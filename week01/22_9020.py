import sys
sys.stdin=open("이민석\input.txt", "rt")

t = int(input())

def gold(g):
    if g == 2:
        sosu = True
    for j in range(2,g):
        if g % j == 0:
            sosu = False
            break
        else:
            sosu = True
    return sosu


for _ in range(t):
    n = int(input())
    mid = n//2
    if gold(mid) == True:
        print(mid,mid)
    else:
        for i in range(1,mid-1):
            l = mid-i
            r = mid+i
            if gold(l)==True and gold(r)==True:
                print(l,r)
                break


