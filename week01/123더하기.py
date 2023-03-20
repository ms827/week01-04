import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
lst = [0]*11
lst[1] = 1
lst[2] = 2
lst[3] = 4
for i in range(4,len(lst)):
    lst[i] = lst[i-1] + lst[i-2] + lst[i-3]

for i in range(n):
    print(lst[int(input())])


print("time :", time.time() - st)
