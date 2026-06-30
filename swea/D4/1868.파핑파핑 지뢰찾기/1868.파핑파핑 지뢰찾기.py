from collections import deque

dirs = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))

def count_boom(i, j):
    cnt_boom = 0

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] == '*':
                cnt_boom += 1

    return cnt_boom


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] != "*" and not visited[i][j]:
                cnt_boom = count_boom(i, j)

                if cnt_boom == 0:
                    q.append((i, j))
                    visited[i][j] = True
                    cnt += 1

                    while q:
                        ci, cj = q.popleft()
                        
                        if count_boom(ci, cj) != 0:
                            continue
                        
                        for dir in dirs:
                            ni, nj = ci + dir[0], cj + dir[1]
                            
                            if 0 <= ni < n and 0 <= nj < n:
                                if arr[ni][nj] != '*' and not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    q.append((ni, nj))
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != "*" and not visited[i][j]:
                cnt += 1

    print(f"#{tc} {cnt}")