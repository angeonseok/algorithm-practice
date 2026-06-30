import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    last_list = list(map(int, input().split()))
    
    ind = [0] * (n + 1)
    
    #변경을 여러번 하는 경우 set 추천(gpt)
    graph = [[] for _ in range(n+1)]

    #graph[a] = a보다 뒤에 와야 하는 팀들
    for i in range(n-1):
        a = last_list[i]
        arr = last_list[i+1:]

        for j in arr:
            graph[a].append(j)
            ind[j] += 1

    #순위 변경 정보 반영
    m = int(input())
    for _ in range(m):
        a, b = map(int,input().split())

        #현재 b -> a 라면 , a -> b로 뒤집기
        if a in graph[b]:
            graph[b].remove(a)  
            ind[a] -= 1
            ind[b] += 1
            graph[a].append(b)
        
        #그 역도 넣어야지
        else:
            graph[a].remove(b)
            ind[b] -= 1
            ind[a] += 1
            graph[b].append(a)

    q = deque()
    for k in range(1, n+1):
        if ind[k] == 0:
            q.append(k)

    #flag = True면 정렬 순서 여러개라 확정 불가능
    flag = False
    result = []
    while q:
        if len(q) >= 2:
            flag = True
            break

        now = q.popleft()
        result.append(now)

        for nxt in graph[now]:
            ind[nxt] -= 1
            if ind[nxt] == 0:
                q.append(nxt)

    if flag:
        print("?")
    elif len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")