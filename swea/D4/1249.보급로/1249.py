import heapq

INF = 10**18
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    dist = [[INF] * n for _ in range(n)]
    pq = [(0, 0, 0)]

    while pq:
        w, i, j = heapq.heappop(pq)

        if w > dist[i][j]:
            continue

        if (i, j) == (n-1, n-1):
            break

        for dir in dirs:
            ni, nj = i + dir[0], j + dir[1]

            if 0 <= ni < n and 0 <= nj < n:
                nw = w + arr[ni][nj]

                if nw < dist[ni][nj]:
                    dist[ni][nj] = nw
                    heapq.heappush(pq, (nw, ni, nj))

    print(f'#{tc} {dist[n-1][n-1]}')