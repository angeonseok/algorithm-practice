import sys
input = sys.stdin.readline

#행과 열, 3x3 정사각형에서 같은 수가 있는지 체크
#같은 수가 있다면 그 수는 사용 불가능
def check_sudouk(x, y, a):
    for i in range(9):
        if arr[x][i] == a:
            return False
        
        if arr[i][y] == a:
            return False
    
    nx = 3 * (x // 3)
    ny = 3 * (y // 3)
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if arr[i][j] == a:
                return False
    
    return True


def sudoku(depth):
    
    #모든 빈칸을 채웠다면
    if depth == len(blank):
        for row in arr:     #결과물 1개만 출력하고 종료
            print(*row)
        exit()

    #1~9까지 전부 탐색할 예정
    for i in range(1, 10):

        #빈칸 좌표 받고
        x = blank[depth][0]
        y = blank[depth][1]

        #그 좌표에 넣을 수 있다면
        if check_sudouk(x, y, i):
            arr[x][y] = i   #넣고 
            sudoku(depth+1) #다음꺼 하러가자
            arr[x][y] = 0   #그리고 복구

arr = [list(map(int, input().split())) for _ in range(9)]

#빈칸 좌표 따러가자
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))

sudoku(0)