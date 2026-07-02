import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(str, input().rstrip())) for _ in range(n)]

#이번엔 문자열이다.
def quad_tree(x, y, n):

    first = data[x][y]

    for i in range(x, x+n):
        for j in range(y,y+n):
            if data[i][j] != first:

                half = n // 2

                #출력형태때문에 깡통의 힘을 빌린 모습
                return ("(" 
                    + quad_tree(x, y, half)
                    + quad_tree(x, y + half, half)
                    + quad_tree(x + half, y, half)
                    + quad_tree(x + half, y + half, half)
                    + ")")
    
    return first
print(quad_tree(0,0,n))