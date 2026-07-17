T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    ans = a + b - 24 if a + b > 23 else a + b
    print(f'#{tc} {ans}')