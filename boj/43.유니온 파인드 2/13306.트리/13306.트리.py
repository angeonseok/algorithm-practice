import sys
input = sys.stdin.readline

#재귀 43점 > 반복문 100점
#n이 20만이라 그런듯
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

#find 고치고 100점 안나오면 여기도 손봐야 했는데 다행
def union(a, b):
    ra = find(a)
    rb = find(b)

    parent[rb] = ra

n, q = map(int, input().split())
parent = list(range(n + 1))         #유니온 파인드에서 사용하는 부모 배열

#문제에서 주어지는 부모 배열
tree_parent = list(range(n + 1))
for i in range(2, n+1):
    a = int(input())
    tree_parent[i] = a

#일단 받아두고
queries = [list(map(int, input().split())) for _ in range(n - 1 + q)]

#질문을 역순으로 처리할 예정
#그러면 처음에는 전부 연결이 끊긴 상태로 볼 수 있지
ans = []
for cmd in reversed(queries):

    #삭제를 거꾸로 보면 연결
    if cmd[0] == 0:
        b = cmd[1]
        union(b, tree_parent[b])
    
    #경로 가능성 체크
    else:
        c, d = cmd[1], cmd[2]
        
        if find(c) == find(d):
            ans.append("YES")
        
        else:
            ans.append("NO")

#역순으로 처리했으므로 돌려놔
for j in reversed(ans):
    print(j)