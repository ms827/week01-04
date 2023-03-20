import sys
sys.stdin=open("input.txt", "rt")
"""
m, n, l = map(int, sys.stdin.readline().split()) 
shoot = list(map(int, sys.stdin.readline().split()) )

ans = 0

def search_left(xx,yy):
    for j in range(m):
        if shoot[j] < xx:
            if xx-shoot[j]+yy <= l:
                return True
    return False
        
            
def search_right(xx,yy):
    for k in range(m):
        if shoot[k] > xx:
            if abs(xx-shoot[k])+yy <= l:
                return True
    return False


for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    if x in shoot and y-l<=0:
        ans += 1
        continue
    if not y > l:
        if search_left(x,y):
            ans += 1
            continue
        if search_right(x,y):
            ans += 1
            continue
print(ans) 


"""

input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리,
m, n, l = map(int, input().split())
# 사로의 사람위치
gun = list(map(int, sys.stdin.readline().split()))
# 동물위치
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n))
gun.sort()
cnt = 0

for x, y in animal:
    # y좌표가 l보다 크면 범위를 벗어나므로 제외
    if (y>l):
        continue

    # 각 동물위치 기준 가능한 사로 start, end지점 산출
    s = x+y-l
    e = x-y+l
    
    # 사로의 사람 위치를 이진탐색을 해서 어떤사로가 사냥감이 잡히는 사로인지 탐색
    # 하기 위해서 gun리스트를 탐색할 인덱스를 나타낸다.
    left, right = 0, m-1

    while left <= right:
        mid = (left+right)//2
        if gun[mid] >= s and gun[mid] <= e:
            cnt += 1
            break
        elif gun[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
print(cnt)