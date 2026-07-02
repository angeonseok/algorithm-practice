#전형적인 위상정렬
from collections import deque

T = 10
for tc in range(1, T+1):
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)

    #그래프 연결 + 차수 부여
    for i in range(0,len(arr),2):
        a = arr[i]
        b = arr[i+1]
        graph[a].append(b)
        indegree[b] += 1
    
    #차수 0인 친구들 부터 꺼내기
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        node = q.popleft()
        ans.append(node)

        #차수를 점차 감소시키면서 0이 되면 다음 순서로 나올 준비
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(f"#{tc} " + " ".join(map(str, ans)))