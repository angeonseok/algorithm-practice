def bfs(v):
    global cnt
    queue = deque([v])
    visited[v] = cnt

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int,input().split())

cnt = 1
visited = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort(reverse=True)

bfs(v)
for i in range(1, n+1):
    print(visited[i])