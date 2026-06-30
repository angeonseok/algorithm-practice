import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
gnd = [list(map(int,input().split())) for _ in range(n)]

#비로 침수당하는 최대 높이
max_gnd = max(max(row) for row in gnd)

#bfs 탐색용
dirs = ((0,1),(1,0),(0,-1),(-1,0))
q = deque()

#모든 지역이 침수당하기 전까지
ans = 0
for rain in range(max_gnd):
    cnt_safe = 0
    gnd_copy = [row[:] for row in gnd]   

    for i in range(n):
        for j in range(n):
            gnd_copy[i][j] -= rain    

    #1012와 아이디어 같음
    for i in range(n):
        for j in range(n):
            if gnd_copy[i][j] > 0:
                q.append((i,j))
                gnd_copy[i][j] = 0

                while q:
                    x, y = q.popleft()
                    for dir in dirs:
                        nx, ny = x + dir[0], y + dir[1]

                        if 0 <= nx < n and 0 <= ny < n and gnd_copy[nx][ny] > 0:
                                gnd_copy[nx][ny] = 0
                                q.append((nx,ny))
                cnt_safe += 1

    if ans < cnt_safe:
        ans = cnt_safe
print(ans)