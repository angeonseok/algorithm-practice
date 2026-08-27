T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    month = list(map(int, input().split()))

    #애초에 1개월 비용 리스트 만들 때, 일일권과 1개월권 가격 비교를 해
    month_cost = [min(month[i] * cost[0], cost[1]) for i in range(12)]

    #dp[i] == i월까지 비용 총합
    dp = [0] * 13

    for i in range(1, 13):
        # 인덱스 차이 생각해야됨 
        dp[i] = month_cost[i - 1] + dp[i - 1]

        #3월부터는 3개월권 가격까지 비교해야됨
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + cost[2])

    #12월까지 비용 vs 연간회원권
    dp[12] = min(dp[12], cost[3])

    print(f'#{tc} {dp[12]}')