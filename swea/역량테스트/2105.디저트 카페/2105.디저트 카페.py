dirs = ((1, 1), (1, -1), (-1, -1), (-1, 1))

def dfs(si, sj, ci, cj, cnt, d):
    global ans

    #2. 방향을 제한하면서 탐색(현재방향/다음방향)
    for nd in (d, d+1):

        #최대 횟수는 3회
        if nd > 3:
            continue

        ni, nj = ci + dirs[nd][0], cj + dirs[nd][1]

        #3. 시작 지점으로 돌아옴 + 최소 개수 채우면 > 정답 갱신
        if 0 <= ni < n and 0 <= nj < n:
            if ni == si and nj == sj and cnt >= 4:
                ans = max(ans, cnt)
                return
            
            #4. # 디저트 안 겹치면 계속 가
            elif not visited[arr[ni][nj]]:
                visited[arr[ni][nj]] = True
                dfs(si, sj, ni, nj, cnt+1, nd)
                visited[arr[ni][nj]] = False

        
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * 101
    ans = -1

    #1. 사각형 생성 가능 지점만 조사하자
    for i in range(n-2):
        for j in range(1, n-1):
            visited[arr[i][j]] = True
            dfs(i, j, i, j, 1, 0)
            visited[arr[i][j]] = False

    print(f"#{tc} {ans}")