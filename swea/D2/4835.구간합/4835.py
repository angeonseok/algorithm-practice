T = int(input())
for tc in range(1 ,T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = [0] * (n - m + 1)
    for i in range(n - m + 1):
        for j in range(m):
            prefix[i] += arr[i + j]

    print(f'#{tc} {max(prefix) - min(prefix)}')