import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
lst = []
word = ''
for _ in range(n):
    word = input()
    if len(word)>50:
        pass
    if word not in lst:
        lst.append(word)
lst.sort()
ans = sorted(lst, key=len)

print(*ans)

print("time :", time.time() - st)
