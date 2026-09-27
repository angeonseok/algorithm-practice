import heapq

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    heap = []
    for a in arr:
        heapq.heappush(heap, a)

    #인덱스 맞춰주기
    m = n - 1
    ans = 0
    while m > 0:
        m = (m - 1)// 2
        ans += heap[m]

    print(f'#{tc} {ans}')