def dfs(x, y):
    stack = []
    stack.append((x,y))
    home[x][y] = 0
    cnt = 1 #단지 수 측정

    while stack:
        x, y = stack.pop()
        for dir in ((0,1), (1,0),(0,-1),(-1,0)):
            nx, ny = x + dir[0], y + dir[1]

            #인접한 건물이 있다면
            if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
                home[nx][ny] = 0
                stack.append((nx,ny))
                cnt += 1    #수 + 1
    return cnt  #최종적으로 단지 수 반환

def bfs(x,y):
    q = deque()
    q.append((x,y))
    home[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for dir in ((0,1), (1, 0), (0, -1), (-1,0)):
            nx, ny = x + dir[0], y + dir[1]

            if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
                home[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0
hc = []
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            #같은 단지수를 카운팅해야함.
            # hc.append(dfs(i,j))
            hc.append(bfs(i,j))

hc.sort()
print(len(hc))
print(*hc,sep = "\n")