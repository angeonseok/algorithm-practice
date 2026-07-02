#정석은 bfs라는데 이해가 안되서 유니온 파인드로 풀음

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    #서로의 루트노드가 같다 = 사이클임
    if ra == rb:
        cycle[ra] = True
        return
    
    #합치면서 사이클 여부도 넘김
    parent[rb] = ra
    cycle[ra] = cycle[ra] or cycle[rb]

import sys
input = sys.stdin.readline

case = 1

while True:
    n, m = map(int, input().split())

    #종료조건있음
    if n == 0 and m == 0:
        break
    
    parent = list(range(n+1))
    cycle = [False] * (n+1)
    
    #사이클 여부 체크
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    # 트리인 묶음 개수 셀거
    roots = set()
    cnt = 0

    #그냥 시작하면 parent[i]가 루트노드라는 보장이 없다
    #이거 때문에 함 틀림
    for i in range(1, n+1):
        parent[i] = find(i)

    #돌리자
    for i in range(1, n+1):
        root = parent[i]

        #루트 기준으로 보면서 사이클 없는 애들만 트리다.
        if root not in roots and not cycle[root]:
            roots.add(root)
            cnt += 1

    if cnt == 1:
        print(f"Case {case}: There is one tree.")
    elif cnt > 1:
        print(f"Case {case}: A forest of {cnt} trees.")
    else:
        print(f"Case {case}: No trees.")

    case += 1