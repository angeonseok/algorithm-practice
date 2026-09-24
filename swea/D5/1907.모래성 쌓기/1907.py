from collections import deque

dirs = ((0,1), (1,1), (1,0), (1, -1), (0,-1), (-1,-1), (-1,0), (-1,1))

#매번 배열 상태 체크하면 시간 터질거같음
T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]

    #그래서 바다 위치 기준으로 -1씩 깎아버릴거임
    q = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '.':
                q.append((i, j))

    ans = 0
    while q:
        break_sand = False

        #파도 구분
        for _ in range(len(q)):
            ci, cj = q.popleft()

            for dir in dirs:
                ni, nj = ci + dir[0], cj + dir[1]

                #바다 8방향에 있는 놈들 1씩 깐다
                if 0 <= ni < h and 0 <= nj < w and arr[ni][nj].isdigit():
                    arr[ni][nj] = str(int(arr[ni][nj]) - 1)

                    #0되는 놈은 이제 바다가 된다
                    if arr[ni][nj] == '0':
                        break_sand = True
                        q.append((ni, nj))

        #이번 파도에 부서진 놈 있으면 횟수 추가
        if break_sand:
            ans += 1

    print(f'#{tc} {ans}')