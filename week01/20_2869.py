import sys
sys.stdin=open("이민석\input.txt", "rt")


a,b,v = map(int,input().split())

# 시간초과
"""
ans = 0

while v > 0:
    if v-a <= 0:
        print(ans+1)
        break
    else:
        v -= a
    v += b
    ans += 1
"""

if (v-b) % (a-b) == 0:
    print((v-b) // (a-b))
else:
    print(((v-b) // (a-b)) +1)


