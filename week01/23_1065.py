import sys
sys.stdin=open("이민석\input.txt", "rt")

x = int(input())

if x < 100:
    han = x
else:
    han = 99
    for i in range(100, x+1):
        lst = list(map(int, str(i)))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            han += 1
print(han)




