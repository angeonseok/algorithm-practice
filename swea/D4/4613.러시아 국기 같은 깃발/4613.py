T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input().strip() for  _  in range(n)]

    ans = 2501

    #3등분해서 셀거다.
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            #위치 십
            cnt = 0

            #상단은 흰색이여야함
            for a in range(i+1):
                cnt += m - arr[a].count('W')

            #중단은 파랑
            for b in range(i+1, j+1):
                cnt += m - arr[b].count('B')

            #하단은
            for c in range(j+1, n):
                cnt += m - arr[c].count('R')

            if cnt < ans:
                ans = cnt

    print(f'#{tc} {ans}')