T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    #걍 정렬하고 시작하자
    arr.sort()

    ans = float('inf')

    #묶음 안의 최대와 최소만 생각해서 계산하면 될 듯
    for i in range(n - k + 1):
        ans = min(ans, arr[i + k - 1] - arr[i])

    print(f'#{tc} {ans}')