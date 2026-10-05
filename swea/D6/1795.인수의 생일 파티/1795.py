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

    return dist


T = int(input())
for tc in range(1, T+1):
    n, m, x = map(int, input().split())

    #정방향으로 1번 역방향으로 1번
    graph = [[] for _ in range(n + 1)]
    r_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        r_graph[b].append((w, a))

    d = sol(graph, x, n)
    rd = sol(r_graph, x, n)

    #가는 길 + 오는 길 최대
    ans = max(d[i] + rd[i] for i in range(1, n + 1))
    
    print(f'#{tc} {ans}')