import sys
input = sys.stdin.readline

n, m = map(int,input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

#인덱스 맞추기
prefix = [[0] * (n + 1) for _ in range(n + 1)]

#누적합 배열 생성. 2차원은 이거다.
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

#특정 구간의 합 계산하기
for n in range(m):
    line = (list(map(int,input().split())))
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    
    #ㅇㅇ
    ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] +prefix[x1-1][y1-1]
    
    print(ans) 