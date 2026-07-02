import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

#문제에서 시작 지점을 줌
q = deque()
visited[0][0] = 1
q.append((0,0))

#bfs 탐색
while q : 
    x, y = q.popleft()  

    for dir in [(0,1), (1,0), (0, -1), (-1, 0)]:
        nx = x + dir[0]
        ny = y + dir[1]

        #조건을 잘 따지자
        if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

print(visited[n-1][m-1])