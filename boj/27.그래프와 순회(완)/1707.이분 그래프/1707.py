import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())

    #맨날하는 그래프 생성
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    visited = [-1] * (v + 1)

    #이분 그래프 조건 체크용
    flag = True

    for i in range(1, v+1):
        #방문 안한 놈이 있다면
        if visited[i] == -1:
            
            #그놈을 기준으로
            q.append(i)
            
            #순회를 해
            while q:
                a = q.popleft()
                if visited[a] == -1:

                    #색칠하기
                    visited[a] = 0

                for j in graph[a]:

                    #인접 노드와 서로 다른 색으로 칠하기
                    if visited[j] == -1:
                        visited[j] = 1 - visited[a]
                        q.append(j)

                    #이미 방문한 인접 노드와 같으면 이분 그래프 아님 >> 바로 종료
                    elif visited[j] == visited[a]:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")  