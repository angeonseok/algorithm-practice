T = int(input())
for tc in range(1, T+1):
    n = int(input().strip())
    
    ans = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            ans -= i
    
        else:
            ans += i

    print(f"#{tc} {ans}")