import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")


n = int(sys.stdin.readline())

array = [int(sys.stdin.readline()) for _ in range(n)]
array.sort()

for i in array:
    print(i)


print("time :", time.time() - st)
