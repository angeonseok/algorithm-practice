#식이 이게 맞나 모르겠네
def ok(k, mid):
    for i in range(n):
        if time[i] > mid:
            k -= team[i] - mid // food[i]
        if k < 0:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    team = sorted(list(map(int, input().split())))
    food = sorted(list(map(int, input().split())), reverse=True)

    #미리 점수 최적화 갈겨놓기
    time = [team[i] * food[i] for i in range(n)]

    #이분탐색 ㄱ
    lo, hi = 0, max(time)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(k, mid):
            hi = mid
        else:
            lo = mid + 1

    print(f'#{tc} {lo}')