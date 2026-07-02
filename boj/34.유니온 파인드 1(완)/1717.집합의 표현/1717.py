import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#자기 자신을 부모로 시작해보자
parent = [i for i in range(n+1)]

#x의 루트를 경로를 압축하면서 찾자
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

#서로의 루트가 다를 경우 통합하자(b루트를 a루트 밑으로)
def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)

    else:
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            print("yes")
        else:
            print("no")