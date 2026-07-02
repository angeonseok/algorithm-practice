import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
q = deque()
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 0
        
        #갈 수 없는 곳은 0 처리
        elif arr[i][j] == 0:
            visited[i][j] = 0

while q:
    x, y = q.popleft()

    for dir in dirs:
        nx, ny = x + dir[0], y + dir[1]

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if arr[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

for row in visited:
    print(*row)