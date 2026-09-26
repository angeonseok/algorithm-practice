T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] * (k + 1)

    #즐거운 냅색
    for v, c in arr:
        for i in range(k, v - 1, -1):
            dp[i] = max(dp[i], dp[i - v] + c)

    print(f'#{tc} {dp[k]}')