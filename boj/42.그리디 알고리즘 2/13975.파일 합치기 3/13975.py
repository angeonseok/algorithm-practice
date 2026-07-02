import sys
import heapq
input = sys.stdin.readline

# 매번 가장 작은 2개를 꺼내서 합쳐야 되니까 힙 씀
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)

    # 합치는 비용 누적
    ans = 0

    # 파일이 1개 남을 때까지 계속 제일 작은 2개 합치기
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        # 이번에 합친 비용
        c = a + b

        # 합친 파일도 다시 후보라서 힙에 넣어야 됨
        heapq.heappush(arr, c)

        # 매번 합칠 때 든 비용 전부 더한 게 정답
        ans += c
    
    print(ans)