from collections import deque

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    visited = [-1] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int, input().split())

    q = deque([s])
    visited[s] = 0
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

    ans = visited[g] if visited[g] != -1 else 0
    print(f'#{tc} {ans}')