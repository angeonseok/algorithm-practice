import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#합의 최댓값을 계산한 배열 생성할 예정
tri = [[0] * (i + 1) for i in range(n)]
tri[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:  #왼쪽 끝
            tri[i][j] = tri[i-1][j] + arr[i][j]
        
        elif j == i:  #오른쪽 끝
            tri[i][j] =  tri[i-1][j-1] + arr[i][j]
        
        else:   #그 외
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + arr[i][j]

#인덱스 조심
print(max(tri[n-1]))