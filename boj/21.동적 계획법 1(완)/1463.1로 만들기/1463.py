import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

#dp = n >>> 1 되는 최소 계산 횟수
for i in range(2,n+1):
    
    # 1 뺴는 작업은 시행횟수 1회 추가
    dp[i] = dp[i-1] + 1

    # 2로 나눠지면, 2로 나눈 수의 횟수 +1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3도 마찬가지로
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])