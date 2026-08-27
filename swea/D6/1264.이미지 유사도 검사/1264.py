T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x = input().strip()
    y = input().strip()

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    #그냥 lcs문제
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #출력 양식 맞추기
    print(f'#{tc} {100 * dp[n][n]/n:.2f}')