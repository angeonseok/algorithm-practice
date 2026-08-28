#벽까지 경로 만들어서 길이 재는 함수
#위치정보, 방향정보, 경로에 쳐넣을 값
def create_line(i, j, d, v):
    ni = i + d[0]
    nj = j + d[1]

    cnt = 0
    while 0 <= ni < n and 0 <= nj < n:
        #경로 중 다른 장애물이 있는 경우, 경로 생성 불가
        #이미 2로 칠한 애들 다시 0으로 돌려줘야함.
        if arr[ni][nj]:
            bi, bj = i + d[0], j + d[1]
            for _ in range(cnt):
                arr[bi][bj] = 0
                bi += d[0]
                bj += d[1]
            return -1

        arr[ni][nj] = v
        cnt += 1
        ni += d[0]
        nj += d[1]

    #벽까지 이어졌다면 그 경로의 길이 반환
    return cnt


#만든 경로를 저 함수 하나로 다 처리하긴 그래서 경로 지우는 함수 만든
def erase(i, j, d, L):
    ni = i + d[0]
    nj = j + d[1]

    for i in range(L):
        arr[ni][nj] = 0
        ni += d[0]
        nj += d[1]


#idx번째 코어, 거기까지 선택된 총 코어수, 총 길이
def sol(idx, cnt, length):
    global max_cnt, min_len

    #마지막 코어까지 가서
    if idx == len(core):

        #갱신조건: 최대 코어수 or 코어수 같을 때, 더 짧은 경로
        if cnt > max_cnt or (max_cnt == cnt and length < min_len):
            max_cnt = cnt
            min_len = length
        return


    i, j = core[idx]
    #코어 4방향 다 봐야됨
    for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):

        #연결
        L = create_line(i, j, d, 2)

        #연결 안되면 걍 넘겨
        if L < 0:
            continue

        #되면 선택하고 갯수와 길이 더해
        sol(idx + 1, cnt + 1, length + L)

        #연결 해제
        erase(i, j, d, L)

    #이번 코어 선택 안하고 넘어가는 경우
    sol(idx + 1, cnt, length)

    
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #일단 액시노스 좌표를 따
    core = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                if 0 < i < n-1 and 0 < j < n-1:
                    core.append((i, j))

    max_cnt = -1
    min_len = 0
    
    sol(0, 0, 0)
    print(f'#{tc} {min_len}')