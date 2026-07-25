T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    max_p = min(a, b)
    min_p = max(0, a + b - n)
    print(f'#{tc} {max_p} {min_p}')