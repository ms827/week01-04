import sys
sys.stdin=open("이민석\input.txt", "rt")

x,y,w,h = map(int,input().split())

a = min(w-x,x)
b = min(h-y,y)

if a>b:
    print(b)
else:
    print(a)