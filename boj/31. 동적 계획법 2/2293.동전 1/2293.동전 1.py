n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1   #동전을 안쓰는 1가지 경우만 있음

#동전 저장할 배열을 안만들어도 되겠더라
for _ in range(n):
    a = int(input().strip())

    #i-a원을 만드는 방법에 지금 동전을 하나 붙이는 느낌
    for i in range(a, k+1):
        dp[i] += dp[i - a]

print(dp[k])