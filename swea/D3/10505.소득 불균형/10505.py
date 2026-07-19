T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    avg = int(sum(arr) / n)
    cnt = 0
    for i in arr:
        if i <= avg:
            cnt += 1
    
    print(f'#{tc} {cnt}')