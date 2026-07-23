T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]

    pos = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "#":
                pos.append((i, j))
    
    mx_row = max(r for r, c in pos)
    mn_row = min(r for r, c in pos)
    mx_col = max(c for r, c in pos)
    mn_col = min(c for r, c in pos)

    row = mx_row - mn_row + 1
    col = mx_col - mn_col + 1

    if row == col and row * col == len(pos):
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')