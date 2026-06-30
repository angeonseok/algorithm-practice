import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

#k+1로 하니까 걍 뛰쳐나감
q = deque()
visited = [-1] * 100001
trace = [-1] * 100001

q.append(n)
visited[n] = 0

while q:
    now = q.popleft()
    
    if now == k:
        break

    for nxt in (now - 1, now + 1, now * 2):
        if not (0 <= nxt < 100001):
            continue
        
        #이전 노드 위치만 기록해두면 끝
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            trace[nxt] = now
            q.append(nxt)   

#역추적
cur = k
ans = []
while cur != -1:
    ans.append(cur)
    cur = trace[cur]

print(visited[k])
print(*reversed(ans))