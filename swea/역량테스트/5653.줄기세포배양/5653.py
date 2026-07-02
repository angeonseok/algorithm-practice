dirs = ((0,1),(1,0),(0,-1),(-1,0))

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())

    #배치된 좌표는 set으로 관리
    occupied = set()

    ## 좌표 : (생명력, 생성 시간) 형태로 관리
    cell = {}
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(m):
            if arr[j] > 0:
                cell[(i, j)] = [arr[j], 0]
                occupied.add((i, j))

    #k 시간동안 냅둘 예정
    for time in range(1, k+1):
    
        # 이번 시간에 새로 생길 세포 후보 저장
        trans_cell = {}

        for (x, y), (life, born) in cell.items():
            
            #현재 시간 기준 이미 죽은 놈은 빼
            if life * 2 + born < time:
                continue
            
            #현재 시간 기준 전파 가능한 애들은 전파
            #깨어난 시간 + 1시간 뒤에 전파 가능함
            if life + born  + 1 == time:
                for dir in dirs:
                    nx, ny = x + dir[0], y + dir[1]

                    if (nx, ny) in occupied:
                        continue
                    
                    #전파되거나, 같은 시간에 더 큰 놈이 들어오면 갱신
                    if (nx, ny) not in trans_cell or trans_cell[(nx,ny)] < life:
                        trans_cell[(nx,ny)] = life

        #세포 갱신
        for (nx,ny), life in trans_cell.items():
            cell[(nx, ny)] = [life, time]
            occupied.add((nx, ny))

    #죽은 놈 뺴고 카운팅
    ans = 0
    for life, born in cell.values():
        if life * 2 + born > k:
            ans += 1
    
    print(f"#{tc} {ans}")