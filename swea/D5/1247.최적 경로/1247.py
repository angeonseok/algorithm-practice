#거리 계산용
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#현재 손놈 번호, 현재까지 총 거리, 만난 손놈 수, 직전 손놈 위치
def sol(cur, cursum, cnt, prev):
    global ans

    #맨날 보던 맛
    if cursum >= ans:
        return

    #마지막 손놈 본 후에는 집가는 거리까지 포함
    if cnt == n:
        total = cursum + dist(home, customer[cur])

        if total < ans:
            ans = total
        return

    #손놈 조뻉이 돌리기
    for i in range(n):
        if i not in visited:
            visited.add(i)
            sol(i, cursum + dist(prev, customer[i]), cnt + 1, customer[i])
            visited.remove(i)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tmp = list(map(int, input().split()))

    #입력 드럽네
    home = (tmp[0], tmp[1])
    company = (tmp[2], tmp[3])
    customer = [(tmp[i], tmp[i+1]) for i in range(4, len(tmp), 2)]

    #방문 여부 체크
    visited = set()
    ans = float('inf')
    sol(0, 0, 0, company)

    print(f'#{tc} {ans}')