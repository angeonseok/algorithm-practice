for tc in range(1,11):
    n = int(input())
    mat = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0

    for i in range(100):
        for j in range(100):
            
            #1찾으면 2랑 만날 때 까지 탐색. 그 사이에 있는 값은 0으로 
            if mat[j][i] == 1:
                for k in range(j+1, 100):
                    if mat[k][i] == 2:
                        cnt += 1
                        break
                    else:
                        mat[k][i] = 0
    
    print(f'#{tc} {cnt}')