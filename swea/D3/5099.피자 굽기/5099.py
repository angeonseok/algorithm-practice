from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    #순서와 치즈량 묶어서 저장
    lst = deque()
    for i, c in enumerate(arr):
        lst.append((i+1, c))

    #화덕 죠뻉이용
    q = deque()
    for _ in range(n):
        q.append(lst.popleft())

    #죠뺑이
    while len(q) != 1:
        idx, a = q.popleft()
        a //= 2

        #append 자체가 회전까지 해줌
        if a != 0:
            q.append((idx, a))

        elif lst:
            q.append(lst.popleft())

    print(f'#{tc} {q[0][0]}')