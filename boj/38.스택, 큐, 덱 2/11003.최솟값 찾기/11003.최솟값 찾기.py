import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
for i in range(n):

    #넣을 때 덱 맨 뒤 값이 지금 값보다 크면 그거 제거 
    while q and q[-1] > arr[i]:
        q.pop()
    q.append(arr[i])

    #구간 범위 벗어나면 앞에서 제거
    if i >= l and q[0] == arr[i-l]:
        q.popleft()
    
    #맨 앞놈이 최소값임
    print(q[0], end = " ")