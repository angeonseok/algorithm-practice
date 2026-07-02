import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
trace = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:

            #진짜 길이 늘어날 때만 갱신
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                trace[i] = j
            else:
                dp[i] = dp[i]

#dp[i] : i에서 끝나는 lis 길이
#맨 끝놈이 최대인 보장이 없다
idx = dp.index(max(dp))
ans = []

#최대 길이를 알고 있어서 좀 더 편하네
while len(ans) != max(dp):
    ans.append(arr[idx])
    idx = trace[idx]

print(max(dp))
print(*reversed(ans))   #ans는 역순으로 저장되어있음