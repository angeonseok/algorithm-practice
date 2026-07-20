T = int(input())
for tc in range(1, T+1):
    n = int(input().strip())
    ans = "Odd" if n % 2 == 1 else "Even"
    print(f'#{tc} {ans}')