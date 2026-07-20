T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    ans = 1 if (a * b * c - 1) % 2 == 1 else 2
    print(ans)