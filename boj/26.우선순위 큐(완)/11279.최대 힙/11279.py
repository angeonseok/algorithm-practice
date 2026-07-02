import sys
import heapq      #기본적으로 최소 힙 지원
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, -x)    #최대 힙처럼 하려면 음수를 넣어
    else:
        if heap:
            print(-heapq.heappop(heap)) #최솟값의 음수 > 최댓값됨
        
        else:
            print(0)