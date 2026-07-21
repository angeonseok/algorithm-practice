T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    ans = "ON"
    t = "1" * n
    bits = int(t, 2)

    if (m & bits) != bits:
        ans = "OFF"
    
    print(f'#{tc} {ans}')