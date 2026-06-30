import sys
import heapq
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]

#이번엔 양방향 그래프당
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

#경유지점 저장용
point = list(map(int,input().split()))

INF = 10**18

#3번 해야되기 떄문에 함수로 다익스트라 구현
def dijkstra(n, start, graph):
    dist = [INF] * (n + 1)
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

#시작점 > 모든 정점간 최소거리
d1 = dijkstra(n, 1, graph)

#경유지점 1 > 모든 정점간 최소거리
d2 = dijkstra(n, point[0], graph)

#경유지점 2 > 모든 정점 간 최소거리
d3 = dijkstra(n, point[1], graph)

#루트 1 : 시작점 > 경유지점 1 > 경유지점 2 > 목적지
route1 = d1[point[0]] + d2[point[1]] + d3[n]

#루트 2 : 시작점 > 경유지점 2 > 경유지점 1 > 목적지
route2 = d1[point[1]] + d3[point[0]] + d2[n]

ans = min(route1, route2)
if ans >= INF:
    print(-1)
else:
    print(ans)