import sys
sys.stdin=open("이민석\input.txt", "rt")

a,b = list(input().split())

if int(a[::-1]) >= int(b[::-1]):
    print(a[::-1])
else:
    print(b[::-1])
