import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q=deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0

#미방문이면 돌리고 +1
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)