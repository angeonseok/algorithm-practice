T = int(input())
for tc in range(1, T+1):
    l, u, x = map(int, input().split())

    ans = 0
    if x < l:
        ans = l - x
    elif x > u:
        ans = -1
    else:
        ans = 0

    print(f'#{tc} {ans}')