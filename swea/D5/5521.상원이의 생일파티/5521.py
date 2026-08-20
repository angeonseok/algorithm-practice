from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    #양방향인가?
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    visited[1] = True
    q = deque([1])

    cnt = 0

    # 딱 2번만 전파해야됨.
    for _ in range(2):
        for _ in range(len(q)):
            now = q.popleft()

            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    q.append(nxt)

    print(f'#{tc} {cnt}')