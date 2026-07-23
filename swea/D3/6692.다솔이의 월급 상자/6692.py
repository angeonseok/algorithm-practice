T = int(input())
for tc in range(1, T+1):
    n = int(input())

    ans = 0
    for i in range(n):
        a, b = map(float, input().split())
        ans += a * b

    print(f'#{tc} {ans}')