import sys
from collections import deque
input = sys.stdin.readline

#1차원 배열 bfs가 더 어려운거같기도

n, k = map(int, input().split())
q = deque()
visited = [0] * 100001

q.append(n)
visited[n] = 0

while q:
    x = q.popleft()
    if x == k:
        break
    
    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx < 100001 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[k])