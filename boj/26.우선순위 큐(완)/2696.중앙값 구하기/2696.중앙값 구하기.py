import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    #입력 양식이 10개씩 들어온다
    arr = []
    r = n
    while r > 0:
        line = list(map(int,input().split()))
        arr.extend(line)
        r -= len(line)

    #중앙값 기준 더 큰 놈을 min에, 중앙값 포함해서 작은 놈은 max에
    max_heap = []
    min_heap = []

    ans = []
    
    #길이가 같은 경우 max heap에 우선 넣기
    for i in range(n):
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -arr[i])
        else:
            heapq.heappush(min_heap, arr[i])

        #넣은 후 조건 맞추기(중앙값은 max heap에 들어갈 수 있도록)
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        #순서기준 홀수번쨰 마다 중앙값 추출
        if i % 2  == 0:
            ans.append(-max_heap[0])

    #출력양식도 이상해오
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i:i+10])