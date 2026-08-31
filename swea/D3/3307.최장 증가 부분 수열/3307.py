T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    #dp[i] = i가 증가수열의 최댓값일 때 길이
    dp = [1] * n

    for i in range(1, n):

        #앞쪽에서 나보다 작은 놈 뒤에 붙이기
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{tc} {max(dp)}')