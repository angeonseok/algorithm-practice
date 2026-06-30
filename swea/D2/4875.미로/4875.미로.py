dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(i, j):
    stack = []
    visited[i][j] = 1
    stack.append((i, j))

    while stack:
        x, y = stack.pop()

        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            if arr[nx][ny] == 3:
                return 1
            
            if visited[nx][ny] == 0 and arr[nx][ny] != 1:
                visited[nx][ny] = 1
                stack.append((nx,ny))
    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                ans = dfs(i,j)

    print(f"#{tc} {ans}")