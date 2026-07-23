import math

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    num = math.ceil(n ** (1/3))

    if num ** 3 == n:
        print(f'#{tc} {num}')
    else:
        print(f'#{tc} -1')