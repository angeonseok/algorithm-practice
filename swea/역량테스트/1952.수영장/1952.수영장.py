T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    month = list(map(int, input().split()))

    #일일권 가격만 계산해서 맞추면 된다
    days_cost = [cost[0] * month[i] for i in range(12)]

    #n월까지 총 누적 금액 담아둘 거
    dp = [0] * 13

    for i in range(1, 13):
        #윌 비용 중 싼 놈
        dp[i] = min(days_cost[i - 1], cost[1]) + dp[i - 1]

        #3이후부터는 3개월권 가격을 비교
        if i >= 3: 
            dp[i] = min(dp[i], dp[i-3] + cost[2])
    
    #마지막으로 연간 이용권과 12월까지 누적 금액 비교
    ans = min(dp[12], cost[3])
    print(f"#{tc} {ans}")