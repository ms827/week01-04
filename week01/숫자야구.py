import sys
sys.stdin=open("이민석\input.txt", "rt")

def strike(a, b):
    a,b = str(a), str(b)
    cnt = 0
    for i in range(3):
        if a[i] == b[i]:
            cnt += 1
    return cnt

# def ball(a, b):
#     a,b = str(a), str(b)
#     cnt = 0
#     for i in b:
#         if i in a:
#             cnt += 1
#     return cnt

lst = []
for i in range(123, 988):
    if '0' not in str(i) and len(set(str(i))) == 3:
        lst.append(i)

n = int(input())

for _ in range(n):
    num, s, b = map(int,input().split())
    for j in lst:
        s_cnt = strike(j,num)
        b_cnt = ball(j,num)
        if s_cnt != s or b_cnt-s_cnt != b:
            lst.remove(j)

print(len(lst))