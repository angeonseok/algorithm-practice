def check(row, col):
    for i in range(row):

        #1. 같은 열에 속하거나
        #2. 행의 차이 = 열의 차이(대각선 위치)인 경우 컽
        if queen[i] == col or (abs(row - i) == abs(col - queen[i])):
            return False
    return True


def N_queen(row):
    global cnt

    #모든 행에 다 놨으면 경우의 수 + 1
    if row == n:
        cnt += 1
        return 

    #일단 모든 곳에 놔본다
    for i in range(n):
        queen[row] = i

        #거기 둘 수 있다면
        if check(row, i):

            #난 다음 행으로 갈거야.
            N_queen(row + 1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    #인덱스 = 행, 값 = 열
    queen = [0] * n
    cnt = 0
    N_queen(0)

    print(f'#{tc} {cnt}')