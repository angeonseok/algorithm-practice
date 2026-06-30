import sys
input = sys.stdin.readline

def bipartite_matching(graph, left_size, right_size):
    match_left = [-1] * (left_size + 1)     #왼쪽 정점이 현재 누구랑 매칭됐는지
    match_right = [-1] * (right_size + 1)   #오른쪽 정점이 현재 누구랑 매칭됐는지

    def dfs(v, visited):
        #왼쪽 v가 연결할 수 있는 오른쪽 정점 확인
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True

            #1. 비어있거나
            #2. 이미 누가 차지중이어도, 그 놈을 다른 데 옮길 수 있으면 매칭
            if match_right[u] == -1 or dfs(match_right[u], visited):
                match_left[v] = u
                match_right[u] = v
                return True
        
        return False
    
    result = 0
    
    #왼쪽 정점 하나씩 보면서 매칭 시도
    for v in range(1, left_size + 1):
        visited = [False] * (right_size + 1)
        if dfs(v, visited):
            result += 1
    
    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    work = arr[1: cnt + 1]
    graph[i].extend(work)

ans = bipartite_matching(graph, n, m)
print(ans)