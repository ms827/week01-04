from itertools import combinations
import sys
sys.stdin=open("이민석\input.txt", "rt")
#틀렸습니다.
a_list = list(map(int,sys.stdin.readline().split()))
b_list = list(map(int,sys.stdin.readline().split()))
n = input()

k1 = a_list[0]
a_list.pop(0)
k2 = b_list[0]
b_list.pop(0)

a_com= combinations(a_list,6)
b_com = combinations(b_list,6)

for i in a_com:
    for j in i:
        print(j,end=' ')
    print()

print()

for i in b_com:
    for j in i:
        print(j,end=' ')
    print()