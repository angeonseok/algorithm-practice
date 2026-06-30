import sys
input = sys.stdin.readline

#처음엔 배열을 직접만들다가 시간 터짐
#주어진 좌표가 몇 사분면 안에 있는지 파악하면서 그 이외 영역 칸수 다 더함

def Z_arr(r, c, n):
    if n == 1:
        return 0
    
    half = n // 2
    area = half * half

    #1사분면
    if r < half and c < half:
        return Z_arr(r, c, half)
    
    #2사분면
    if r < half and c >= half:
        return area + Z_arr(r, c - half, half)
    
    #3사분면
    if r >= half and c < half:
        return 2 * area + Z_arr(r - half, c, half)
    
    #4사분면
    if r >= half and c >= half:
        return 3 * area + Z_arr(r - half, c - half, half)
    
n, r, c = map(int, input().split())
print(Z_arr(r, c, 2 ** n))