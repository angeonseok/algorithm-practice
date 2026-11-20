import heapq

def sol(graph, start, end, v):
    INF = 10**18
    dist = [INF] * (v + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heapq.heappop(pq)

        if d > dist[now]:
            continue

        for nw, nxt in graph[now]:
            nd = nw + d
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist[end]


T = int(input())
for tc in range(1, T+1):
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((t, e))

    ans = -1
    for i in range(1, n+1):
        ans = max(ans, sol(graph, i, x, n))

    print(f'#{tc} {ans}')