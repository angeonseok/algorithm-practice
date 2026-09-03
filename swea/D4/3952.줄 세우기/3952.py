from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1

    q = deque([i for i in range(1, n+1) if ind[i] == 0])
    ans = []
    while q:
        now = q.popleft()
        ans.append(now)

        for nxt in graph[now]:
            ind[nxt] -= 1

            if ind[nxt] == 0:
                q.append(nxt)

    #사실 조건 만족하는 경우만 줘서 없어도됨ㅋㅋ
    if len(ans) != n:
        ans = []

    print(f'#{tc}', *ans)