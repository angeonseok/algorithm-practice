import sys
from collections import deque
input = sys.stdin.readline

dirs = ((0,1), (1,0),(0,-1),(-1,0))

def island(arr):
    q = deque()
    cnt = 1
    i_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i,j))
                arr[i][j] += cnt
                cnt +=1
                i_cnt += 1

                while q:
                    x, y = q.popleft()

                    for dir in dirs:
                        nx, ny = x + dir[0], y + dir[1]
                        if not(0 <= nx < n and 0 <= ny < m):
                            continue
                        if arr[nx][ny] == 1:
                            arr[nx][ny] = arr[x][y]
                            q.append((nx,ny))

    return arr, i_cnt


def bridge(arr):
    temp= []

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cur_i = arr[i][j]

                for dir in dirs:
                    cnt = 0
                    ni, nj = i + dir[0], j + dir[1]

                    while 0 <= ni < n and 0 <= nj < m:
                        if arr[ni][nj] == cur_i:
                            break
                        
                        if arr[ni][nj] == 0:
                            cnt += 1
                            ni += dir[0]
                            nj += dir[1]
                            continue

                        if arr[ni][nj] != 0 and arr[ni][nj] != cur_i:
                            c = arr[ni][nj]
                            if cnt >= 2:
                                temp.append((cnt, cur_i, c))
                            break                    
    #크루스칼은 간선 리스트 그대로 사용 (중복은 union-find가 걸러줌)
    return temp


#union-find
def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True


#섬 번호가 2부터 시작하므로 parent 크기 v + 2
def kruskal(v, edges):
    parent = list(range(v + 2))
    edges.sort()
    total = 0
    cnt = 1     #정점 1개에서 시작, 간선 하나 붙을 때마다 +1

    for w, a, b in edges:
        if cnt == v:
            break
        if union(parent, a, b):
            total += w
            cnt += 1

    return total, cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr, i_cnt = island(arr)
edges = bridge(arr)
total, cnt = kruskal(i_cnt, edges)

#kruskal도 cnt를 연결된 정점 수로 보내준다
if cnt != i_cnt:
    print(-1)
else:
    print(total)