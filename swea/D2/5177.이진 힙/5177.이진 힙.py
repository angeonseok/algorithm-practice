import heapq

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    idx = n - 1
    ans = 0

    while idx > 0:
        idx = (idx - 1) // 2
        ans += heap[idx]

    print(f"#{tc} {ans}")