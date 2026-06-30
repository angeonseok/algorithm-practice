import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#뒤집어서 증가하는 수열 만들면 감소하는 수열
r_arr = arr[::-1]

up = [0] * n
down = [0] * n

for i in range(n):
    for j in range(i):

        #증가하는 수열 만들고
        if arr[i] > arr[j]:
            up[i] = max(up[i], up[j] + 1)

        #감소하는 수열 만들고
        if r_arr[i] > r_arr[j]:
            down[i] = max(down[i], down[j] + 1)

dp = [0] * n

# i 까지 증가, 그 이후로 감소해야함. 결과도 1을 더해줘야 맞음
for i in range(n):
    dp[i] = up[i] + down[n - 1 - i] + 1

print(max(dp))