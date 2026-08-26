# 합치려다가 참사났다.
def sol(v, cnt):
    global ans
    ans = max(ans, cnt)

    for nxt in graph[v]:
        if not visited[nxt]:
            visited[nxt] = True
            sol(nxt, cnt + 1)
            visited[nxt] = False


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    #중복 방문 가딩
    visited = [False] * (n+1)
    ans = 1

    #모든 정점에서 가능 경로 체크하기
    for i in range(n+1):
        visited[i] = True
        sol(i, 1)
        visited[i] = False

    print(f'#{tc} {ans}')