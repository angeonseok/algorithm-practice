T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())

    arr = [input().strip() for _ in range(h) ]

    #가로부터 칠하자
    row = 0
    for i in range(h):
        cnt = 0
        for j in range(w):
            if arr[i][j] == '#':
                cnt += 1
            
        if cnt == w:
            row += 1

    #그다음은 세로를 칠하자
    col = 0
    for i in range(w):
        cnt = 0
        for j in range(h):
            if arr[j][i] == '#':
                cnt += 1
            
        if cnt == h:
            col += 1

    #다 칠할 수 있다면 더 작은 놈으로 칠하자
    ans = 0
    if row == h and col == w:
        ans = min(row, col)

    #아니면 둘 다 더해야 정답
    else:
        ans = row + col
    print(ans)