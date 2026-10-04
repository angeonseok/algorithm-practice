def kruskal(v, edges):
    parent = list(range(v+1))

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        
        return x


    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa == pb:
            return False
        
        parent[pa] = pb

        return True

    edges.sort()
    total = 0
    cnt = 0

    for w, a, b in edges:
        if union(a, b):
            total += w
            cnt += 1

            if cnt == v - 1:
                break

    return total


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    m = int(input())

    edges = []
    for _ in range(m):
        s, e, c = map(int, input().split())
        edges.append((c, s, e))

    ans = kruskal(n, edges)

    print(f'#{tc} {ans}')