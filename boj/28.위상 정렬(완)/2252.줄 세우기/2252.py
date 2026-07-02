import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 핵심)노드에 진입차수 부여
ind = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1     # a -> b 이므로 b의 진입차수 1 증가 (b는 a를 먼저 처리해야 함)

q = deque()
for i in range(1, n+1):

    #차수가 0인 친구들부터 탐색 시작
    if ind[i] == 0:
        q.append(i)

#정렬 후 결과물 저장용
result = []

while q:
    now = q.popleft()
    result.append(now)

    # now 처리했으니까 now 다음 노드들 진입차수 -1
    # 0되면 이제 들어갈 수 있음
    for nxt in graph[now]:
        ind[nxt] -= 1       
        if ind[nxt] == 0:
            q.append(nxt)

#주어진 개수와 정렬된 수가 다르면 사이클이 존재 > 위상 정렬 불가
if len(result) != n:
    print(-1)
else:
    print(*result)