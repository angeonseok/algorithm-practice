T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    d = b - a
    ans = 0

    if d < 0 or d == 1:
        ans = -1
    else:
        ans = d // 2 if d % 2 == 0 else (d - 1) // 2

    print(f'#{tc} {ans}')