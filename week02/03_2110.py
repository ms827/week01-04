import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

def Search(m):
    cnt=1
    end=iptime[0] 
    for i in iptime[1:]: 
        if i-end>=m:
            cnt+=1
            end=i
    return cnt


n, c=map(int, input().split())
iptime=[]

for _ in range(n):
    iptime.append(int(input()))

iptime.sort() 

lt=1
rt=iptime[-1]-iptime[0]

while lt<=rt:  
    mid=(lt+rt)//2
    if Search(mid)>=c:
        ans=mid
        lt=mid+1
    else:
        rt=mid-1

print(ans)



print("time :", time.time() - st)
