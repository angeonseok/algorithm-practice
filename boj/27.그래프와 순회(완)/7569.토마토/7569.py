#3차원은 머리가 아프다
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int,input().split())

#입력 받는거부터 머리가 아프다
room = [[list(map(int, input().split())) for _ in range(n)] \
       for _ in range(h)]

visited = [[[-1] * m for _ in range(n)] for _ in range(h)]

q = deque()

#찾는거도 머리가 아프다
for i in range(h):
    for j in range(n):
        for k in range(m):
            if room[i][j][k] == 1:
                q.append((i,j,k))
                visited[i][j][k] = 0

while q : 
    i, j, k = q.popleft()

    #방향 결정은 사람을 미치게 한다
    for dir in ((1, 0, 0), (0, 1, 0), (0, 0 ,1),\
                 (-1, 0, 0), (0, -1, 0), (0, 0, -1)):
        ni, nj, nk = i + dir[0], j + dir[1], k + dir[2]

        #조건은 또 왜이런데
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m :
            if room[ni][nj][nk] == 0 and visited[ni][nj][nk] == -1:
                visited[ni][nj][nk] = visited[i][j][k] + 1
                q.append((ni,nj,nk))

ans = 0  #모두 다 익은 경우에는 0 출력됨
flag = True #플래그를 걸어

for i in range(h):
    for j in range(n):
        for k in range(m):
            #익을 수 없는 놈이 있다면 바로 -1
            if room[i][j][k] == 0 and visited[i][j][k] == -1:
                flag = False
            #아니면 최대
            else:
                ans = max(ans, visited[i][j][k])

if flag is False:
    print(-1)
else:
    print(ans)