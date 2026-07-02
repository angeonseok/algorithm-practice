from collections import deque

dirs = ((-1,0), (0,1), (1,0), (0,-1))

pipeline = {
    1 : (0, 1, 2, 3),
    2 : (0, 2),
    3 : (1, 3),
    4 : (0, 1),
    5 : (1, 2),
    6 : (2, 3),
    7 : (0, 3)
}

#상호 연결 확인
def link(i, j, ni, nj):
    for d in pipeline[arr[ni][nj]]:
        a, b = ni + dirs[d][0], nj + dirs[d][1]
        
        if a == i and b == j:
            return True
    
    return False

#즐거운 bfs
def bfs(x, y):
    q = deque()
    cnt = 0

    q.append((x, y))
    visited[x][y] = 1
    cnt += 1

    while q:
        x, y = q.popleft()

        #l초 이후는 구할 필요가 없다
        if visited[x][y] == l:
            continue

        for d in pipeline[arr[x][y]]:
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            #서로 연결된 경우 이동 후 카운팅
            if arr[nx][ny] != 0 and visited[nx][ny] == 0:
                if link(x, y, nx, ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = bfs(r, c)
    print(f"#{tc} {ans}")