import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# trees.sort()
start = 1
end = max(trees)
# end =trees[-1]




while start <= end:
    cut = 0
    median = (start + end) // 2
    # for i in range(n):
    #     if trees[i] > median:
    #         cut += trees[i]-median

    for tree in trees:
        if tree > median:
            cut += tree-median


    if cut < m:
        end = median - 1
    else:
        start = median + 1

print(end)

print("time :", time.time() - st)
