import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")
from itertools import permutations

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = 1e9


def dfs_backtracking(start, now, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[now][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
            min_value = min(min_value, value + travel_cost[now][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
        return
    for i in range(N): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        print(i)
        if travel_cost[now][i] != 0 and i not in visited and value < min_value: 
            visited.append(i) #그 도시를 방문목록에 추가
            print(visited)
            dfs_backtracking(start, i, value + travel_cost[now][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제
            print(visited,'pop')
        

#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)




print("time :", time.time() - st)
 