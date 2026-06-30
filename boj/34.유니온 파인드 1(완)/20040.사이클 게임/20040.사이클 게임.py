import sys
input = sys.stdin.readline

#find 재귀로 했다가 터짐. 반복문으로 할 수 밖에 없었다.
def find(x):
    root = x

    #루트찾기
    while parent[root] != root:
        root = parent[root]

    #경로 압축
    while parent[x] != x:
        nxt = parent[x]
        parent[x] = root
        x = nxt
    return root

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a


n, m = map(int, input().split())
parent = [i for i in range(n)]

for cnt in range(1, m+1):
    a, b = map(int, input().split())
    
    #서로 부모가 같은 경우 => 사이클임
    if find(a) == find(b):
        print(cnt)
        break

    union(a, b)

else:
    print(0)