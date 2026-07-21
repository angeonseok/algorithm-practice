import math

T = int(input())
for tc in range(1, T+1):
    n, d = map(int, input().split())

    r = 2 * d + 1
    ans = math.ceil(n/r) 
    print(f'#{tc} {ans}')