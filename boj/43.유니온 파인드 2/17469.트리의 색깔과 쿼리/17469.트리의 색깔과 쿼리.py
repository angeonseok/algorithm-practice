#쿼리를 역순 처리 할 것
# 끊는다 > 연결한다로 바꿔 처리

def find(x, uf_parent):
    while x != uf_parent[x]:
        uf_parent[x] = uf_parent[uf_parent[x]]
        x = uf_parent[x]
    return x

#대표 부모 연결 + 색집합 합치기
def union(a, b, sets):
    ra = find(a, uf_parent)
    rb = find(b, uf_parent)

    #작은 놈을 큰 놈에 합치기
    if ra != rb:
        if len(sets[ra]) < len(sets[rb]):
            ra, rb = rb, ra

        uf_parent[rb] = ra
        sets[ra] |= sets[rb]

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

#원래 부모 노드 저장
tree_parent = list(range(n + 1))
for i in range(2, n + 1):
    a = int(input().rstrip())
    tree_parent[i] = a

#각 노드별 색을 담을 예정
sets = [set() for _ in range(n + 1)]
for j in range(1, n + 1):
    color = int(input().rstrip())
    sets[j].add(color)

#저장 후 역순 처리 할 예정
queries = [list(map(int, input().split())) for _ in range(n + q - 1)]

#문제에서 연결할 부모와 구분하기 위해 이렇게 작명
uf_parent = list(range(n + 1))
ans = []

#역순 처리
for cmd, node in reversed(queries):
    #부모 노드와 연결
    if cmd == 1:
        union(node, tree_parent[node], sets)
    
    #현재 노드가 속한 컴포넌트의 색 개수 확인
    else:
        root = find(node, uf_parent)
        ans.append(len(sets[root]))

#출력을 역순으로 해야 맞음
for i in ans[::-1]:
    print(i)