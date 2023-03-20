import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1


for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

print("time :", time.time() - st)
