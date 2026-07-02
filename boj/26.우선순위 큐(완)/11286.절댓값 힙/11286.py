import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap=[]

for _ in range(n):
    x = int(input())
    
    #절댓값기준 정렬
    if x != 0:
       heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            abs_num, num = heapq.heappop(heap)  #이래 꺼내는거 맞나
            print(num)
        else:
            print(0)