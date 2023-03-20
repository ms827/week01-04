import sys
sys.stdin=open("이민석\input.txt", "rt")

def solve(a: list) -> int:
    return(sum(a))


print(solve([1,2,3]))