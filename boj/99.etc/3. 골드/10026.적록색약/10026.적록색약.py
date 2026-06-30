import sys
from collections import deque
input = sys.stdin.readline

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

#같은 영역 구분하기
def bfs(arr, i, j):
    q = deque()
    target = arr[i][j]
    q.append((i, j))
    arr[i][j] = 0

    while q:
        x, y = q.popleft()
        
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if arr[nx][ny] == target:
                arr[nx][ny] = 0
                q.append((nx,ny))

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
arr_RG = [row[:] for row in arr]     

#색약용 배열 세팅
for i in range(n):
    for j in range(n):
        if arr_RG[i][j] == "G":
            arr_RG[i][j] = "R"

#정상 배열 영역 카운팅
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            bfs(arr, i, j)
            cnt += 1

#색약 배열 영역 카운팅
cnt_RG = 0
for i in range(n):
    for j in range(n):
        if arr_RG[i][j] != 0:
            bfs(arr_RG, i, j)
            cnt_RG += 1

print(f"{cnt} {cnt_RG}")