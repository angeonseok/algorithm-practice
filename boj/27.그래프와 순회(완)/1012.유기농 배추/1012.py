def bfs(y, x):
    q = deque()
    q.append((y,x))
    mat[y][x] = 0

    while q:
        y, x = q.popleft()
        for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            ny, nx = y + dir[0], x + dir[1]

            #주변에 1인 곳들만 탐색
            if 0 <= ny < n and 0 <= nx < m and mat[ny][nx] == 1:
                mat[ny][nx] = 0
                q.append((ny,nx))

#사실상 덱 vs 스택 차이
def dfs(y, x):
    stack = []
    stack.append((y,x))
    mat[y][x] = 0

    while stack:
        y, x = stack.pop()
        for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            ny, nx = y + dir[0], x + dir[1]

            if 0 <= ny < n and 0 <= nx < m and mat[ny][nx] == 1:
                mat[ny][nx] = 0
                stack.append((ny,nx))

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    mat = [[0] * m for _ in range(n)]   #입력 순서를 잘 봐야함

    for i in range(k):
        a, b = map(int,input().split()) #좌표를 입력으로 받음
        mat[b][a] = 1

    #값이 1인 곳으로 들가서 인접한 1인 애들 다 부수고 카운팅
    cnt = 0
    for y in range(n):
        for x in range(m):
            if mat[y][x] == 1:  
                # dfs(y, x)
                bfs(y, x)
                cnt +=1
    
    print(cnt)