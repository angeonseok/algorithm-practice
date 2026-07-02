#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):
    parent = list(range(v+1))
    rank = [0] * (v+1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # def find(x):
    #     while parent[x] != x:
    #         parent[x] = parent[parent[x]]
    #         x = parent[x]
    #     return x

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False
        
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
            if cnt == v - 1:
                break

    return total, cnt

n = int(input())
point = []

for _ in range(n):
    a, b = map(float, input().split())
    point.append((a, b))

#가중치를 직접 계산해서 edge 생성
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = ((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5
        edges.append((d, i+1, j+1))

total, cnt = kruskal(n, edges)
print(f"{total:.2f}")

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start = 1):
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

n = int(input())

#크루스칼보다 더 힘들게 그래프 만든거 같은데..
point = []
for i in range(n):
    a, b = map(float, input().split())
    point.append((a, b))

#temp없이 그래프를 한번에 만드는게 더 좋을 듯
temp = []
for i in range(n):
    for j in range(i+1, n):
        d = ((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5
        temp.append((d, i+1, j+1))

graph = [[] for _ in range(n+1)]
for d, a, b in temp:
    graph[a].append((d, b))
    graph[b].append((d, a))

total, cnt = prim(n, graph)
print(f"{total:.2f}")