import sys
input = sys.stdin.readline

n = int(input())

line = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append((a, b)) 

#line[0] 기준으로 오름차순으로 정렬
line.sort()

#최소는 1임
dp = [1] * n
for i in range(n):
    for j in range(i):
        
        #line[1] 기준으로 가장 긴 증가 부분 계산(전깃줄이 교차하지 않는 가장 긴 개수)
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

#전체에서 가장 큰 부분 뺴면 잘라야하는 전선 수
print(n - max(dp))