T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = []
    for i in range(n - m + 1):
        s = 0
        for j in range(m):
            s += arr[i + j]
        prefix.append(s)

    ans = max(prefix) - min(prefix)
    print(f"#{tc} {ans}")