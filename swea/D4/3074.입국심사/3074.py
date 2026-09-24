T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    time = [int(input()) for _ in range(n)]

    #전체 완료 최소, 최대시간 설정
    lo, hi = 1, min(time) * m

    #파라매트릭 서치
    while lo < hi:
        mid = (lo + hi) // 2

        total = sum(mid // t for t in time)

        #최소 시간을 더 줄일 수 있음
        if total >= m:
            hi = mid

        #최소 시간을 늘려야함
        else:
            lo = mid + 1

    print(f'#{tc} {lo}')