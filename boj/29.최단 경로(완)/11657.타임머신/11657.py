import sys
input = sys.stdin.readline

INF = 10**18

#음수 간선이 존재하는 경우, 다익스트라는 최단거리 보장이 안됨.
#벨만 포드 써야됨
def bellman_ford(n, edges, start):
    dist = [INF] * (n+1)
    dist[start] = 0

    #v-1번 완화
    #v-1번 돌리면서 간선 간 거리를 점점 줄여나가기
    for _ in range(n-1):
        update = False
        for u, v, w in edges:

            #갈 수 있을 때 만 ㅇㅇ
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                update = True
        
        #이번 라운드에서 변화없으면 더 돌릴 필요 없음
        if not update:
            break
    
    #v-1번 완화 이후 한 번 더 간선 전체를 돈다.
    #완화 다 했는데 또 줄어? > 음수인 사이클 존재
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            return None, True
        
    return dist, False

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

dist, cycle = bellman_ford(n, edges, 1)

#음수 사이클이 존재한다면
if cycle:
    print(-1)

#없으면 값 출력. 도달 불가능하면 -1
else:
    for i in range(2, n+1):
        print(dist[i] if dist[i] != INF else -1)