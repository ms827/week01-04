import sys

n = int(input())

video = []

for i in range(n):
    video.append(input())

for i in video:
    print(*i)

rv = len(video)
cv = len(video[0])

print(rv, cv)


def video_zip(r_left, r_right, c_left, c_right):

    if r_right == r_left:
        print(video[r_left, c_left], end='')


    while (r_right != r_left):
        for i in range(r_left, r_right):
            checkout = 1

            for j in range(c_left, c_right):
                if i == r_left and j == c_left:
                    check_num = int(video[i][j])

                if int(video[i][j]) == check_num:
                    check_num = int(video[i][j])
                    if i == r_right-1 and j==c_right-1:
                        print(check_num, end='')
                        # checkout=0
                elif int(video[i][j]) != check_num:
                    print('(', end='')
                    if r_right > r_left+1:
                        video_zip(r_left, r_right//2, c_left, c_right//2)
                        video_zip(r_left, r_right//2, c_right//2, c_right)
                        video_zip(r_right//2, r_right, c_left, c_right//2)
                        video_zip(r_right//2, r_right, c_right//2, c_right)

                    checkout = 0
                    print(')', end='')
                    break

            if checkout == 0:
                break
        if checkout == 0:
                break       



rr_left = 0
rr_right = len(video)
cc_left = 0
cc_right = len(video[0])

video_zip(rr_left, rr_right, cc_left, cc_right)