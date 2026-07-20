T = int(input())
for tc in range(1, T+1):
    a = input().strip()
    cnt = a.count('x')
    
    ans = "YES" if cnt < 8 else "NO"
    print(f'#{tc} {ans}')