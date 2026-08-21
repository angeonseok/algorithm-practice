T = int(int(input()))
for tc in range(1, T+1):
    a = input()
    b = input()

    ans = 1 if b.find(a) > 0 else 0
    print(f'#{tc} {ans}')