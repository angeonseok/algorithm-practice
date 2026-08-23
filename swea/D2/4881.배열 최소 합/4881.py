def sol(depth, cursum, n):
    global ans

    #현재 합이 지금까지 최솟값보다 크면 더 따질 필요 없음
    if cursum >= ans:
        return

    #안걸러졌으면 얘가 최소겠지
    if depth == n:
        ans = cursum
        return

    for i in range(n):

        #한번도 선택되지 않은 줄에 대해서만 선택
        if i not in visited:
            visited.add(i)
            sol(depth + 1, cursum + arr[depth][i], n)
            visited.remove(i)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 987654321

    #선택지에서 지워야해서 set 씀
    visited = set()
    sol(0, 0, n)

    print(f'#{tc} {ans}')