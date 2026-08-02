#포탄 떄려박기용
dirs = {'^': (-1, 0), 
       'v': (1, 0), 
       '<': (0, -1), 
       '>': (0, 1)
       }


#커맨드 처리용
move = {'U': (-1, 0, '^'),
        'D': (1, 0, 'v'), 
        'L': (0, -1, '<'), 
        'R': (0, 1, '>')
        }


T = int(input())

for tc in range(1, T+1):
    h, w = map(int, input().split())
    field = [list(input().strip()) for _ in range(h)]
    n = int(input())
    cmd = input().strip()

    #우선 시작 좌표를 찾자
    for i in range(h):
        for j in range(w):
            if field[i][j] in ('^', 'v', '<', '>'):
                si, sj, d = i, j, field[i][j]

    #커맨드대로 처리하자
    for c in cmd:

        #발사를 먼저 처리하게 하는게 나아보이던데
        if c == 'S':
            ni, nj = si + dirs[d][0], sj + dirs[d][1]

            while(0 <= ni < h and 0 <= nj < w):
                if field[ni][nj] == '*':
                    field[ni][nj] = '.'
                    break

                elif field[ni][nj] == '#':
                    break

                ni += dirs[d][0]
                nj += dirs[d][1]

        #여긴 전부 이동
        else:
            if c in move:
                d = move[c][2]
                field[si][sj] = d
                ni, nj = si + move[c][0], sj + move[c][1]

                if 0 <= ni < h and 0 <= nj < w and field[ni][nj] == '.':
                    field[ni][nj] = move[c][2]
                    field[si][sj] = '.'
                    si, sj = ni, nj

    #출력 양식 맞추기
    print(f'#{tc}', end = " ")
    for i in field:
        print("".join(i))