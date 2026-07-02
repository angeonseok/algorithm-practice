import sys
input = sys.stdin.readline

mod = 1000000007

#검색좀 했음

# 피보나치 전이행렬:
# [F(n)  ]   [1 1] [F(n-1)]
# [F(n-1)] = [1 0] [F(n-2)]
# 따라서 [[1,1],[1,0]]^(n-1)의 [0][0]은 F(n)이다.
def mat_mul(a, b):
    mat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat[i][j] = (mat[i][j] + a[i][k] * b[k][j]) % mod
    return mat

# 분할정복으로 행렬 거듭제곱 계산
# num == 0이면 A^0 = I 이므로 단위행렬 반환
def pibb(arr, num):
    if num == 0:
        return [[1, 0], [0, 1]]
    if num == 1:
        for i in range(2):
            for j in range(2):
                arr[i][j] %= mod
        return arr
    
    if num % 2 == 0:
        half = pibb(arr, num // 2)
        return mat_mul(half, half)
    else:
        half = pibb(arr, num // 2)
        return mat_mul(mat_mul(half, half), arr)
    
n = int(input())
arr = [[1, 1], [1, 0]]
ans = pibb(arr, n-1)
print(ans[0][0])