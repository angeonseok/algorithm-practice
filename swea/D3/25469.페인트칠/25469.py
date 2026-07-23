T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())

    arr = [input().strip() for _ in range(h) ]

    row = 0
    for i in range(h):
        cnt = 0
        for j in range(w):
            if arr[i][j] == '#':
                cnt += 1
            
        if cnt == w:
            row += 1
    
    col = 0
    for i in range(w):
        cnt = 0
        for j in range(h):
            if arr[j][i] == '#':
                cnt += 1
            
        if cnt == h:
            col += 1
    
    ans = 0
    if row == h and col == w:
        ans = min(row, col)
    else:
        ans = row + col
    print(ans)