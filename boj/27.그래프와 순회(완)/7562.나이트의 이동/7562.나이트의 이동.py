import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l = int(input())
    a, b = map(int,input().split())
    c, d = map(int, input().split())

    mat = [[0] * l for _ in range(l)]

    q = deque()
    mat[a][b] = 0       #이동 횟수
    q.append((a,b))     #시작지점 제공함

    while q:
        x, y = q.popleft()
        
        #종료조건
        if x == c and y ==d:
            print(mat[c][d])
            break
        
        #나이트는 8방향 이동
        for dir in [(-2,1), (-1,2), (1, 2), (2,1), (2,-1), (1,-2), (-1,-2),(-2,-1)]:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 <= nx < l and 0 <= ny < l and mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx,ny))