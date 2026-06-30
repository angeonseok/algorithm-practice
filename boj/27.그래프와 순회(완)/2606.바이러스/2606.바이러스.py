import sys
from collections import deque
input = sys.stdin.readline

#dfs bfs 다 해봤다.

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    

n = int(input())
e = int(input())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs(1)  #둘 중 하나만 실행해라
bfs(1)
print(sum(visited)-1)