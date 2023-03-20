import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

ans = 0
length = len(data)
count = 0

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                ans = max(ans, sum_value)

print(ans)



print("time :", time.time() - st)
