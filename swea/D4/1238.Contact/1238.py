from collections import deque

for tc in range(1, 11):
    l, s = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, l, 2):
        a, b = arr[i], arr[i+1]
        graph[a].append(b)

    visited = [False] * 101
    q = deque([s])
    visited[s] = True

    ans = s

    #걍 max 떄려박으니까 들린 놈들 중 최댓값 뽑더라고.
    while q:
        ans = max(q)

        #현재 시점의 내용물에서만 따진다.
        for _ in range(len(q)):
            now = q.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

    print(f'#{tc} {ans}')
