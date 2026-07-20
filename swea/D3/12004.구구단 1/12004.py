T = int(input())
for tc in range(1, T+1):
    n = int(input())

    for i in range(9, 0, -1):
        if n % i == 0:
            a = n // i

            if 1 <= a <= 9:
                print(f'#{tc} Yes')
                break
    else:
        print(f'#{tc} No')