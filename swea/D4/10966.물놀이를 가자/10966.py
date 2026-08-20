from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    #모든 물 지점 모아야됨
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i, j))
    
    while q:
        x, y = q.popleft()

        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    #합치는거 이렇게 써도됨
    print(f'#{tc} {sum(sum(n) for n in visited)}')