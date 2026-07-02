import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int,input().split()))
    for i in a:
        heapq.heappush(heap, i)
        
        #힙의 길이 자체를 n으로 제한
        if len(heap) > n:
            heapq.heappop(heap)

#n번쨰 큰 수 : heap 중 최소값
print(heap[0])