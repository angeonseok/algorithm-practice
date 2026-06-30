#bfs로 푸는거 같은데
#모든 경로를 따지길래 플로이드 워셜로 해봄
import sys
input = sys.stdin.readline

INF = 10**18

def floyd(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][k] == INF:
                continue   

            ik = dist[i][k]
            for j in range(1, n+1):
                nd = ik + dist[k][j]

                if nd < dist[i][j]:
                    dist[i][j] = nd

n, m = map(int, input().split())
dist = [[INF] * (n + 1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

floyd(n, dist)

#모든 친구들과 연결거리가 가장 짧은 친구가 정답
#번호 작은 놈 우선
sum_dist = INF
ans = 0

for i in range(1, n+1):
    temp = sum(dist[i][1:])
    
    if sum_dist > temp:
        sum_dist = temp
        ans = i

print(ans)