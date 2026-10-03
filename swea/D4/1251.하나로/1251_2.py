import heapq

def prim(graph, v, start):
    visited = [False] * (v+1)
    pq = [(0, start)]
    total = 0
    cnt = 0

    while pq and cnt < v:
        w, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        total += w
        cnt += 1

        for nxt, w in graph[node]:
            if not visited[nxt]:
                heapq.heappush(pq, (w, nxt))

    return total


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            graph[i].append((j, dist))
            graph[j].append((i, dist))

    ans = prim(graph, n, 0)
    print(f'#{tc} {round(ans * e)}')