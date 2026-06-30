import sys
input = sys.stdin.readline

n = int(input().rstrip())

#dp랑 인덱스 통일
wine = [0] * (n + 1)
for i in range(1, n + 1):
    wine[i] = int(input().strip())

#ㅎㅇ
dp = [0] * (n + 1)

if n >= 1:
    dp[1] = wine[1]

if n >= 2:
    dp[2] = wine[1] + wine[2]

#여기서도 조건 3가지 중 가장 큰 놈으로 해야지
if n >= 3:
    dp[3] = max(wine[1] + wine[2], wine[1] + wine[3], wine[2] + wine[3])

#점화식 
for i in range(4, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1] )

print(dp[n])