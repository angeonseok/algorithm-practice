import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX+1)

q = deque()
q.append(n)
visited[n] = 0

while q:
    a = q.popleft()
    
    #순간이동시
    na = a * 2
    if 0 <= na <= MAX and visited[na] == -1:
        visited[na] = visited[a]    #시간은 그대로
        q.appendleft(na)            #순서는 덱 맨 앞으로 다시 넣기

    #걸으면 그냥 append
    for na in (a - 1, a + 1):
        if 0 <= na <= MAX and visited[na] == -1:
            visited[na] = visited[a] + 1
            q.append(na)

print(visited[k])