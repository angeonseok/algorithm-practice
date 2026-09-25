#예전에 적어둔게 있어서 보고 걍 갈김. 이건 코사라주 풀이
T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    r_graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        r_graph[b].append(a)

    visited = [False] * (v + 1)
    order = []

    def dfs1(v):
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                dfs1(i)

        order.append(v)

    for i in range(1, v+1):
        if not visited[i]:
            dfs1(i)

    visited_r = [False] * (v + 1)
    sccs = []

    def dfs2(v, scc):
        visited_r[v] = True
        scc.append(v)
        
        for i in r_graph[v]:
            if not visited_r[i]:
                dfs2(i, scc)

    while order:
        v = order.pop()
        if not visited_r[v]:
            scc = []
            dfs2(v, scc)
            sccs.append(scc)

    print(f'#{tc} {len(sccs)}')