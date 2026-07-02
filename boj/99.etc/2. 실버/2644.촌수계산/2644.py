import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x, y = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q =deque()
visited = [-1] * (n+1)
q.append(x)
visited[x] = 0

while q:
    a = q.popleft()

    for i in graph[a]:
        if visited[i] == -1:
            visited[i] = visited[a] + 1
            q.append(i)

print(visited[y])