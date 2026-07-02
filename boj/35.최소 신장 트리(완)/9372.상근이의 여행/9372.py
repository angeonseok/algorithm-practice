#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):

    #rank기준으로 union 할거임
    parent = list(range(v+1))
    rank = [0] * (v + 1)

    #크루스칼은 유니온 파인드로 사이클 생기나 체크하면서 간선 고른다.
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    #반복문버전도 알아둬라
    # def find(x):
    #     while parent[x] != x:
    #         parent[x] = parent[parent[x]]
    #         x = parent[x]
    #     return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        
        else:
            parent[rb] = ra
            rank[ra] += 1

        return True
    
    #비용기준으로 정렬
    edges.sort()
    total = 0
    cnt = 0       #선택한 간선 수 카운팅

    #싼 간선부터 보면서 합칠 수 있으면 채택
    for w, a, b in edges:
        if union(a, b):
            total += w
            cnt += 1

            #간선 v-1개면 트리 완성이라 더 볼 필요없다.
            if cnt == v - 1:
                break
    
    return total, cnt

T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    edges = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((0, a, b))
    
    total, cnt = kruskal(n, edges)

    print(cnt)

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start=1):
    visited = [False] * (v+1)
    pq = [(0, start)]
    total = 0
    cnt = 0         #mst에 포함된 정점 개수

    #힙 내용물 꺼내면서
    while pq and cnt < v:
        w, u = heapq.heappop(pq)
        
        #방문한 노드에 대해서는 처리 x
        if visited[u]:
            continue

        #방문처리하고 거리 합치기
        visited[u] = True
        total += w 
        cnt += 1

        #정접과 연결된 다른 정점들 중 방문 안한거 있으면 힙에 담기
        for nw, nu in graph[u]:
            if not visited[nu]:
                heapq.heappush(pq, (nw, nu))

    #그래프가 연결이면 cnt == v 아니면 문제가 있다.
    return total, cnt

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((0,b))
        graph[b].append((0,a))
    
    total, cnt = prim(n, graph)
    print(cnt-1)