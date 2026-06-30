T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        for j in range(n):
            cnt = 0

            #k의 범위 : 1 ~ 2n - 1
            for k in range(1, 2 * n):
                
                #|dx| + |dy| = k - 1 >> 현재 서비스 범위의 테두리 좌표 조건
                for dx in range(-k + 1, k):
                    
                    #dx 값이 결정되면  dy도 결정
                    dy_val = k - 1 -abs(dx)

                    ## 마름모 한 겹씩 넓혀가며 집 수 누적
                    for dy in [dy_val, -dy_val]:
                        ni, nj = i + dx, j + dy

                        if 0 <= ni < n and 0 <= nj < n:
                            cnt += arr[ni][nj]
                        
                        #중심점 중복 방지
                        if dy_val == 0:
                            break
                
                #범위 운영 비용과 서비스 비용 계산
                cost = k * k + (k - 1) * (k - 1)
                total = cnt * m - cost

                #서비스 비용이 0원 이상인 경우에 정답 갱신
                if total >= 0:
                    ans = max(ans, cnt)
    
    print(f"#{tc} {ans}")