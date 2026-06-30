import sys
from collections import deque
input = sys.stdin.readline

#사다리와 뱀 합쳐서 입력받아도 됨
n,m = map(int, input().split())
graph = [0] * 101

for _ in range(n+m):
    a, b = map(int,input().split())
    graph[a] = b

visited = [-1] * 101

#시작점
q = deque([1])
visited[1] = 0

while q:
    x = q.popleft()
    if x == 100:
        break
    
    #주사위 결과들
    for d in range(1,7):
        nx = x + d
        if nx > 100:
            continue
        
        #도착한 칸이 뱀/사다리 시작점이면 최종 도착칸으로 이동
        if graph[nx] != 0:
            nx = graph[nx]

        #최종 도착 칸 기준으로 방문 체크
        if visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[100])