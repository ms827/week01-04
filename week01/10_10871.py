n, x = input().split()

a = map(int, input().split())
for i in a:
    if i < int(x):
        print(i)