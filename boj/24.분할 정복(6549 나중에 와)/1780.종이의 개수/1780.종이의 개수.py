import sys
input = sys.stdin.readline

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
a, b, c, = 0, 0, 0

def cut_9(x,y,n):
    global a, b, c

    first = p[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != first:

                c_nine = n // 3

                #나눌때 가로 > 세로 순으로 잘 하자
                for dx in range(3):
                    for dy in range(3):
                        cut_9(x + dx*c_nine, y + dy*c_nine, c_nine)
                return
            
    if first == -1:
        a += 1
    elif first == 0:
        b += 1
    else:
        c += 1

cut_9(0,0,n)
print(a, b, c,sep='\n')