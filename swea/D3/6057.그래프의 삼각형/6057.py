T = int(input())
for tc in range(1, T+1):
    n, m = map(int ,input().split())

    #인접행렬 만들거다.
    arr = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a][b] = True
        arr[b][a] = True

    cnt = 0

    #i < j < k라고 명시해놨으니 그대로 적자.
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            #경로가 있는 경우에만 파고들면 된다.
            if arr[i][j]:
                for k in range(j + 1, n + 1):
                    if arr[j][k] and arr[k][i]:
                        cnt += 1

    print(f'#{tc} {cnt}')