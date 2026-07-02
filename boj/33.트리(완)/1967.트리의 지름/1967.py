#1167번 문제와 풀이가 같음

import sys
from collections import deque
input = sys.stdin.readline

def bfs(root, graph):
    k = len(graph)
    
    q = deque()
    visited = [-1] * k
    q.append(root)
    visited[root] = 0

    while q:
        now = q.popleft()

        #그래서 dist만 이용해봤네
        for nxt, dist in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + dist
                q.append(nxt)

    far_node = 0
    far_dist = 0

    for i in range(1, k):
        if far_dist < visited[i]:
            far_dist = visited[i]
            far_node = i

    return far_node, far_dist
                
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

a, b = bfs(n, graph)
c, d = bfs(a, graph)
print(d)