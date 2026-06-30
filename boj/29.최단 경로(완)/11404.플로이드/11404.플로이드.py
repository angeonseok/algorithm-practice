import sys
input = sys.stdin.readline

INF = 10**18

#dist[i][j] = i -> j 최단거리
#k를 중간에 거쳐도 되는 정점으로 하나씩 허용하며 업데이트
def floyd_warshall(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):

            #애초에 i -> k가 불가능하면 무시
            if dist[i][k] == INF:
                continue

            ik = dist[i][k]

            #기존 경로 대비 우회경로가 더 빠르면 갱신
            for j in range(1, n+1):
                nd = ik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd


n = int(input())
m = int(input())

#거리 행렬 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신 가는 비용은 0으로
for i in range(n + 1):
    dist[i][i] = 0

#입력 받은 애들 넣어주고
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

#모든 쌍 최단거리 계산
floyd_warshall(n, dist)

#도달 불가한 경우 0으로 변환해서 출력
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append("0" if dist[i][j] == INF else str(dist[i][j]))
    print(" ".join(row))
