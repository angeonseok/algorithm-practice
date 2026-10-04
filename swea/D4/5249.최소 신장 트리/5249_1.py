def kruskal(v, edges):
    parent = list(range(v + 1))

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

            if cnt == v:
                break

    return total


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    edges = []
    for _ in range(e):
        s, e, w = map(int, input().split())
        edges.append((w, s, e))

    ans = kruskal(v, edges)

    print(f'#{tc} {ans}')