def sol(now_i, now_j, depth, cur):
    #시작점 넣은 상태라 6개 더 넣으면 끝
    if depth == 6:
        visited.add(cur)
        return

    #4방향 탐색
    for dir in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = now_i + dir[0], now_j + dir[1]

        #범위만 안넘어가면 넣으면 된다
        if 0 <= ni < 4 and 0 <= nj < 4:
            sol(ni, nj, depth + 1, cur + arr[ni][nj])
    

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]

    visited = set()
    for i in range(4):
        for j in range(4):
            #시작점 하나 넣고 시작
            sol(i, j, 0, arr[i][j])

    print(f'#{tc} {len(visited)}')