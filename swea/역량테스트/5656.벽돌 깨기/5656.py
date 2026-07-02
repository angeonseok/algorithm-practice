from collections import deque
 
dirs = ((0,1), (1,0), (0,-1), (-1,0))
 
#1. 터트린다
def boom(a, arr):
    q = deque()
 
    for i in range(H):
        if arr[i][a] != 0:
            q.append((i, a, arr[i][a]))
            arr[i][a] = 0
            break
 
    while q:
        x, y, r = q.popleft()
 
        for k in range(1, r):
            for dir in dirs:
                nx, ny = x + dir[0] * k, y + dir[1] * k
 
                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if arr[nx][ny] != 0:
                    q.append((nx, ny, arr[nx][ny]))
                    arr[nx][ny] = 0
    return arr
 
#2. 내려간다
def fall(arr):
    for i in range(W):
        temp = []
        for j in range(H):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
                arr[j][i] = 0
 
        nj = H-1
        for v in reversed(temp):
            arr[nj][i] = v
            nj -= 1
 
    return arr
 
#3. 센다
def count(arr):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                cnt += 1
    return cnt
 
#4. 종합선물세트
def sol(depth, arr):
    global ans
    cnt = count(arr)
    ans = min(ans, cnt)
 
    if depth == N or cnt == 0:
        return
 
    for i in range(W):
        clone = [row[:] for row in arr]
        boom(i, clone)
        fall(clone)
        sol(depth+1, clone)
 
T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
 
    ans = 987654321
    sol(0,arr)
 
    print(f"#{tc} {ans}")