T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    ans = a if a == b else 1
    print(f'#{tc} {ans}')