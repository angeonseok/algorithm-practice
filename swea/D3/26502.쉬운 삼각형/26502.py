T = int(input())
for tc in range(1, T+1):
    n = int(input())
    point = [tuple(map(int, input().split())) for _ in range(n)]

    for i in range(n):
