T = int(input())
for tc in range(1, T+1):
    n, l = map(int, input().split())

    arr = [(map(int, input().split())) for _ in range(n)]

    #dp[l] = l칼로리일 때 최대 점수
    dp = [0] * (l + 1)

    #점수와 칼로리
    for t, k in arr:

        #역순으로 해서 중복 방지. k값 넣을 수 있는 범위까지만 따진다.
        for i in range(l, k - 1, -1):

            #현재 점수 vs k칼로리 더하기 전 점수에 k 칼로리 점수 더한 값
            dp[i] = max(dp[i], dp[i - k] + t)

    print(f'#{tc} {max(dp)}')