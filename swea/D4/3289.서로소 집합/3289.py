#전형적인 유니온파인드

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
 
 
def union(a, b):
    ra = find(a)
    rb = find(b)
     
    if ra != rb:
        parent[rb] = ra
 
 
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parent = list(range(n+1))
     
    ans = ""
    for _ in range(m):
        cmd, a, b = map(int, input().split())
 
        if cmd  == 0:
            union(a, b)
         
        else:
            if find(a) == find(b):
                ans += '1'
            else:
                ans += '0'
 
    print(f"#{tc} {ans}")