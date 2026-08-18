T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = 0
    for i in arr:
        if i < 40:
            ans += 40
        else:
            ans += i

    print(f'#{tc} {int(ans / 5)}')