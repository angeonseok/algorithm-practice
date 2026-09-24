dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [list(input().strip()) for _ in range(r)]

    #좌표, 방향, 메모리 정보 담아야됨.
    visited = [[[[False] * 16 for _ in range(4)] for _ in range(c)] for _ in range(r)]

    #애초에 도착지점 없는 경우 걸러내기
    if not any('@' in row for row in arr):
        print(f'#{tc} NO')
        continue

    #dfs 가자
    stack = [(0, 0, 0, 0)]
    visited[0][0][0][0] = True
    flag = False

    while stack:
        x, y, d, m = stack.pop()

        #정답 좌표로 어떻게든 오면 끝내기
        if arr[x][y] == '@':
            flag = True
            break

        #문제 조건에 맞게 d, m 값 변경
        if arr[x][y] == '<':
            d = 2
        
        elif arr[x][y] == '>':
            d = 0
        
        elif arr[x][y] == '^':
            d = 3
        
        elif arr[x][y] == 'v':
            d = 1
        
        elif arr[x][y] == '_':
            d = 0 if m == 0 else 2
        
        elif arr[x][y] == '|':
            d = 1 if m == 0 else 3        
        
        elif arr[x][y].isdigit():
            m = int(arr[x][y])
        
        elif arr[x][y] == '+':
            m = (m + 1) % 16
        
        elif arr[x][y] == '-':
            m = (m - 1) % 16


        #'?' 같은 경우는 4방향 돌려야해서 맨 마지막에 따로 처리
        nds = range(4) if arr[x][y] == '?' else [d]
        for nd in nds:
            nx = (x + dirs[nd][0]) % r
            ny = (y + dirs[nd][1]) % c

            #미방문시 방문 처리 후 넣기
            if not visited[nx][ny][nd][m]:
                visited[nx][ny][nd][m] = True
                stack.append((nx, ny, nd, m))

    print(f'#{tc} {"YES" if flag else "NO"}')