import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))

    prefix = [0] * (k + 1)
    for i in range(1, k+1):
        prefix[i] = prefix[i-1] + arr[i-1]
    
    INF = 10**18
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    
    #현재 보는 구간 길이 기준
    for length in range(2, k+1):
        for i in range(1, k + 2 - length):
            r = i + length - 1
            dp[i][r] = INF

            total = prefix[r] - prefix[i-1]

            #m기준 왼쪽합 + 오른쪽 합 + 둘 합치는 비용
            for m in range(i, r):
                dp[i][r] = min(dp[i][r], dp[i][m] + dp[m+1][r] + total)

    #1~끝까지 합친 값 출력
    print(dp)
    print(dp[1][-1])