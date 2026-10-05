import heapq

def sol(graph, start, v):
    INF = 10**18
    dist = [INF] * (v + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heapq.heappop(pq)

        if d > dist[now]:
            continue

        for w, nxt in graph[now]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist[-1]


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    print(f'#{tc} {sol(graph, 0, n)}')