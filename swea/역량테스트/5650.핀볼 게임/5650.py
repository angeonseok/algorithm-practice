from collections import defaultdict

#방향
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))


#벽에 반사될 때 방향
reflect = {
    1 : {0 : 2, 1 : 0, 2 : 3, 3 : 1}, 
    2 : {0 : 2, 1 : 3, 2 : 1, 3 : 0}, 
    3 : {0 : 1, 1 : 3, 2 : 0, 3 : 2}, 
    4 : {0 : 3, 1 : 2, 2 : 0, 3 : 1}, 
    5 : {0 : 2, 1 : 3, 2 : 0, 3 : 1}, 
}


def game(si, sj, d):
    i, j = si, sj
    score = 0

    while True:
        ni, nj = i + dir[d][0], j + dir[d][1]

        nxt = field[ni][nj]

        #1. 종료조건(블랙홀 or 시작지점)
        if nxt == -1 or (ni == si and nj == sj):
            return score

        #2. 벽에 충돌했을 때
        elif 1 <= nxt <= 5:
            d = reflect[nxt][d]
            score += 1

        #. 화이트홀 들어갈 때
        elif 6 <= nxt <= 10:
            a, b = whitehole[nxt]
            if (ni, nj) == a:
                ni, nj = b
            else:
                ni, nj = a

        #위치 최신화
        i, j = ni, nj
        

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #가장자리는 전부 5번 블록과 같은 판정으로 맵 재생성
    field = [[5] * (n + 2)]
    for i in range(n):
        field.append([5] + arr[i] + [5])
    field.append([5] * (n + 2))

    #화이트홀은 좌표 모아둔다
    whitehole = defaultdict(list)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if 6 <= field[i][j] <= 10:
                whitehole[field[i][j]].append((i, j))

    #핀볼 놓을 수 있는 지점에서 4방향 테스트
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if field[i][j] != 0:
                continue

            for d in range(4):
                ans = max(ans, game(i, j, d))

    print(f'#{tc} {ans}')