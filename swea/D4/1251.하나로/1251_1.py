#이 문제는 프림 풀이가 맞다. 괜히 이거로 하지마라.
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
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    edge = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            edge.append((dx ** 2 + dy ** 2, i, j))

    total = kruskal(n, edge)
    print(f'#{tc} {round(total * e)}')