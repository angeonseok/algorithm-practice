T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    #두 점의 거리를 미리 계산해두기
    diff = [abs(arr[i + 1] - arr[i]) for i in range(n - 1)]
    total = sum(diff)

    ans = float('inf')
    for i in range(1, n - 1):

        #종이로 적으니 이래 나왔네
        tmp = total - diff[i - 1] - diff[i] + abs(arr[i + 1] - arr[i - 1])
        ans = min(ans, tmp) 

    print(ans)