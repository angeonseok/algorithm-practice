from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    #중요도와 문서 번호를 같이 저장
    q = deque([(arr[i], i) for i in range(n)])

    cnt = 0

    while q:
        a = q.popleft()

        #큐가 빈 경우는 생각안하다가 신나게 날려버린 모습
        if q and a[0] < max(x[0] for x in q):
            q.append(a)
        else:
            cnt += 1
            if a[1] == m:   #원하는 문서가 나오면 끝
                print(cnt)
                break