from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    visited = [-1] * 1000001
    q = deque([n])
    visited[n] = 0

    while q:
        now = q.popleft()

        #목표지점이면 걍 끝내
        if now == m:
            break

        #다음 지점은 4가지 연산 결과 중 하나
        for nxt in (now + 1, now - 1, now * 2, now - 10):
            if 0 <= nxt < 1000001 and visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

    print(f'#{tc} {visited[m]}')