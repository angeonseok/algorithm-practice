from collections import deque

#즐거운 위상정렬
def t_sort(graph, ind, v):

    #우선 차수가 0인 친구들부터 시작해야됨.
    q = deque()
    for i in range(1, v + 1):
        if ind[i] == 0:
            q.append(i)

    #순서를 저장해보자
    result = []
    while q:
        now = q.popleft()
        result.append(now)

        #현재 위치에서 도달 가능한 친구들의 차수를 까자
        for nxt in graph[now]:
            ind[nxt] -= 1

            #만약 그 차수가 0이 되면 다음 순서로 넣어주자
            if ind[nxt] == 0:
                q.append(nxt)

    #결과와 정점 개수가 다름 = 사이클 발생이라 위상정렬 불가능
    if len(result) != v:
        return False

    return result

    
for tc in range(1, 11):
    v, e = map(int, input().split())
    tmp = list(map(int, input().split()))

    graph = [[] for _ in range(v + 1)]

    #위상정렬은 차수를 부여해줘야됨
    ind = [0] * (v+1)

    #a -> b 단일 경로. a가 이뤄진 후, b가 이뤄져야하므로 a의 차수가 1  더 높음
    for i in range(e):
        a, b = tmp[2 * i], tmp[2 * i + 1]
        graph[a].append(b)
        ind[b] += 1

    result = t_sort(graph, ind, v)

    print(f'#{tc}', *result)