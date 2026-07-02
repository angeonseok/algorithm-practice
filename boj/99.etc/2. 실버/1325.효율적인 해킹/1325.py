import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

link = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)  #b > a로 해킹가능

for i in range(1, n+1):
    q = deque()
    visited = [-1] * (n+1)
    cnt = 1
    
    q.append(i)
    visited[i] = 0
    while q:
        x = q.popleft()
        
        #현재 컴퓨터에서 해킹가능한 컴퓨터 수 카운팅
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = 1
                cnt += 1
                q.append(nx)

    #결과 저장
    link[i] = cnt

#최대로 해킹할 수 있는 컴퓨터를 골라보자
max_link = max(link)

#여러개면 오름차순 출력
for j in range(1, n+1):
    if link[j] == max_link:
        print(j, end = " ")