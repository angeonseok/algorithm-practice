import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))  #최소값나옴
        else:
            print(0)