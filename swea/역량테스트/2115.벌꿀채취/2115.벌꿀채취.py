#조건을 만족하는 부분집합을 찾고 최대 이익 계산
def profit(idx, total, cur_sum, arr):
    global best

    if total > c:
        return

    if idx == m:
        best = max(best, cur_sum)
        return

    profit(idx + 1, total, cur_sum, arr)
    profit(idx + 1, total + arr[idx], cur_sum + arr[idx] ** 2, arr)


T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #각 좌표별 최대 이익을 저장해둘 예정
    arr_profit = [[0] * (n - m + 1)  for _ in range(n)]
    
    #좌표 기준으로 구간 찾고, 그 구간 내 최대 이익 계산
    for i in range(n):
        for j in range(n - m + 1):
            best = 0
            seg = arr[i][j:j+m]
            profit(0, 0, 0, seg)
            arr_profit[i][j] = best
    
    ans = 0

    #첫번째 노동자
    for i1 in range(n):
        for j1 in range(n - m + 1):

            #두번째 노동자
            for i2 in range(n):
                for j2 in range(n - m + 1):

                    #서로 같은 행에서 구간 겹치면 조건 위배
                    if i1 == i2 and abs(j1 - j2) < m:
                        continue

                    ans = max(ans, arr_profit[i1][j1] + arr_profit[i2][j2])
    
    print(f"#{tc} {ans}")