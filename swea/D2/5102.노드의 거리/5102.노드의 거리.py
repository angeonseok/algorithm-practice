from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        i = q.popleft()

        for j in graph[i]:
            if visited[j] == -1:
                visited[j] = visited[i] + 1
                q.append(j)

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int,input().split())

    visited = [-1] * (v+1)
    bfs(s)
    
    if visited[g] == -1 :
        visited[g] = 0
    
    print(f'#{tc} {visited[g]}')