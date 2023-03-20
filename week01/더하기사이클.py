import sys
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
m = n
cnt = 0

while True:
    arr = list(map(int,str(m)))
    m = ((m%10) * 10) + (sum(arr)%10)
    cnt += 1
    if m == n:
        break

print(cnt)
