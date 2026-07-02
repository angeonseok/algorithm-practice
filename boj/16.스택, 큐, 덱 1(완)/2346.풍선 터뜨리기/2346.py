import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#순서 없이 만드니 순번 저장을 못하네
queue = deque(enumerate(map(int,input().split()), start=1))

ans = []
while queue:
    a = queue.popleft()
    ans.append(a[0])
    
    #지운 수가 음수냐 양수냐 따라 동작이 다름
    if a[1] > 0:
        for _ in range(a[1]-1):
            queue.rotate(-1)        #양수면 <<<<
    
    if a[1] < 0:
        for _ in range(-a[1]):
            queue.rotate(1)         #음수면 >>>>

print(*ans)