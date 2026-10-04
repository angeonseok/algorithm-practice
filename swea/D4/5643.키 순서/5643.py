#플로이드로 모든 이동경로 가능 여부 계산
def floyd(arr, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            ik = arr[i][k]

            if not ik:
                continue
            
            for j in range(1, n + 1):
                if arr[k][j]:
                    arr[i][j] = 1


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    m = int(input())

    field = [[0] * (n + 1) for _ in range(n + 1)]


    for _ in range(m):
        a, b = map(int, input().split())
        field[a][b] = 1

    floyd(field, n)

    ans = 0
    for i in range(1, n + 1):
        cnt = 0

        #이동 가능이면 개수 세기
        for j in range(1, n + 1):
            if field[i][j] or field[j][i]:
                cnt += 1

        #한 행의 모든 점이 이동가능하면 개수 +
        if cnt == n - 1:
            ans += 1

    print(f'#{tc} {ans}')