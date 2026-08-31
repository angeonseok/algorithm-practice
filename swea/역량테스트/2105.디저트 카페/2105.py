#좌하, 우하, 우상, 좌상
dirs = ((1, -1), (1, 1), (-1, 1), (-1, -1))


#시작좌표, 현재좌표, 방향 정보, 쳐먹은 개수
def sol(si, sj, ci, cj, d, cnt):
    global ans

    #돌아서 시작지점으로 온 경우 값 갱신
    if d != 0 and (si, sj) == (ci, cj):
        ans = max(ans, cnt)
        return

    #현재 방향, 다음 방향만 따진다.
    for nd in (d, d + 1):

        #d가 가질 수 있는 값은 3이 최대
        if nd > 3:
            continue

        ni, nj = ci + dirs[nd][0], cj + dirs[nd][1]
        if 0 <= ni < n and 0 <= nj < n:

            #시작점을 visited 처리해서 그냥 돌리면 못감.
            if (si, sj) == (ni, nj):

                #사각형을 그리면서 도착하려면 nd = 3이여야하네.
                if nd == 3:
                    sol(si, sj, ni, nj, nd, cnt)

            #시작점 가는거 아니면 계속 진행
            elif cafe[ni][nj] not in visited:
                visited.add(cafe[ni][nj])
                sol(si, sj, ni, nj, nd, cnt + 1)
                visited.remove(cafe[ni][nj])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]

    visited = set()

    ans = -1
    #탐색 범위를 좁혀봤다. 종이로 그려봐라
    for i in range(n - 2):
        for j in range(1, n - 1):
            visited.add(cafe[i][j])
            sol(i, j, i, j, 0, 1)
            visited.remove(cafe[i][j])

    print(f'#{tc} {ans}')