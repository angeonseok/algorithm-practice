T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    ans = a * b if (1 <= a <= 9) and (1 <= b <= 9) else -1 
    print(f'#{tc} {ans}')