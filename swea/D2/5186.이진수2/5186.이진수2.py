T = int(input())
for tc in range(1, T+1):
    n = float(input().strip())
    ans = ""

    while n > 0:
        if len(ans) >= 12:
            ans = "overflow"
            break

        n *= 2

        if n >= 1:
            ans += "1"
            n -= 1
        
        else:
            ans += "0"
    
    print(f"#{tc} {ans}")