import sys
input = sys.stdin.readline

INF = 10**18

#모든 경로를 조사해야됨 -> 플로이드 사용
def floyd(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):

            if dist[i][k] == INF:
                continue

            ik = dist[i][k]

            for j in range(1, n+1):
                if dist[i][j] > ik + dist[k][j]:
                    dist[i][j] = ik + dist[k][j]

n, m = map(int, input().split())

#문제에서는 사이클 중 최소거리를 물어봤으니 따로 작업안함
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
    

floyd(n, dist)

#사이클 중 최소거리 선택
ans = INF
for i in range(n):
    if dist[i][i] < ans:
        ans = dist[i][i]

if ans == INF:
    print(-1)
else:
    print(ans)