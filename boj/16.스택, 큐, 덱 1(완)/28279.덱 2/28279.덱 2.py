import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n = int(input())

for _ in range(n):
    a = input().split()

    if int(a[0]) == 1:
        queue.appendleft(int(a[1]))
    
    elif int(a[0]) == 2:
        queue.append(int(a[1]))
    
    elif int(a[0]) == 3:
        if queue:
            print(int(queue.popleft()))
        else:
            print(-1)
    
    elif int(a[0]) == 4:
        if queue :
            print((queue.pop()))
        else:
            print(-1)

    elif int(a[0]) == 5:
        print(len(queue))

    elif int(a[0]) == 6:
        if queue : 
            print(0)
        else:
            print(1)

    elif int(a[0]) == 7:
        if queue : 
            print(queue[0])
        else:
            print(-1)

    elif int(a[0]) == 8:
        if queue :
            print(queue[-1])
        else:
            print(-1)