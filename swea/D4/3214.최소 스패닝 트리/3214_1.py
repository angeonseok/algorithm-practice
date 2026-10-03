def kruskal(v, edge):
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


    edge.sort()
    total = 0
    cnt = 0

    for w, a, b in edge:
        if union(a, b):
            total += w
            cnt += 1

            if cnt == v - 1:
                break

    return total


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())

    edge = []
    for _ in range(e):
        a, b, w = map(int, input().split())
        edge.append((w, a, b))

    ans = kruskal(v, edge)
    print(f'#{tc} {ans}')