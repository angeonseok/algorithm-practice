from collections import deque

for tc in range(1, 11):
    input()
    arr = [list(map(int, input().strip())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    #도착점 찾기
    ei, ej = 0, 0
    flag = False
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 3:
                ei, ej = i, j
                flag = True
                break
        if flag:
            break

    q = deque([(1, 1)])
    visited[1][1] = True

    while q:
        x, y = q.popleft()

        #도착했으면 더 돌릴 이유가 없다
        if x == ei and y == ej:
            break

        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    ans = 1 if visited[ei][ej] else 0
    print(f'#{tc} {ans}')