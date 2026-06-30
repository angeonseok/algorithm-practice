import sys
input = sys.stdin.readline

#3차원은 뭐야
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

#있는대로 적으니 틀린 모습
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a> 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    #이미 계산했으면 바로 반환
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
   
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1,b-1,c) + w(a-1, b, c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')