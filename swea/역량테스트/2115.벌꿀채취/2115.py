#최대 점수 계산
def cal_best(idx, total, value, seg):
    global best

    if total > c:
        return 

    if idx == m:
        best = max(best, value)
        return

    cal_best(idx + 1, total, value, seg)
    cal_best(idx + 1, total + seg[idx], value + seg[idx] ** 2, seg)


T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #칸별 최대점수 미리 계산
    profit = [[0] * (n - m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            best = 0
            cal_best(0, 0, 0, arr[i][j : j + m])
            profit[i][j] = best

    #선택 구역 겹치는지 체크
    ans = 0
    for r1 in range(n):
        for c1 in range(n - m  + 1):
            for r2 in range(r1, n):
                for c2 in range(n - m + 1):
                    if r1 == r2 and abs(c1 -c2) < m:
                        continue

                    ans = max(ans, profit[r1][c1] + profit[r2][c2])

    print(f'#{tc} {ans}')