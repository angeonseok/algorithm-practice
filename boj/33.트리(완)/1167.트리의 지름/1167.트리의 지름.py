import sys
from collections import deque
input = sys.stdin.readline

    
#(간선수, 누적거리) 식으로 저장할 예정. 지금 보니까 간선도 필요없어보이는데.. 걍 지워도 될 듯
def bfs(start, graph):
    n = len(graph)
    visited =  [-1] * n

    q = deque()
    q.append(start)

    visited[start] = (0, 0)

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt[0]] == -1:
                v = nxt[1]
                visited[nxt[0]] = (visited[now][0] + 1, visited[now][1] + v)
                q.append(nxt[0])

    far_node = 0
    far_dist = 0

    #제일 먼 노드와 그 거리를 반환
    for i in range(1, n):
        if visited[i] == -1:
            continue

        if visited[i][1] > far_dist:
            far_node = i
            far_dist = visited[i][1]
    
    return far_node, far_dist


V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    arr.pop()          #-1 제거
    p = arr[0]

    # (정점, 비용) 쌍으로 추가
    for i in range(1, len(arr), 2):
        graph[p].append((arr[i], arr[i + 1]))

#이 문제는 2번 돌려야됨
a, b = bfs(1, graph)    #루트(1)부터 해서 제일 먼 놈 찾고
c, d = bfs(a, graph)    #그 놈 기준으로 제일 먼 거리가 정답
print(d)