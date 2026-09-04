T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    #두 집합의 교집합
    sa = set([input() for i in range(a)])
    sb = set([input() for i in range(b)])

    ab = sa & sb
    print(f'#{tc} {len(ab)}')