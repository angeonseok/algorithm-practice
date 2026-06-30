import sys
input = sys.stdin.readline

n = int(input())

#공백만들기
arr = [[" "] * n for _ in range(n)]

#분할정복
def star(arr, r, c, n):

    #더 못쪼개면 별찍어
    if n == 1:
        arr[r][c] = "*"
        return
    
    #전체를 9등분하겠다
    n = n // 3
    for i in range(3):
        for j in range(3):

            #9등분 기준 중앙은 공백으로 둬야지
            if i == 1 and j == 1:
                continue
            else:
                star(arr, r + i*n, c+ j*n, n)

star(arr, 0, 0, n)
for row in arr:
    print("".join(row))