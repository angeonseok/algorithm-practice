#24479와 동일한 구조. 단 dfs 전 그래프 정렬을 내림차순으로
def dfs(v):
    global cnt

    visited[v] = cnt

    graph[v].sort(reverse= True)

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, v = map(int,input().split())

cnt = 1
visited = [0] * (n + 1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
for i in range(1, n+1):
    print(visited[i])