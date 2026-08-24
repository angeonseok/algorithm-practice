T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    ans = float('inf')
    r = 1

    #최대한 정사각형으로 보겠다. n = r * c, n과 가장 가까운 제곱수까지
    while r * r <= n:
        #^^
        for c in (r, n // r):
            ans = min(ans, a * abs(r - c) + b * (n - r * c))
        r += 1

    print(f'#{tc} {ans}')