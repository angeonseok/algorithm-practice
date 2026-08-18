T = int(input())
for tc in range(1, T+1):
    a, b = input().split()

    # s + t == t + s면 가능
    print(f'#{tc} {"yes" if a + b == b + a else "no"}')