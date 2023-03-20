import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")


import itertools

n = int(input())
k = int(input())

deck = []
for i in range(n):
    deck.append(input())

cards = itertools.permutations(deck, k)

ans = set()
for card in cards:
    print(card)
    ans.add(''.join(card))
print(ans)
print(len(ans))


"""
nn = int(input())
kk = int(input())
card = []

for i in range(nn):
    card.append(input())

string = []
result = set()

def slice(card, n): # 본인을 제외한 것을 리턴해주는 함수
    return card[0:n] + card[n+1:len(card)] # card 안 건드리고 본인은 제외한 리스트를 새로 만들어서 리턴해주는 것

def setCards(card,k):
    global string
    n = len(card)

    if k <= 0:
        result.add(''.join(string))
        return
    for i in range(n):
        string.append(card[i])
        setCards(slice(card,i),k-1) # 방금 전에 뽑은 것을 리스트에서 제외하고 그 중에서 k-1개 뽑아줘야 함
        string.pop() # string을 pop해줘야 복구가 됨

setCards(card,kk)
print(len(result))

"""
print("time :", time.time() - st)