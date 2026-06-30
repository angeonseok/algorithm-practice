import sys
input=sys.stdin.readline

t = int(input().rstrip())
num = [int(input()) for _ in range(t)]
max_num = max(num)                          #입력값 중 젤 큰놈을 찾아

   
p = [True] * (max_num+1)                    #그 놈 기준으로 소수를 찾아놔
p[0] = False
p[1] = False

for i in range(2, int(max_num ** 0.5)+1):
    if p[i]:
        for j in range(i * i, max_num + 1, i):
            p[j] = False

pm = [k for k in range(2, max_num + 1) if p[k]]

for i in num:               
    cnt = 0
    for j in pm:
        if j > i // 2:      # n = p - (n - p)로 본다면 절반 날려도 되지않나
            break
        if p[i - j] :       # n - p가 소수라면 카운팅
            cnt += 1
    print(cnt)
