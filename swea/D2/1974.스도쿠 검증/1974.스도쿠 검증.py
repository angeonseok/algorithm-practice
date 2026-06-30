#합이 45임을 이용해서 판별
def check(x, y):
    sum_row = 0
    for i in range(9):
        sum_row += sudoku[x][i]
    
    if sum_row != 45:
        return False
    
    sum_col = 0
    for i in range(9):
        sum_col += sudoku[i][y]
    
    if sum_col != 45:
        return False
        
    sum_mat = 0
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(nx, nx+3):
        for j in range(ny, ny+3):
            sum_mat += sudoku[i][j]

    if sum_mat != 45:
        return False

    return True        
T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    flag = True
    for i in range(9):
        for j in range(9):
            if not check(i, j):
                flag = False
                break
            
        if not flag:
            break
    
    if not flag:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")