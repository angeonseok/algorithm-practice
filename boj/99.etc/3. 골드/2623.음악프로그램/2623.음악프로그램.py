import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

ind = [0] * (n+1)
graph = [[] for _ in range(n+1)]

#들어오는 입력형태를 잘 보자
for _ in range(m):
    s = list(map(int,input().split()))
    k = s[0]
    arr = s[1:]
    for i in range(k-1):
        a = arr[i]
        b = arr[i+1]
        graph[a].append(b)
        ind[b] += 1

ans = []
q = deque()
for j in range(1, n+1):
    if ind[j] == 0:
        q.append(j)

while q:
    now = q.popleft()
    ans.append(now)

    for nxt in graph[now]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            q.append(nxt)

if len(ans) != n:
    print(0)
else:
    for k in range(n):
        print(ans[k])