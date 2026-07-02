import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

#보석의 무게와 가치 저장
info = []
for _ in range(n):
    a, b = map(int, input().split())
    info.append((a,b))

#k개의 가방 수용가능 무게 저장
bag = []
for _ in range(k):
    c = int(input())
    bag.append(c)

#정렬
info.sort()
bag.sort()

heap = []
ans = 0
idx = 0

#작은 가방부터
for i in bag:
    
    #보석들 중 가방의 수용가능 무게보다 크지 않은 보석들을 찾고
    while idx < len(info) and info[idx][0] <= i:
        #보석의 가치를 최대 힙에 저장
        heapq.heappush(heap, -info[idx][1])
        idx += 1

    #가방 하나에 최대 가치 보석 하나씩 넣어서 합하기
    if heap:
        ans += -heapq.heappop(heap)

print(ans)