import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
data = list(map(int, input().split()))
cal = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

min_result = 1e9
max_result = -1e9

# 모든 경우의 수를 탐색하는 재귀 함수
def dfs(i, now):
    global min_result, max_result

    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)
        return

    if cal[0] > 0:
        cal[0] -= 1
        dfs(i+1, now+data[i])
        cal[0] += 1

    if cal[1] > 0:
        cal[1] -= 1
        dfs(i+1, now-data[i])
        cal[1] += 1

    if cal[2] > 0:
        cal[2] -= 1
        dfs(i+1, now*data[i])
        cal[2] += 1

    if cal[3] > 0:
        cal[3] -= 1
        if now < 0:
            dfs(i+1, -(-now // data[i]))
        else:
            dfs(i+1, now // data[i])
        cal[3] += 1

dfs(1, data[0])
print(max_result)
print(min_result)

print("time :", time.time() - st)
