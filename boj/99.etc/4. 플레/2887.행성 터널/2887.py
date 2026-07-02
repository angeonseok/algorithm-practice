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
    
    def find2(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
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

            if cnt == v-1:
                break
    
    return total, cnt

n = int(input())

#edge 생성할때 n 수 안보고 전부 연결시키다가 메모리 터짐
#문제에서 거리는 3개의 축 중 차가 최소인 것으로 줘서 x,y,z 순으로 정렬해서 인접한 애들만 연결함
#일단 그러니 풀림

#포인트 저장할 때, 이 포인트가 몇번째 행성인지도 저장해야됨.
#정렬하고 이 포인트가 어느 행성인지 알아야지.
point = []
for i in range(n):
    x, y, z = map(int, input().split())
    point.append((x,y,z,i+1))

edges = []
#1. x정렬기준 인접한 애들 연결
point.sort(key=lambda x : x[0])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(x1 - x2)
    edges.append((d, a, b))

#2. y정렬 기준 인접한 애들 연결
point.sort(key=lambda x : x[1])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(y1 - y2)
    edges.append((d, a, b))

#3. z정렬 기준 인접한 애들 연결
point.sort(key=lambda x : x[2])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(z1 - z2)
    edges.append((d, a, b))

total, cnt = kruskal(n, edges)
print(total)

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

point = []
for i in range(n):
    x, y, z = map(int, input().split())
    point.append((x,y,z,i+1))

graph = [[] for _ in range(n+1)]

#x기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[0])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(x1-x2)
    graph[a].append((d, b))
    graph[b].append((d, a))

#y기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[1])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(y1-y2)
    graph[a].append((d, b))
    graph[b].append((d, a))

#z기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[2])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(z1-z2)
    graph[a].append((d, b))
    graph[b].append((d, a))

total, cnt = prim(n, graph)
print(total)