import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

#그래프에 간선 가중치도 포함시키기
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w= map(int,input().split())
    graph[u].append((v,w))

#시작점 > 각 정점까지 최단 거리 정보 받기
INF = 10 ** 18
dist = [INF] * (V + 1)
dist[start] = 0

#(시작점과의 거리, 정점) 힙에 담기
pq = [(0,start)]

#다익스트라는 힙을 활용
while pq:
    d, u = heapq.heappop(pq)
    
    #dist는 최신 정보가 들어감. d와 dist가 다르면 구버전이니 스킵
    if d != dist[u]:
        continue
    
    #거리정보 갱신
    for v, w in graph[u]:
        nd = d + w

        #갱신 가능하면 힙에 다시 넣자
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

ans = []
for i in range(1, V+1):
    if dist[i] == INF:
        ans.append("INF")
    else:
        ans.append(str(dist[i]))

print("\n".join(ans))