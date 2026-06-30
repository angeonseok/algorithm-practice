import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]

#벽을 부쉈는지 아닌지 체크하기 위해 3차원 배열로 생성
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

#큐에 벽을 부순 정보(status:0 안부숨, 1 부숨)도 함께 집어넣기
def bfs(start_x, start_y, status):
    q = deque()
    q.append((start_x, start_y, status))
    visited[start_x][start_y][0] = 1

    while q:
        x, y, status = q.popleft()
        for dir in ((0,1),(1,0),(0,-1),(-1,0)):
            nx,ny = x + dir[0], y + dir[1]

            #여기까지는 익히 맛보던 bfs
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and visited[nx][ny][status] == 0:
                    visited[nx][ny][status] = visited[x][y][status] + 1
                    q.append((nx,ny,status))

                #벽을 만나고, 아직 벽을 안부쉈으면(status=0) 부수고(status=1) 진행
                elif maze[nx][ny] == 1 and visited[nx][ny][1] == 0 and status == 0:
                    visited[nx][ny][1] = visited[x][y][status] + 1
                    q.append((nx,ny,1))

bfs(0,0,0)

a = visited[n-1][m-1][0]
b = visited[n-1][m-1][1]

#도착불가능
if a == 0 and b == 0:
    print(-1)
#벽을 뚫었을 때 만 도달 가능
elif a == 0:
    print(b)
#왜뚫음?
elif b == 0:
    print(a)
#두 가지 경우 다 가능하면 최소경로
else:
    print(min(a, b))