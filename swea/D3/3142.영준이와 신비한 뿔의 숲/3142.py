T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    a = n - m
    b = 2 * m - n

    print(f'#{tc} {b} {a}')