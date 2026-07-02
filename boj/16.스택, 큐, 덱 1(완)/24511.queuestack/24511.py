import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input().rstrip())
C = list(map(int,input().split()))

#스택부분은 의미가 없음. 하나의 큐 처럼 작동함. 궁금하면 종이로 해라. 바로 안다.

#초기 입력값을 왼쪽이 최신인 순으로 받기
queuestack = deque()
for i in range(N):
    if A[i] == 0:
        queuestack.appendleft(B[i])

#그럼 입력 그대로 받고 앞에서부터 지우기 좋지
for j in range(M):
    queuestack.append(C[j])
    print(queuestack.popleft(),end = " ")