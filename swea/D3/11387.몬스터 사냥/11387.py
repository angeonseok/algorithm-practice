T = int(input())
for tc in range(1, T+1):
    d, l, n = map(int, input().split())

    ans = 0
    for i in range(n):
        ans += d * (100 + i * l) // 100

    print(f'#{tc} {ans}')