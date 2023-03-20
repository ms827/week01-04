import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

import itertools
num = ''

while num != ['0']:
    num = list(input().split())
    lotto = itertools.combinations(num[1:], 6)
    for i in lotto:
        ans = ' '.join(i)
        print(ans)
    print()




print("time :", time.time() - st)
