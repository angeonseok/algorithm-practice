#부모 찾기
def find(x):
    if x != parents[x]:
        x = find(parents[x])
    return parents[x]


#합치기
def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parents[pa] = pb


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    parents = list(range(n + 1))

    for i in range(0, len(arr), 2):
        a = arr[i]
        b = arr[i + 1]
        union(a, b)

    ans = 0
    #루트 개수가 정답임
    for i in range(1, n + 1):
        if i == find(i):
            ans += 1
    
    print(f'#{tc} {ans}')