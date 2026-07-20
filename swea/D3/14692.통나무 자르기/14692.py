T = int(input())
for tc in range(1, T+1):
    n = int(input())

    ans = "Alice" if n % 2 == 0 else "Bob"
    print(f'#{tc} {ans}')