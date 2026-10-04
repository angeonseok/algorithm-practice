INF = 10**18

#플로이드
def floyd(arr, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if arr[i][k] == INF:
                continue

            for j in range(1, n + 1):
                if arr[k][j] == INF:
                    continue

                nd = arr[i][k] + arr[k][j]
                if nd < arr[i][j]:
                    arr[i][j] = nd


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    #문제에서 자기 자신으로 돌아오는 사이클을 물어봐서 따로 처리 안함
    field = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        field[s][e] = c

    floyd(field, n)

    ans = INF
    #자신으로 돌아오는 사이클 중 최소 거리
    for i in range(1, n + 1):
        ans = min(ans, field[i][i])

    print(f'#{tc} {ans}')