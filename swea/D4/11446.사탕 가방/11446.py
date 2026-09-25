#k개 가방 만들 때, 한 가방 당 m개 이상 되는가 
def ok(k):
    s = 0
    for i in arr:
        s += i // k

        if s >= m:
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    lo, hi = 0, sum(arr) // m

    #최소가 0이라 올려줘야됨
    while lo < hi:
        mid = (lo + hi + 1) // 2

        if ok(mid):
            lo = mid

        else:
            hi = mid - 1

    print(f'#{tc} {lo}')