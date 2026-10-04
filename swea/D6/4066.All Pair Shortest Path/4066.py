INF = 10**18

#아슬아슬하게 플로이드 될거같음
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

    arr = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        arr[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        #중복이 여러개 들어오나
        if arr[a][b] > c:
            arr[a][b] = c

    floyd(arr, n)

    #ㅋㅋ
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == INF:
                arr[i][j] = -1

    print(f'#{tc}', end= " ")
    for i in range(1, n + 1):
        print(*arr[i][1:], end= " ")
    print()