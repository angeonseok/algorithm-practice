import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))         #이 문제는 단방향임.

start, end = map(int, input().split())

INF = 10**18
dist = [INF] * (n + 1)
trace = [-1] * (n + 1)          #경로 추적용
dist[start] = 0
pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            trace[v] = u        #v 직전 노드 저장
            heapq.heappush(pq, (nd, v))

ans = []
cur = end

#trace 따라가며 경로 복원
while cur != -1:
    ans.append(cur)
    cur = trace[cur]    

print(dist[end])
print(len(ans))
print(*reversed(ans))