def sol(p, target):
    l, r = 1, p
    cnt = 0
    while True:
        c = (l + r) // 2
        cnt += 1
        
        if c == target:
            return cnt
        
        if c < target:
            l = c 
        
        else:
            r = c 


T = int(input())
for tc in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    a = sol(p, pa)
    b = sol(p, pb)
    
    if a < b:
        ans = 'A'
    
    elif a > b:
        ans = 'B'
    
    else:
        ans = 0
    
    print(f'#{tc} {ans}')