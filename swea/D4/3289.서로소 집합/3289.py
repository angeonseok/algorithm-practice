# 1들어오면 부모 비교
def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


#0들어오면 합치기
def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    parent = list(range(n + 1))
    ans = []
    for _ in range(m):
        cmd, a, b = map(int, input().split())

        if cmd == 0:
            union(a, b)
        else:
            if find(a) != find(b):
                ans.append("0")
            else:
                ans.append("1")

    print(f'#{tc} {"".join(ans)}')