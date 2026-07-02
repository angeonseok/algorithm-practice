import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

#재귀 dfs + dp 느낌
#이미 계산한 경로를 다시 계산하지 않고 사용
def route(i, j):
    #도착하면 경로 하나
    if i == m - 1 and j == n-1:
        return 1
    
    #이미 계산한 곳이면 그 값 바로 사용
    if visited[i][j] != -1:
        return visited[i][j]
    
    visited[i][j] = 0

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        
        if not (0 <= ni < m and 0 <= nj < n):
            continue
        
        if arr[ni][nj] < arr[i][j]:
            visited[i][j] += route(ni, nj)

    #여기서 도착지까지 가는 경우의 수
    return visited[i][j]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

visited = [[-1] * n for _ in range(m)]

print(route(0, 0))