import sys
input = sys.stdin.readline

T = int(input())

#하, 우, 상, 좌 순으로 델타 정렬
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

for a in range(1,T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    d = 0
    cnt = 1

    #배열 만들었으면 안에서 작업해야지
    for _ in range(n * n):
        
        #탐색한 칸을 칠해
        arr[x][y] = cnt

        #다음 좌표
        nx = x + dx[d]
        ny = y + dy[d]

        #다음 좌표가 불가능한가? 왔던 길 또 가는 건가?
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x = nx
            y = ny
        
        #그렇다면 d값 변환시켜서 다시 도전
        else:
            d = (d + 1) % 4
            x = x + dx[d]
            y = y + dy[d]

        #이동하면 카운트 늘려
        cnt += 1
    
    print(f'#{a}')
    for i in arr:
        print(*i)