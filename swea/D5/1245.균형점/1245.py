T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tmp = list(map(int, input().split()))

    point = [(tmp[i], tmp[n + i]) for i in range(n)]
    point.sort()

    ans = []

    #균형점 n-1개라 해서 인접 점 사이에 균형점 때려박을 예정
    for i in range(n - 1):
        lo, hi = point[i][0], point[i + 1][0]

        #100번정도면 충분할라나
        for _ in range(100):
            mid = (hi + lo) / 2
            f = 0.0

            #공통되는 애들 제외하고 따지기
            for d, m in point:
                if d < mid:
                    f += m / (mid - d) ** 2
                else:
                    f -= m / (mid - d) ** 2

            #총합이 0보다 크면 왼쪽 구간을 땡기기
            if f > 0:
                lo = mid

            #작으면 그 역으로
            else:
                hi = mid

        ans.append(mid)

    print(f'#{tc}', end=" ")
    for x in ans:
        print(f'{x:.10f}', end = " ")
    print()