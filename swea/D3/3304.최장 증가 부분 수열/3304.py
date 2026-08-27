T = int(input())
for tc in range(1, T+1):
    a, b = input().split()

    #길이가 같다는 보장이 없음
    n = len(a)
    m = len(b)

    #함 표 그려보셈. a를 세로축, b를 가로축
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    #lcs 즐겁게
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #다 짜놓고 반대로 씀
    print(f'#{tc} {dp[n][m]}')