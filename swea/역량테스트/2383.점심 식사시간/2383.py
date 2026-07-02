def calc(arr, length):
    if not arr:
        return 0

    # 도착 시간 빠른 순으로 처리
    arr.sort()
    end = []

    for i in range(len(arr)):
        # 처음 3명은 도착하면 바로 내려감
        if i < 3:
            start = arr[i]
        else:
            # 4번째부터는 3명 제한 때문에 앞에서 3칸 먼저 들어간 놈 끝날 때까지 대기 가능
            start = max(arr[i], end[i - 3])

        # 내려가기 시작한 시간 + 계단 길이 = 끝나는 시간
        end.append(start + length)

    # 마지막 사람 끝나는 시간이 그 계단 종료 시간
    return end[-1]


def dfs(idx):
    global ans

    # 모든 사람 계단 배정 끝났으면 시간 계산
    if idx == len(people):
        t1 = calc(stair1_people[:], stair1_len)
        t2 = calc(stair2_people[:], stair2_len)
        ans = min(ans, max(t1, t2))
        return

    x, y = people[idx]

    # 1번 계단 가는 경우
    # 계단까지 이동시간 + 계단 입구 도착 후 1분
    dist1 = abs(x - stair1[0]) + abs(y - stair1[1]) + 1
    stair1_people.append(dist1)
    dfs(idx + 1)
    stair1_people.pop()

    # 2번 계단 가는 경우
    # 계단까지 이동시간 + 계단 입구 도착 후 1분
    dist2 = abs(x - stair2[0]) + abs(y - stair2[1]) + 1
    stair2_people.append(dist2)
    dfs(idx + 1)
    stair2_people.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    # 사람 위치랑 계단 위치 따로 저장
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] >= 2:
                stairs.append((i, j))

    stair1 = stairs[0]
    stair2 = stairs[1]
    stair1_len = board[stair1[0]][stair1[1]]
    stair2_len = board[stair2[0]][stair2[1]]

    # 각 계단으로 가는 사람들 도착 시간 저장용
    stair1_people = []
    stair2_people = []
    ans = float('inf')

    # 사람마다 어느 계단 갈지 완탐
    dfs(0)

    print(f'#{tc} {ans}')