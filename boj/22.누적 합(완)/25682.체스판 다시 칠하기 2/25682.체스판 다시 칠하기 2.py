import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(n)]

#칠해야하는 칸 수를 누적합으로 저장할 예정
prefix_W = [[0] * (m+1) for _ in range(n+1)]
prefix_B = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_W[i][j] = prefix_W[i-1][j] + prefix_W[i][j-1] - prefix_W[i-1][j-1]
        prefix_B[i][j] = prefix_B[i-1][j] + prefix_B[i][j-1] - prefix_B[i-1][j-1]

        #(1,1)칸 기준 색이 다음 색을 결정함
        if (i + j) % 2 == 0:
            if arr[i-1][j-1] != "W":    #기준 : W
                prefix_W[i][j] += 1
            
            if arr[i-1][j-1] != "B":    #기준 : B
                prefix_B[i][j] += 1
        else:
            if arr[i-1][j-1] != "B":
                prefix_W[i][j] += 1
            
            if arr[i-1][j-1] != "W":
                prefix_B[i][j] += 1

#누적합 결과를 기반으로 k*k칸에 칠하는 횟수 계산. range범위 잘못잡았다 틀림ㅇㅇ
ans = n*m+1
for i in range(k, n+1):
    for j in range(k, m+1):
        w = prefix_W[i][j] - prefix_W[i-k][j] - prefix_W[i][j-k] + prefix_W[i-k][j-k]
        b = prefix_B[i][j] - prefix_B[i-k][j] - prefix_B[i][j-k] + prefix_B[i-k][j-k]
        ans = min(ans, w, b)

print(ans)