#현재 좌표, 칸수, 공사 여부
def create_line(now_i, now_j, cnt, cut):
    global ans
    ans = max(ans, cnt)

    #4방향 탐색
    for dir in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nxt_i, nxt_j = now_i + dir[0], now_j + dir[1]

        #맨날 보는 그 조건
        if 0 <= nxt_i < n and 0 <= nxt_j < n and not visited[nxt_i][nxt_j]:

            #1)공사를 안해도 되는 경우: 걍 진행
            if arr[now_i][now_j] > arr[nxt_i][nxt_j]:
                visited[nxt_i][nxt_j] = True
                create_line(nxt_i, nxt_j, cnt + 1, cut)
                visited[nxt_i][nxt_j] = False

            #2)공사 찬스 있을 때, 공사를 한다면 진행 가능한 경우
            elif arr[now_i][now_j] > arr[nxt_i][nxt_j] - k and not cut:

                #값을 변경했다가 되돌려줘야함.
                tmp = arr[nxt_i][nxt_j]

                # 더 깎을 필요 없이 1칸차이나게만
                arr[nxt_i][nxt_j] = arr[now_i][now_j] - 1

                #그리고 진행하고 돌려놓기
                visited[nxt_i][nxt_j] = True
                create_line(nxt_i, nxt_j, cnt + 1, True)
                visited[nxt_i][nxt_j] = False
                arr[nxt_i][nxt_j] = tmp

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #방문여부 따져야됨
    visited = [[False] * n for _ in range(n)]

    #가장 높은 봉우리 "값" 구하기
    max_h = max(max(row) for row in arr)

    ans = 0
    #가장 높은 봉우리 탐색해서
    for i in range(n):
        for j in range(n):

            #찾으면 등산로 조성 시작
            if arr[i][j] == max_h:
                visited[i][j] = True
                create_line(i, j, 1, False)
                visited[i][j] = False

    print(f'#{tc} {ans}')