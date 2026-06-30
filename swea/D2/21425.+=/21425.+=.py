T = int(input())
for tc in range(1, T + 1):
    a, b, n = map(int, input().split())

    #둘 중 하나가 초과될 때 까지
    cnt = 0
    while a <= n and b <= n:

        #둘 중 큰 놈을 작은 놈에 계속 더해
        if a > b:
            b += a
        else:
            a += b
        cnt += 1

    print(cnt)