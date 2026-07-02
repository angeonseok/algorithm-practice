def bfs(v):
    global cnt
    #큐를 생성 한 후 정점 입력
    queue = deque([v])
    visited[v] = cnt

    #큐가 빌 때까지 반복
    while queue:
        #맨 앞 정점 꺼냄
        node = queue.popleft()

        #현재 정점과 연결된 모든 인접 정점 탐색
        for i in graph[node]:

            #방문 안했으면 방문 처리
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt

                #방문한 정점을 큐에 삽입.이후 이 정점의 인접 노드 탐색
                queue.append(i)

import sys
from collections import deque
input = sys.stdin.readline

#기본적으로 dfs랑 형식 자체가 비슷함
n, m, v = map(int,input().split())

visited = [0] * (n + 1)
cnt = 1

graph =[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

bfs(v)

for i in range(1, n+1):
    print(visited[i])