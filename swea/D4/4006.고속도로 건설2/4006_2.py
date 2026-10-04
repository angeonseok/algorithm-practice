import heapq

def prim(graph, v, start):
    visited = [False] * (v + 1)
    pq = [(0, start)]
    total = 0

    while pq:
        w, now = heapq.heappop(pq)

        if visited[now]:
            continue

        visited[now] = True
        total += w

        for nw, nxt in graph[now]:
            if not visited[nxt]:
                heapq.heappush(pq, (nw, nxt))

    return total


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((c, e))
        graph[e].append((c, s))

    ans = prim(graph, n, 1)

    print(f'#{tc} {ans}')