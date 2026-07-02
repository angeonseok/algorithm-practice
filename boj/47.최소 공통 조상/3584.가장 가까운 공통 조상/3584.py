#부모 - 자식 연결관계를 줌
#그럼 걍 부모노드 거슬러가면서 방문체크하면 되지 않냐
import sys

T = int(input())
for _ in range(T):
    n = int(input())
    parent = [-1] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    
    node_1, node_2 = map(int, input().split())
    visited = [0] * (n+1)

    #첫번째 노드 기준 부모 방문체크
    idx_1 = node_1
    while idx_1 != -1:
         visited[idx_1] = 1
         idx_1 = parent[idx_1]
    
    #두번째 노드 기준으로 부모 거슬러 올라감 > 방문체크된 놈 처음 만나면 그게 lca
    idx_2 = node_2
    while idx_2 != -1:
        if visited[idx_2]:
            print(idx_2)
            break
        
        idx_2 = parent[idx_2]