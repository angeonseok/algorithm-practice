T = int(input())
for tc in range(1, T+1):
    n = int(input())
    point = [tuple(map(int, input().split())) for _ in range(n)]

    #걍 삼각형 만들지 뭐.
    ans = 0
    for i in range(n):

        #이 점을 직각으로 할 예정.
        a, b = point[i]
        x, y = 0, 0

        for j in range(n):
            if i == j:
                continue

            c, d = point[j]

            if a == c:
                tmp_y = abs(d - b)
                y = max(y, tmp_y)

            elif b == d:
                tmp_x = abs(c - a)
                x = max(x, tmp_x)

        ans = max(ans, x * y)
        
    print(ans)