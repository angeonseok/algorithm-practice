import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end = " ")     #방문한 정점 출력

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_1[v] = 1

    while queue:
        node = queue.popleft()
        print(node, end = " ")  #방문한 정점 출력
        
        for i in graph[node]:
            if visited_1[i] == 0:
                visited_1[i] = 1
                queue.append(i)

n, m, v = map(int, input().split())

visited = [0] * (n + 1)
visited_1 = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)