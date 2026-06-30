from collections import defaultdict

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

reflect = {
    1: {0: 1, 1: 3, 2: 0, 3: 2},
    2: {0: 3, 1: 0, 2: 1, 3: 2},
    3: {0: 2, 1: 0, 2: 3, 3: 1},
    4: {0: 1, 1: 2, 2: 3, 3: 0},
    5: {0: 1, 1: 0, 2: 3, 3: 2},
}

def game(arr, si, sj, d):
    i, j = si, sj
    score = 0

    while True:
        ni = i + dirs[d][0]
        nj = j + dirs[d][1]

        arr_object = arr[ni][nj]

        # 블랙홀에 박으면 종료
        if arr_object == -1:
            return score
        
        # 블록에 박으면 방향전환 + 점수
        if 1 <= arr_object <= 5:
            d = reflect[arr_object][d]
            score += 1
        
        # 웜홀에 가면 위치 이동
        elif 6 <= arr_object <= 10: 
            a, b = wormhole[arr_object]
            if (ni, nj) == a:
                ni, nj = b
            else:
                ni, nj = a

        i, j = ni, nj   #위치 업데이트 >> 이거 없어서 박음

        # 시작점 오면 끝
        if ni == si and nj == sj:
            return score
        

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr_input = [list(map(int, input().split())) for _ in range(n)]

    # 외곽박은거 >> 5번 블록 박은거로 바꿔 계산하기 위해 패딩
    arr = [[5] * (n + 2)]
    for row in arr_input:
        arr.append([5] + row + [5])
    arr.append([5] * (n + 2))

    # 웜홀 좌표 미리 저장
    wormhole = {6: [], 7: [], 8: [], 9: [], 10: [], }
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if 6 <= arr[i][j] <= 10:
                wormhole[arr[i][j]].append((i, j))

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 0:
                for d in range(4):
                    ans = max(ans, game(arr, i, j, d))
    
    print(f"#{tc} {ans}")