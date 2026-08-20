from collections import deque

for tc in range(1, 11):
    _, n = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(100)]
    for i in range(n):
        a, b = arr[i * 2], arr[i * 2 + 1]
        graph[a].append(b)

    visited = [False] * 100
    visited[0] = True
    q = deque([0])

    while q:
        now = q.popleft()

        if now == 99:
            break

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    ans = 1 if visited[99] else 0
    print(f'#{tc} {ans}')