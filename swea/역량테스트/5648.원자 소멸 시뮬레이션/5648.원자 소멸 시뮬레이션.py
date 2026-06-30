dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = []

    for _ in range(N):
        x, y, d, e = map(int, input().split())

        # 0.5초 단위 충돌까지 잡으려고 좌표 2배로 뻥튀기
        atoms.append([x * 2, y * 2, d, e])

    ans = 0
    LIMIT = 4000

    # 좌표 범위 끝까지 시간 진행
    for _ in range(LIMIT):
        pos = {}

        # 이동 + 범위 안에 남아있는 원자만 저장
        moved = []
        for x, y, d, e in atoms:
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 밖으로 나간 놈은 버림
            if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
                moved.append([nx, ny, d, e])
                key = (nx, ny)

                # 같은 위치에 몇 개 모였는지 카운트
                pos[key] = pos.get(key, 0) + 1

        # 충돌한 원자는 에너지 더하고 제거
        new_atoms = []
        for x, y, d, e in moved:
            if pos[(x, y)] >= 2:
                ans += e
            else:
                new_atoms.append([x, y, d, e])

        # 살아남은 원자들로 갱신
        atoms = new_atoms

        # 다 사라졌으면 더 볼 필요 없음
        if not atoms:
            break

    print(f'#{tc} {ans}')