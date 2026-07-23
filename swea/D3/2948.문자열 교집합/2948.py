T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    lst_1 = list(input().split())
    lst_2 = list(input().split())

    o = set(lst_1) | set(lst_2)
    print(f'#{tc} {n + m - len(o)}')