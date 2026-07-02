import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

#쓰니까 나옴
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    a = int(input())
    print(dp[a])