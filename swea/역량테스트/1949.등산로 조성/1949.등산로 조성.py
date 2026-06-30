dirs = ((0, 1), (1, 0), (0, -1), (-1,0))

#2. 탐색하자
def dfs(i, j, length, cut):
    global ans
    ans = max(ans, length)

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:

            #3. 안깎고 가는 경우 > 그냥 진행
            if arr[ni][nj] < arr[i][j] and not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj, length + 1, cut)
                visited[ni][nj] = False

            #4. 깎을 수 있고, 깎고 가는 경우 > 깎아서 진행 후 복원(tmp로 원래 값 저장 미리해두기)
            elif not cut and arr[ni][nj] - k < arr[i][j] and not visited[ni][nj]:
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1

                visited[ni][nj] = True
                dfs(ni, nj, length + 1, True)
                visited[ni][nj] = False
                arr[ni][nj] = tmp
    

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    ans = 0

    #1. 최대 높이 봉우리 찾기
    max_h = max(max(row) for row in arr)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_h:
                visited[i][j] = True
                dfs(i, j, 1, False)
                visited[i][j] = False

    print(f"#{tc} {ans}")