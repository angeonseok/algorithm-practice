from collections import deque

#상하좌우. (0, 0)은 인덱스 맞추기용으로 넣음
dirs = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

#각 파이프별 이동가능 방향
pipe = {
    1 : (1, 2, 3, 4),
    2 : (1, 2),
    3 : (3, 4),
    4 : (1, 4),
    5 : (2, 4),
    6 : (2, 3),
    7 : (1, 3)
}

#이동방향별 이동가능 파이프. 상하좌우순
ok = {
    (-1, 0) : (1, 2, 5, 6),
    (1, 0) : (1, 2, 4, 7),
    (0, -1) : (1, 3, 4, 5),
    (0, 1) : (1, 3, 6, 7),
}

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1

    while q:
        i, j = q.popleft()

        #visited 에 시간 박으면서 갈거라 이래도 됨
        if visited[i][j] == l:
            continue

        for p in pipe[arr[i][j]]:
            di, dj = dirs[p]
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m:

                #탐색한 칸이랑 현재 칸이 이어져있는지 확인도 해줘야됨.
                if arr[ni][nj] in ok[(di, dj)] and not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    cnt += 1
                    q.append((ni, nj))

    return cnt

T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = bfs(r, c)
    print(f'#{tc} {ans}')