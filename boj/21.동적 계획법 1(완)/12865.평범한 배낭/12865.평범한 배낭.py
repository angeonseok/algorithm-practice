import sys
input = sys.stdin.readline

n, k = map(int,input().split())

#이차원 배열로 자료 받기
item_list = [map(int, input().split()) for _ in range(n)]

#우리는 k값에 따라 결과가 달라진다
dp = [0] * (k + 1)

#딱 맞게 넣거나, 이전 결과 + 무게 한도 안걸리는 놈 추가
for w, v in item_list:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])