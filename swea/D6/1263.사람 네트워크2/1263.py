from collections import deque

def bfs(v):
    visited  = [-1] * n
    visited[v] = 0
    q = deque([v])
    total = 0

    while q:
        now = q.popleft()
        
        for i in range(n):
            if arr[now][i] and visited[i] == -1:
                visited[i] = visited[now] + 1
                total += visited[i]

                #가지치기 넣어봤네.
                if total >= ans:
                    return ans

                q.append(i)

    return total


T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    n = tmp[0]

    #일단은 행렬로 한다.
    arr = [tmp[i:i+n] for i in range(1, len(tmp), n)]

    #모든 정점 bfs돌려서 최소 구해보자.
    ans = float('inf')
    for i in range(n):
        ans = min(ans, bfs(i))

    #이 문제 왠지 모르겠는데 플로이드가 안터짐
    print(f'#{tc} {ans}')