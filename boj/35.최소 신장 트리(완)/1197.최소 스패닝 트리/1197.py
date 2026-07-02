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
        
        #여기를 굳이 케이스를 나눠야하나 하는 생각이 드네
        if rank[ra] < rank[rb]:
            parent[ra] = rb

        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        
        else:
            parent[rb] = ra
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

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

total, cnt = kruskal(v, edges)
print(total)

#2.프림
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

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

total, cnt = prim(v, graph)
print(total)