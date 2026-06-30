import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    if n % h == 0:
        y = h
        x = n // h
    else:
        y = n % h
        x = n // h + 1

    print(f"{y}{x:02d}")