n = int(input())

for _ in range(n):
    quiz = input()
    a=0
    b=0
    for i in quiz:
        if i == 'O':
            a += 1
            b += a
        else:
            a = 0
    print(b)  