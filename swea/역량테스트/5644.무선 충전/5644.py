# 0 이동없음, 1 상, 2 우, 3 하, 4 좌
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    moveA = [0] + list(map(int, input().split()))
    moveB = [0] + list(map(int, input().split()))

    bc = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        bc.append((y, x, c, p))   # 행, 열로 바꿔 저장

    ax, ay = 1, 1
    bx, by = 10, 10
    ans = 0

    for t in range(M + 1):
        # 현재 시간 이동 적용
        ax += dx[moveA[t]]
        ay += dy[moveA[t]]
        bx += dx[moveB[t]]
        by += dy[moveB[t]]

        a_list = []
        b_list = []

        # 현재 위치에서 잡히는 BC 찾기
        for i in range(A):
            x, y, c, p = bc[i]

            if abs(ax - x) + abs(ay - y) <= c:
                a_list.append(i)

            if abs(bx - x) + abs(by - y) <= c:
                b_list.append(i)

        # 아무 BC도 못 쓰는 경우 대비
        a_list.append(-1)
        b_list.append(-1)

        best = 0

        # A, B가 고를 수 있는 BC 조합 전부 비교
        for ai in a_list:
            for bi in b_list:
                total = 0

                if ai == -1 and bi == -1:
                    total = 0
                elif ai == -1:
                    total = bc[bi][3]
                elif bi == -1:
                    total = bc[ai][3]
                elif ai == bi:
                    # 같은 BC 고르면 성능은 한 번만 반영
                    total = bc[ai][3]
                else:
                    total = bc[ai][3] + bc[bi][3]

                best = max(best, total)

        ans += best

    print(f'#{tc} {ans}')