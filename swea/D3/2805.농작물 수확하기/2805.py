T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    mid = n // 2
    ans = 0
    for i in range(n):
        diff = abs(mid - i)
        ans += sum(arr[i][diff: n - diff])
    
    print(f'#{tc} {ans}')