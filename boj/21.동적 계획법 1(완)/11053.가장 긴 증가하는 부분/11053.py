import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#최소길이가 1임
dp = [1] * n

#i까지를 기준으로
for i in range(n):
    #i 이전 항에 대해
    for j in range(i):
        #arr[i]가 이전 항보다 크다면
        if arr[i] > arr[j]:
            #최대길이를 dp에 저장
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))