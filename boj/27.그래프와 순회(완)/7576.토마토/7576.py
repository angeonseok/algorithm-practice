import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

#첫 입력부터 모든 토마토가 익은 상태(room에 0이 없음)
if sum(row.count(0) for row in room) == 0:
    print(0)
else:
    q = deque()
    #첫 시작지점 모으기
    for i in range(n):
        for j in range(m):
            if room[i][j] == 1:
                q.append((i,j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        
        for dir in ((0,1), (1,0), (0,-1),(-1,0)):
            nx,ny = x + dir[0], y + dir[1]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                room[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1  #전파
                q.append((nx,ny))

    #작업 이후 모든 토마토가 익으면
    if sum(row.count(0) for row in room) == 0:
        
        #최대일수는 visited에 적혀있다
        result = max(max(row) for row in visited)
        print(result)
    else:
        print(-1)   #아님말고