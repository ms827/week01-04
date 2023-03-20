#코드를 입력하세요.
import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(paper)
result = []

#크기 n과 함께 시작 지점을 입력받는다
def cut(x, y, n):
    color = paper[x][y]
    #x, y좌표부터 모든 n*n칸이 같은 값인 경우
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                #1사분면
                cut(x, y, n//2)
                #2사분면
                cut(x , y + n//2, n//2)
                #3사분면
                cut(x + n//2, y, n//2)
                #4사분면
                cut(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

cut(0, 0, n)
print(result.count(0))
print(result.count(1))