import sys

ans = []

while 1 : 
    n = int(sys.stdin.readline())

    if n == 0 :
        break

    p = [True] * (2*n + 1)              #체가 편하긴 하네
    p[0] = False
    p[1] = False
    
    for i in range(2, n+1):
        if p[i]:
            for j in range(i*i, 2* n + 1, i):
                p[j] = False
    pm = [i for i in range(2, 2 * n + 1) if p[i]]

    cnt = 0                             #갯수를 물으니 카운트세자
    for k in pm :
        if k > n and k <= (2 * n) :
            cnt += 1
    ans.append(cnt)                     #모아서 출력해야하니 모으자

for a in ans:
    print(a)