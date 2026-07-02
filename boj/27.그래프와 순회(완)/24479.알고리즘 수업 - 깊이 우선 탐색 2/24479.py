def dfs(v):
    global cnt

    #방문 순서 기록
    visited[v] = cnt
    
    #인접 정점을 오름차순 정점
    graph[v].sort()

    #방문 안하면 방문 순서 증가 후 재귀적으로 dfs 수행
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)       #재귀 깊이 제한 증가
input = sys.stdin.readline

#정점 개수, 간선 개수, 시작 정점
n, m, v = map(int,input().split())
visited = [0] * (n + 1)

#그래프 생성
graph = [[] for _ in range(n+1)]
cnt = 1

#무방향 그래프이므로, 양쪽 추가
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#수행
dfs(v)
for i in range(1, n+1):
    print(visited[i])