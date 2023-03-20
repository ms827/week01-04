import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

sq1, sq2 = map(int,input().split())
n = int(input())
square = [[sq1],[sq2]]
print(square)
for _ in range(n):
    xy, cut = map(int,input().split())
    if xy==0:
        square[1].append(cut) 
    else:
        square[0].append(cut) 



square[0].sort()
square[1].sort()
print(square)

print(len(square[0]))
x_list = square[0][:1]
y_list = square[1][:1]
print(x_list)
print(y_list)
for x in range(len(square[0])-1):
    x_list.append(square[0][x+1]-square[0][x])
for y in range(len(square[1])-1):
    y_list.append(square[1][y+1]-square[1][y])
print(x_list)
print(y_list)

x_list.sort()
y_list.sort()
max_square = x_list[-1] * y_list[-1]
print(max_square)

# max_lst = []
# for a in x_list:
#     for b in range(len(y_list)):
#         max_lst.append(y_list[b]*a)

# print(max(max_lst))


print("time :", time.time() - st)


