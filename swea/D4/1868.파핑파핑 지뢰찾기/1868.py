from collections import deque

#8방향
dirs = ((0,1), (1,1), (1,0), (1, -1), (0,-1), (-1,-1), (-1,0), (-1,1))

#8방향에 지뢰 없는 놈 찾기. 굳?이 함수를 만들어야하는가 의문
def search_point(i, j):
    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] == '*':
                return False

    return True


#8방향 지뢰 수 세기
def count_mine(i, j):
    cnt = 0
    for dir in dirs:
            ni, nj = i + dir[0], j + dir[1]
    
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == '*':
                    cnt += 1
    
    return cnt


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]

    ans = 0
    q = deque()
    for i in range(n):
        for j in range(n):

            #주변 깨끗한 놈 먼저 눌러서 연쇄폭발
            if arr[i][j] == '.' and search_point(i, j):
                arr[i][j] = '0'
                ans += 1
                q.append((i, j))

                while q:
                    ci, cj = q.popleft()

                    for dir in dirs:
                            ni, nj = ci + dir[0], cj + dir[1]

                            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == '.':
                                if search_point(ni, nj):
                                    arr[ni][nj] = '0'
                                    q.append((ni, nj))

                                else:
                                    arr[ni][nj] = str(count_mine(ni, nj))

    #터트릴거 터트리고 안 터진 놈들 수 세기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                ans += 1
                
    print(f'#{tc} {ans}')