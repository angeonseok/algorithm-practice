def check(arr, X):
    N = len(arr)
    # 경사로 이미 쓴 칸 체크용
    used = [0] * N
    i = 0

    while i < N - 1:
        # 같은 높이면 그냥 감
        if arr[i] == arr[i + 1]:
            i += 1

        # 오르막이면 뒤쪽 X칸이 전부 같아야 됨
        elif arr[i] + 1 == arr[i + 1]:
            for j in range(i, i - X, -1):
                if j < 0 or arr[j] != arr[i] or used[j]:
                    return False
                used[j] = 1
            i += 1

        # 내리막이면 앞쪽 X칸이 전부 같아야 됨
        elif arr[i] - 1 == arr[i + 1]:
            for j in range(i + 1, i + X + 1):
                if j >= N or arr[j] != arr[i + 1] or used[j]:
                    return False
                used[j] = 1
            i += X

        else:
            return False

    return True


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 각 행, 열이 활주로 가능한지 검사
    for i in range(N):
        if check(board[i], X):
            ans += 1

        col = []
        for j in range(N):
            col.append(board[j][i])

        if check(col, X):
            ans += 1

    print(f'#{tc} {ans}')