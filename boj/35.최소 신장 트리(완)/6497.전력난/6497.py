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

#입력양식 안지켰다가 틀림
while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    
    #전체 비용 - 최소 연결 비용 = 최대 절약 비용
    t_cost = 0

    edges = []
    for _ in range(n):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))
        t_cost += w

    total, cnt = kruskal(m, edges)
    print(t_cost-total)

#2. 프림
import sys
import heapq
input = sys.stdin.readline

#문제마다 시작번호를 잘 봐야 할 듯. 이번 문제는 시작번호가 0번
def prim(v, graph, start=0):
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

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    
    t_cost = 0
    graph = [[] for _ in range(m+1)]
    for _ in range(n):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
        t_cost += w
    
    total , cnt = prim(m, graph)
    print(t_cost-total)
