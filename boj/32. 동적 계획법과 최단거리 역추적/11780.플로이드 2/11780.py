#기존 역추적들이 이전 값들을 저장했는데
#얘는 다음 경로 값을 저장해야되네
import sys
input = sys.stdin.readline

INF = 10**18

def floyd(n, dist, trace):
    for k in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][k] == INF:
                continue

            for j in range(1, n+1):
                nd = dist[i][k] + dist[k][j]
            
                if dist[i][j] > nd:
                    dist[i][j] = nd
                    trace[i][j] = trace[i][k]   #다음 갈 노드 갱신

def route(i, j, trace):
    #애초에 못가거나, 자기 자신에게 가는 경우
    if trace[i][j] == 0:
        return []

    cur = i
    path = [i]

    #다음 노드 추적
    while cur != j:
        cur = trace[cur][j]
        path.append(cur)
    
    return path
    

n = int(input())
dist = [[INF] * (n + 1) for _ in range(n + 1)]
trace = [[0] * (n+1) for _ in range(n+1)]  

for i in range(1, n + 1):
    dist[i][i] = 0

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    
    if c < dist[a][b]:
        dist[a][b] = c
        trace[a][b] = b     #다음 위치 저장

floyd(n, dist, trace)

#따로 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

#여기도 dist값 안따지고 걍 path 생성 가능여부만으로 하니 좋네
for i in range(1, n+1):
    for j in range(1, n+1):
        path = route(i, j, trace)

        if path:
            print(len(path), *path)
        else:
            print(0)