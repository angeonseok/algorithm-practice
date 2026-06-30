#모든 정점 도달 거리의 합 구해야됨
INF = 10**18
 
def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
 
            ik = dist[i][k]
 
            for j in range(n):
                nd = ik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
 
 
T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
 
    arr = tmp[1:]
    n = tmp[0]
 
    dist = []
    for i in range(0, len(arr), n):
        tmp = arr[i:i+n]
        dist.append(tmp)
     
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF
 
    floyd(dist, n)
     
    ans = min(sum(row) for row in dist)
    print(f"#{tc} {ans}")