import sys
input = sys.stdin.readline

INF = 10**18

#모든 경로의 가능여부 + 행렬형태 자료 > 플로이드 씀
def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue

            ik = dist[i][k]
            for j in range(n):
                nd = ik + dist[k][j]

                if nd < dist[i][j]:
                    dist[i][j] = nd


n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

#연결 안됨 > INF로 표현 변경
for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            dist[i][j] = INF

floyd(n, dist)

#도달 가능한 경우는 1, 아니면 0
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF:
            dist[i][j] = 1
        else:
            dist[i][j] = 0

for row in dist:
    print(*row)