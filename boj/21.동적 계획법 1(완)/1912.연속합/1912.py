import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

#num과 인덱스 맞추기
dp = [0] * n
dp[0] = num[0]

#dp[i] : i를 포함한 
for i in range(1, n):
    dp[i] = max(num[i], dp[i-1] + num[i])

print(max(dp))