import sys
import heapq
input = sys.stdin.readline

INF = 10**18

def dijkstra(n, graph, start):
    dist = [INF] * (n+1)
    dist[start] = 0

    pq = [(0,start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int,input().split())
    s, g, h = map(int,input().split())
    
    #양방향 그래프
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    #후보지
    cand = [int(input()) for _ in range(t)]

    s_route = dijkstra(n, graph, s)
    c_route_g = dijkstra(n, graph, g)
    c_route_h= dijkstra(n, graph, h)

    ans = []
    for i in cand:

        #g - h를 경유하면서 후보지로 가는 경우를 구하고
        route1 = s_route[g] + c_route_g[h] + c_route_h[i]
        route2 = s_route[h] + c_route_h[g] + c_route_g[i]

        #경유하는 루트가 시작지점기준으로 최단루트가 맞으면 정답
        if s_route[i] == route1 or s_route[i] == route2:
            ans.append(i)
    
    ans.sort()
    print(*ans)