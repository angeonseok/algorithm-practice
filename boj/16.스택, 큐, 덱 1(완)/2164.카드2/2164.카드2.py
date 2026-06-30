import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

#카드뭉치 만들고
deck = deque()
for i in range(1,n+1):
    deck.append(i)

#맨 위 빼기 > 그 다음 카드를 빼서 > 그 카드를 맨 뒤로
while len(deck) > 1:
    deck.popleft()

    a = deck.popleft()
    deck.append(a)

print(deck[0])