T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = 10**18
    for s in range(7):
        cnt = 0
        days = 0
        
        while cnt != n:
            if lst[(s + days) % 7] == 1:
                cnt += 1
            days += 1
        ans = min(ans, days)
    
    print(f'#{tc} {ans}')