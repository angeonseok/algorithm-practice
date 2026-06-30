import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

#이전에 선택한 색에 따라 다르게 저장할 예정
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = rgb[0]

#현재 결과를 이전에 선택한 값에 따라 다르게 저장
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + rgb[i][0], dp[i-1][2] + rgb[i][0])  #빨강을 선택했을 때
    dp[i][1] = min(dp[i-1][0] + rgb[i][1], dp[i-1][2] + rgb[i][1])  #초록을 선택했을 때
    dp[i][2] = min(dp[i-1][0] + rgb[i][2], dp[i-1][1] + rgb[i][2])  #파랑을 선택했을 때

print(min(dp[n-1]))