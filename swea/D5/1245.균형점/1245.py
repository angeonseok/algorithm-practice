T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tmp = list(map(int, input().split()))

    point = [(tmp[i], tmp[i + 1]) for i in range(0, len(tmp), 2)]
    print(point)