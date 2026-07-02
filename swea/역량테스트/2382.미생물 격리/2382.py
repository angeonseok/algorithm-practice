dirs = {
    1 : (-1, 0),
    2 : (1, 0),
    3 : (0, -1),
    4 : (0, 1),
}

r_dirs = {
    1 : 2,
    2 : 1,
    3 : 4,
    4 : 3,
}

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    
    #미생물 정보 모아두기
    micro = []
    for _ in range(k):
        r, c, nums, d = map(int, input().split())
        micro.append([r, c, nums, d])

    #m초동안 진행
    for _ in range(m):

        #1. 이동
        for status in micro:
            status[0] += dirs[status[3]][0]
            status[1] += dirs[status[3]][1]

            #최외곽에 도착하면 > 미생물 수 절반, 방향은 반대로
            if status[0] == 0 or status[0] == n-1 or status[1] == 0 or status[1] == n - 1:
                status[2] //= 2
                status[3] = r_dirs[status[3]]

        #2. 이동 끝난 군집들을 위치별로 모으기        
        pos = {}
        for status in micro:
            if status[2] == 0:
                continue
            
            key = (status[0], status[1])
            if key not in pos:
                # **max값 별도 추적을 위해 마지막에 추가**
                pos[key] = [status[0], status[1], status[2], status[3], status[2]]
            
            #3. 이미 저장 된 위치가 있는데, 그 곳으로 또 가는 놈이 있는 경우 > 결합
            else:
                if status[2] > pos[key][4]:
                    pos[key][3] = status[3]
                    pos[key][4] = status[2]
                pos[key][2] += status[2]
        
        #4. 한 과정이 끝난 후 정보 갱신
        micro = [[v[0], v[1], v[2], v[3]] for v in pos.values()]

    #5. m초 후 남은 미생물 합치기
    ans = sum(status[2] for status in micro)
    print(f"#{tc} {ans}")