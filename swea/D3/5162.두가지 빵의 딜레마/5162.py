T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    print(f'#{tc} {c // min(a, b)}')