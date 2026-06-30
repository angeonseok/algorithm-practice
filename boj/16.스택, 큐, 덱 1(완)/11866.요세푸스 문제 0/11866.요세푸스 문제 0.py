import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
queue = deque()

for i in range(1, n+1):
    queue.append(i)

#k번째 수가 맨 앞으로 올 때 까지 회전 > 제거 > 제거한 순서대로 모아두기
ans = []
while len(queue) > 0:
    for _ in range(k-1):
        queue.rotate(-1)
    a = queue.popleft()
    ans.append(str(a))

#출력 한방에 하고싶었음
print('<', ', '.join(ans), ">",sep="")