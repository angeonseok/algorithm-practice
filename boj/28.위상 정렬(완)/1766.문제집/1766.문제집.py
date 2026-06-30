import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ind = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

#위상 정렬 중 번호 작은 순으로 뽑으라면 heap쓰래.
heap = []
for i in range(1, n+1):
    if ind[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)

    for i in graph[now]:
        ind[i] -= 1
        if ind[i] == 0:
            heapq.heappush(heap, i)

if len(result) != n:
    print('정렬 불가')
else:
    print(*result)