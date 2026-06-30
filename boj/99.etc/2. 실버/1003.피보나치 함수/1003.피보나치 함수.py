#재귀했다가 터짐
import sys
input = sys.stdin.readline

n = int(input())

#그래서 dp로 처리했네
dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for _ in range(n):
    a = int(input())
    print(dp[a][0], dp[a][1])