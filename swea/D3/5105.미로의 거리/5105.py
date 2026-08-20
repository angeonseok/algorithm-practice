from collections import deque

def find_point(arr, n, k):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                return i, j


def bfs(i, j):
    visited = [[-1] * n for _ in range(n)]
    q = deque([(i, j)])
    visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in ((0,1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    si, sj = find_point(arr, n, 2)
    visited = bfs(si, sj)

    ei, ej = find_point(arr, n, 3)
    ans = visited[ei][ej] - 1 if visited[ei][ej] != -1 else 0
    print(f'#{tc} {ans}')