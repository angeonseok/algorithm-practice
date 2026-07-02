T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        num, d = map(int, input().split())
        num -= 1

        # 이번 명령에서 각 톱니 회전 방향 먼저 기록
        rot = [0] * 4
        rot[num] = d

        # 왼쪽으로 전파 확인
        for i in range(num, 0, -1):
            if arr[i][6] != arr[i - 1][2]:
                rot[i - 1] = -rot[i]
            else:
                break

        # 오른쪽으로 전파 확인
        for i in range(num, 3):
            if arr[i][2] != arr[i + 1][6]:
                rot[i + 1] = -rot[i]
            else:
                break

        # 전파 다 본 뒤 한 번에 회전
        for i in range(4):
            if rot[i] == 1:   # 시계
                arr[i] = [arr[i][-1]] + arr[i][:-1]
            elif rot[i] == -1:   # 반시계
                arr[i] = arr[i][1:] + [arr[i][0]]

    # 12시 방향이 S극이면 점수 더하기
    ans = 0
    if arr[0][0] == 1:
        ans += 1
    if arr[1][0] == 1:
        ans += 2
    if arr[2][0] == 1:
        ans += 4
    if arr[3][0] == 1:
        ans += 8

    print(f'#{tc} {ans}')