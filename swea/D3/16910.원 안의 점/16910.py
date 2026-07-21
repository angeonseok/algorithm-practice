T = int(input())
for tc in range(1, T+1):
    n = int(input())

    ans = 0
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            if x ** 2 + y ** 2 <= n ** 2:
                ans += 1
    
    print(f'#{tc} {ans}')