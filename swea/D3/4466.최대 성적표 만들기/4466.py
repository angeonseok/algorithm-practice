T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    ans = 0
    for i in range(k):
        ans += arr[i]

    print(f'#{tc} {ans}')