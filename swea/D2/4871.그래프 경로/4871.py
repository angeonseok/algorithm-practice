from collections import deque

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    #단방향이네 ㅋㅋ
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())

    q = deque([s])
    visited[s] = True

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    ans = 1 if visited[g] else 0
    print(f'#{tc} {ans}')