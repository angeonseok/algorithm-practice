T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = n - 2
    for i in range(1, n-1):
        a, b, c = arr[i-1], arr[i], arr[i+1]
        if max(a, b, c) == b or min(a, b, c) == b:
            ans -= 1
            
    print(f'#{tc} {ans}')