T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_p = 0
    ans = 0

    for p in reversed(arr):
        if p > max_p:
            max_p = p
        else:
            ans += max_p - p
    
    print(f'#{tc} {ans}')