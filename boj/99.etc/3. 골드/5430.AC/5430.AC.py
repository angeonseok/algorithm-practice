import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    
    #대괄호만 벗겨 받기
    arr = input().strip()[1:-1]

    #빈 배열인지 아닌지 나눠서 변환
    if len(arr) == 0:
        q = deque()
    else:
        q = deque(map(int, arr.split(',')))

    #reverse를 직접하면 터질 것 같아서 xor로 관리
    r = 0

    #에러나면 마지막 출력 스킵
    flag = False

    for cmd in p:
        if cmd == "R":
            r ^= 1
        
        else:
            if len(q) == 0:
                print('error')
                flag = True
                break

            else:
                if r == 0:
                    q.popleft()
                else:
                    q.pop()

    if not flag:
        if r == 1:
            q.reverse()

        print('[' + ','.join(map(str, q)) + ']')