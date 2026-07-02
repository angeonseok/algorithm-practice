#다익스트라에서 dp냄새가 난다
import sys
import heapq
input = sys.stdin.readline

#기름값 인덱스 통일을 위해 더미 추가
n, m = map(int, input().split())
oil_cost = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

#거리를 기름값에 따라 다르게 저장할라고 2차원 배열씀
#처음엔 defaultdict 썼는데, 못알아먹겠어서 갈아엎음
INF = 10**18
dist = [[INF] * (max(oil_cost) + 1) for _ in range(n+1)]

#기름값 정보까지 넣고 시작
dist[1][oil_cost[1]] = 0
pq = [(0, 1, oil_cost[1])]

while pq:
    d, u, oil = heapq.heappop(pq)

    #목적지 도달했으면 바로 종료하기
    #이거 넣으니까 100점나옴
    if u == n:
        break
    
    if d > dist[u][oil]:
        continue
    
    #현재 기름값으로 계산
    #그 후 기름값 갱신
    for v, w in graph[u]:
        nd = d + w * oil
        new_oil = min(oil, oil_cost[v])

        if nd < dist[v][new_oil]:
            dist[v][new_oil] = nd
            heapq.heappush(pq, (nd, v, new_oil))

#무조건 도착한다는 보장 있어서 이렇게 함
print(min(dist[n]))