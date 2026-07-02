#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):
    parent = list(range(v+1))
    rank = [0] * (v+1)
    
    #재귀버전 find
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    #반복문버전 find
    def find2(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False
        
        #ra의 랭크가 무조건 크다고 생각하고싶다.
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra

        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True
    
    edges.sort()
    total = 0
    cnt = 0

    for w, a, b in edges:
        if union(a, b):
            total += w
            cnt += 1

            if cnt == v-1:
                break
    
    return total, cnt

n, m = map(int, input().split())

#먼저 우주신들의 좌표를 순서대로 받고
point = []
for _ in range(n):
    a, b = map(int, input().split())
    point.append((a, b))

#좌표를 통해 각 우주신들의 거리 계산해서 넣기
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = float(((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5)
        edges.append((d, i+1, j+1))

#이미 연결된 신들 번호를 받고, 그 거리를 0으로 하여 저장
for _ in range(m):
    c, d = map(int, input().split())
    edges.append((0, c, d))

total, cnt = kruskal(n, edges)
print(f"{total:.2f}")

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start=1):
    visited = [False] * (v+1)
    pq = [(0, start)]
    total = 0
    cnt = 0

    while pq and cnt < v:
        w, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        visited[u] = True
        total += w
        cnt += 1

        for nw, nu in graph[u]:
            if not visited[nu]:
                heapq.heappush(pq, (nw, nu))
    
    return total, cnt

n, m = map(int, input().split())

point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

#4386처럼 나누지 않고 한번에 그래프 생성
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(i+1, n):
        d = float(((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5)
        graph[i+1].append((d, j+1))
        graph[j+1].append((d, i+1))

#비용 0인 간선 처리도 해주고
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((0, b))
    graph[b].append((0, a))

total, cnt = prim(n, graph)
print(f"{total:.2f}")