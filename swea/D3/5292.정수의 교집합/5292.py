T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    #이거도 집합연산
    sa = set(list(map(int, input().split())))
    sb = set(list(map(int, input().split())))

    ans = sa & sb
    print(f'#{tc} {len(ans)}')