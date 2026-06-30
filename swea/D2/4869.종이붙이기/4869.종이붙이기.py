def p_case(i):
    if i == 1:
        return 1
    if i == 2:
        return 3
    if i >= 3:
        return 2 * p_case(i-2) + p_case(i-1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = n // 10
    print(f'#{tc} {p_case(n/10)}')