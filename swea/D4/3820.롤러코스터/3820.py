MOD = 1000000007


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])

    #정렬 조건 b / (a - 1) 작은 순으로, 만약 a = 1이면 뒤로 보내버려
    arr.sort(key=lambda x: x[1] / (x[0] - 1) if x[0] != 1 else float('inf'))

    ans = 1
    for a, b in arr:
        ans = (a * ans + b) % MOD

    print(f'#{tc} {ans % MOD}')