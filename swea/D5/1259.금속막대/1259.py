T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tmp = list(map(int, input().split()))

    arr = [(tmp[2 * i], tmp[2 * i + 1]) for i in range(n)]
        