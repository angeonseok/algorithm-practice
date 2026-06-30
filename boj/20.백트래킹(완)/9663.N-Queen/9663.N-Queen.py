import sys
input = sys.stdin.readline

#일단 놨을 때, 이전 배치들과 충돌나는지 체크
def check(col):
    for i in range(col):
        #대각선 위치면 컷(행 차이 == 열 차이)
        #같은 열이면 컷
        if abs(maps[i] - maps[col]) == abs(col - i) or maps[i] == maps[col]:
            return False

    return True

def N_queen(row):
    global cnt

    if row == n:    #가능한 경우에 카운팅
        cnt += 1
        return
    
    for i in range(n):      #모든 열에 대해서 조사
        maps[row] = i       #먼저 놓고
        if check(row):      #가능한 위치면
            N_queen(row+1)  #다음 행으로 진행

n = int(input())
maps = [0] * n      #인덱스 = 행, 데이터 값 = 열
cnt = 0

N_queen(0)
print(cnt)