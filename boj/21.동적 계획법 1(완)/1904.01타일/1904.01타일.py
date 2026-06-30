#식은 금방 나오는데 메모리 터졌다
import sys
input = sys.stdin.readline

n = int(input())

#1. n + 1 곱했다가 터졌다.
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

#2. 구하면서 계속 안나눠주니 터졌다.
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])