import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n = int(input())
lst = list(map(int,input().split()))

lst.sort()
ans = [0,0]
lt = 0
rt = -1
min_value = float('inf')


while lt-rt < n:  
    if lst[lt]+lst[rt] == 0:
        print(lst[lt],lst[rt])
        exit(0)
    elif lst[lt]+lst[rt] < 0:
        
        if min_value > abs(lst[lt]+lst[rt]):
            min_value = abs(lst[lt]+lst[rt])
            ans = [lst[lt],lst[rt]]
        lt += 1
    else:
        if min_value > abs(lst[lt]+lst[rt]):
            min_value = abs(lst[lt]+lst[rt])
            ans = [lst[lt],lst[rt]]
        rt -= 1

print(ans[0],ans[1])

print("time :", time.time() - st)
