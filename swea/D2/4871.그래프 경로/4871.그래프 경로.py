def dfs(start, end):
    stack = []
    visited = [0] * (v+1)
    
    stack.append(start)
    visited[start] = 1

    while stack:
        now = stack.pop()

        for nxt in graph[now]:
            if nxt == end:
                return 1
            
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append(nxt)

    return 0

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, e = map(int, input().split())
    ans = dfs(s, e)

    print(f"#{tc} {ans}")