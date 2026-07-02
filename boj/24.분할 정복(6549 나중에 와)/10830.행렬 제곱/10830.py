import sys
input = sys.stdin.readline

def mat_mul(a, b):
    mat = [[0] * n for _ in range(n)]

    #행렬 계산 후 나머지를 += 로 갈겼다가 이상하게 나옴
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j] = (mat[i][j] + a[i][k] * b[k][j]) % 1000

    return mat

#즐거운 분할정복
def div_mat_cal(arr, b):

    #길이가 1이 된 경우 일단 모든 항목을 1000으로 나눈 나머지로
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    #거듭제곱횟수가 짝수면 반갈
    if b % 2 == 0:
        m_half = div_mat_cal(arr, b//2)
        return mat_mul(m_half, m_half)

    #홀수면 반갈반갈 계산 후 하나 따로 더 계산
    else:
        m_half = div_mat_cal(arr, b//2)
        return mat_mul(mat_mul(m_half, m_half), arr)
    

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = div_mat_cal(arr, b)
for i in ans:
    print(*i)