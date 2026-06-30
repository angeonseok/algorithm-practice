import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문 체크 + 부모노드 저장용 리스트 생성
visited = [0] * (n+1)
p = [0] * (n+1)

#루트를 1로 설정
q = deque([1])
visited[1] = -1

#bfs로 순회하면서 a의 자식들 체크 > 자식들의 자식 체크 .............
while q:
    a = q.popleft()
    for i in graph[a]:
        if visited[i] == 0:
            visited[i] = -1
            p[i] = a
            q.append(i)

for i in p:
    if i != 0:
        print(i)