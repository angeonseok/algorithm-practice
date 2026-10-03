import heapq

def prim(graph, v, start):
    visited = [False] * (v + 1)
    pq = [(0, start)]
    total = 0
    cnt = 0

    while pq and cnt < v:
        w, now = heapq.heappop(pq)

        if visited[now]:
            continue

        visited[now] = True
        total += w
        cnt += 1

        for nw, nxt in graph[now]:
            if not visited[nxt]:
                heapq.heappush(pq, (nw, nxt))

    return total

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))

    ans = prim(graph, v, 1)
    print(f'#{tc} {ans}')