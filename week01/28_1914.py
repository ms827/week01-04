import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

def hanoi(n, start, target, sub):
    if n == 1:
        print(start, target)
        return
    
    hanoi(n-1, start, sub, target)
    print(start, target)
    hanoi(n-1, sub, target, start)


n = int(input())
print(2**n - 1)
if n<=20:
    hanoi(n, 1, 3, 2)




print("time :", time.time() - st)
