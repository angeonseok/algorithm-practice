import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    #얘는 왜 테케 밖에 넣었니
    visited = [False] * 10000
    q = deque()
    q.append((A, ""))
    visited[A] = True

    while q:
        num, cmd = q.popleft()

        #어떤 연산을 했는지 출력해야됨   
        if num == B:
            print(cmd)
            break
    
        D = (2 * num) % 10000
        if not visited[D]:
            visited[D] = True
            q.append((D, cmd + "D"))

        S = num - 1 if num != 0 else 9999
        if not visited[S]:
            visited[S] = True
            q.append((S, cmd + "S"))

        #이 식 얻을라고 손으로 좀 적었네
        L = (num % 1000) * 10 + (num // 1000)
        if not visited[L]:
            visited[L] = True
            q.append((L, cmd + "L"))

        #이 식 얻을라고 손으로 좀 적었네 2
        #L 기본 뼈대 복사해놓고 R로 안바꾸는건 뭔 기교지
        R = (num // 10) + (num % 10) * 1000
        if not visited[R]:
            visited[R] = True
            q.append((R, cmd + "R"))