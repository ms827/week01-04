import sys
sys.stdin=open("이민석\input.txt", "rt")

t = int(input())


for _ in range(t):
    r, s = list(map(str, input().split()))
    r = int(r)

    for i in s:
        print(r*i, end='')
    print()