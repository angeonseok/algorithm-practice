import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    #사이즈도 계산해서 리턴시켜주기
    if root_a != root_b:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    return size[root_a]

T = int(input())
for _ in range(T):
    n = int(input())

    #문자열이라 딕셔너리가 떠오르더라
    parent = {}
    size = {}
    for i in range(n):
        a, b = map(str, input().split())
        
        #숫자로 줄떄는 for문으로 자기 자신 parent 등록하고 사이즈도 넣었는데..
        #딕셔너리로 받아서 해야하니 먼저 등록하고 union시키자
        if a not in parent:
            parent[a] = a
            size[a] = 1

        if b not in parent:
            parent[b] = b
            size[b] = 1

        print(union(a, b))