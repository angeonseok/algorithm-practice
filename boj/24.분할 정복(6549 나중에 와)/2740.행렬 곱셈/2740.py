import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

x, y = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(x)]

#행과 열을 반대로 잡았다가 틀린 모습
ans = [[0] * y for _ in range(n)]
for i in range(n):
    for j in range(y):
        for t in range(m):
            ans[i][j] += A[i][t] * B[t][j]

for i in ans:
    print(*i)