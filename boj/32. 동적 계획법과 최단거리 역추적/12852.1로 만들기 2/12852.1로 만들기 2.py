import sys
input = sys.stdin.readline

#이전 인덱스 저장용 배열까지 생성
n = int(input())
dp = [0] * (n + 1)
trace = [0] * (n + 1)

#인덱스를 저장하면서 가야하기 떄문에 min 안쓰고 ㅇㅇ
#dp배열에 값을 저장하면서 trace에 이전 인덱스까지 저장
for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    trace[i] = i - 1

    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            trace[i] = i//2

    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            trace[i] = i//3

#역추적 과정
cur = n
ans = []

while cur != 1:
    ans.append(cur)
    cur = trace[cur]

#결과가 1인데 같이 나와야지
ans.append(1)

print(dp[n])
print(*ans)