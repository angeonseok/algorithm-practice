def find(x):
    if x != parent[x]:
        x = find(parent[x])
    return parent[x]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    parent = list(range(n + 1))

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    #루트 개수가 정답
    ans = set()
    for i in range(1, n + 1):
        ans.add(find(i))

    print(f'#{tc} {len(ans)}')