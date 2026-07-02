import sys
input = sys.stdin.readline

n ,k = map(int,input().split())
#동전 단위 내림차순 정렬
p = sorted([int(input()) for _ in range(n)],reverse=True)

#단위 큰거부터 계산해서 k값을 조져
cnt = 0
for i in p:

    #카운팅 먼저 하고 k값 줄여야지
    cnt += k // i
    k = k % i
    
    if k == 0:
        break

print(cnt)