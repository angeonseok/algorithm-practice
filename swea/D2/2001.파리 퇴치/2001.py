T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]
    
    ans = 0
    for i in range(m, n+1):
        for j in range(m, n+1):
            temp = prefix[i][j] - prefix[i-m][j] - prefix[i][j-m] + prefix[i-m][j-m]
            ans = max(ans, temp)
    
    print(f"#{tc} {ans}")