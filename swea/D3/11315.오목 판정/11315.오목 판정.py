T =int(input())
for tc in range(1, T+1):
    n = int(input())
    m = [input().strip() for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            #돌이 있는 부분부터 탐색
            if m[i][j] == 'o':
                for dir in [(-1,1), (0,1),(1,1),(1,0)]:
                    cnt = 0
                    ni, nj = i, j

                    #방향 유지하면서 5개 이상 체크될 때 까지 확인
                    while 0 <= ni < n and 0 <= nj < n and m[ni][nj] =='o':
                        cnt += 1
                        ni += dir[0]
                        nj += dir[1]

                    #체크 되면 다 빠져나가
                    if cnt >= 5:
                        ans = 1
                        break
                if ans:
                    break
        if ans:
            break       
   
    if ans:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')