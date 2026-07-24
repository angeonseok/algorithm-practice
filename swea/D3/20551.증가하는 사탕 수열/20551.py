T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    if b <= 1 or c <= 2:
        print(f'#{tc} -1')
        continue

    ans = 0
    if b >= c:
        ans += (b - c) + 1
        b = c - 1

    if a >= b:
        ans += (a - b) + 1

    print(f'#{tc} {ans}')