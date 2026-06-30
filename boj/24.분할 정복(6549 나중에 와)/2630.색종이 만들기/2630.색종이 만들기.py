import sys
input = sys.stdin.readline
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

w = 0
b = 0

#분할 정복
def cut(x,y,n):
    global w
    global b

    #기준값
    first = p[x][y]

    for i in range(x, x+n):
        for j in range(y,y+n):

            #전부 같지 않다면?
            if p[i][j] != first:
                
                #4등분 내고 끝
                half = n // 2
                cut(x, y, half)
                cut(x, y + half, half)
                cut(x + half, y, half)
                cut(x + half, y + half, half)
                return

    #전부 같으면 카운트        
    if first == 0:
        w += 1
    else:
        b += 1

cut(0,0,n)
print(w)
print(b)