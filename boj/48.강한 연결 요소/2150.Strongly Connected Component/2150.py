import sys
sys.setrecursionlimit(100000)   #재귀를 2번 돌려서 걸어야함

def kosaraju(graph, r_graph, V):
    visited = [False] * (V + 1)
    order = []


    def dfs1(v):
        visited[v] = True
        for nxt in graph[v]:
            if not visited[nxt]:
                dfs1(nxt)

        #다 보고 나오면서 순서 저장. 나중에 종료 순서 역순으로 봐야됨
        order.append(v)

    for v in range(1, V+1):
        if not visited[v]:
            dfs1(v)

    visited = [False] * (V + 1)
    sccs = []

    #역방향 그래프에서 연결된 애들 다 묶기
    def dfs2(v, scc):
        visited[v] = True
        scc.append(v)
        for nxt in r_graph[v]:
            if not visited[nxt]:
                dfs2(nxt, scc)
    
    #종료 순서의 역순으로 보면서 역방향 그래프 dfs 함 돌리기
    while order:
        v = order.pop()

        if not visited[v]:
            scc = []
            dfs2(v, scc)
            sccs.append(scc)
    
    return sccs

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
r_graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)

sccs = kosaraju(graph, r_graph, v)

#출력 조건에 맞게 정렬 및 가공
for scc in sccs:
    scc.sort()
    scc.append(-1)
sccs.sort(key=lambda x: x[0])

print(len(sccs))
for scc in sccs:
    print(*scc)