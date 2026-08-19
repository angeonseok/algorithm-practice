from collections import deque

#방향 설정
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

#좌표찾기
def find_point(arr, n, k):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                return i, j


#ㅈ거운 bfs. deque를 stack으로 하면 dfs
def bfs(i, j):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    visited[i][j] += 1
    q.append((i, j))

    while q:
        x, y= q.popleft()

        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] += 1
                q.append((nx, ny))

    return visited


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    si, sj = find_point(arr, n, 2)
    visited = bfs(si, sj)

    ei, ej = find_point(arr, n, 3)

    ans = 1 if visited[ei][ej] != -1 else 0
    print(f'#{tc} {ans}')