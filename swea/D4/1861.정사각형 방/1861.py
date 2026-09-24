def sol(i, j):
    global cnt

    for dir in ((0,1), (1,0), (0,-1), (-1,0)):
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] == arr[i][j] + 1:
                cnt += 1
                sol(ni, nj)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    ans_num = 1
    for i in range(n):
        for j in range(n):
            start_num = arr[i][j]
            cnt = 1
            sol(i, j)

            if ans < cnt:
                ans = cnt
                ans_num = start_num

            elif ans == cnt and start_num < ans_num:
                ans_num = start_num

    print(f'#{tc} {ans_num} {ans}')