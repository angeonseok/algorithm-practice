def sol(cur, cursum, cnt):
    global ans

    #가망없으면 걸러
    if cursum >= ans:
        return

    #1구역 제외 다 고르면
    if cnt == n - 1:

        #1구역 가는 비용 더해서 비교
        total = cursum + arr[cur][0]
        if total < ans:
            ans = total
        return

    #맨날 맛보는 그 맛
    for i in range(1, n):
        if i not in visited:
            visited.add(i)
            sol(i, cursum + arr[cur][i], cnt + 1)
            visited.remove(i)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #1구역을 맨 마지막에 고를 예정
    visited = set()
    visited.add(0)
    ans = float('inf')
    sol(0, 0, 0)

    print(f'#{tc} {ans}')