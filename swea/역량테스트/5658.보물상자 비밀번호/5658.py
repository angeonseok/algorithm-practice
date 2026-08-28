#덱이 생각보다 많은걸 처리해준다.
from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    #회전을 위해 바로 덱에
    q = deque(input().strip())

    #사각형
    side = n // 4

    #중복 거르기
    password = set()

    #원래 상태로 돌아올 때까지 회전하면서 비번 쳐넣기
    for _ in range(side):
        #덱으로 하면 슬라이싱 불가능해서 바꿈
        arr = list(q)

        #한 변에 있는 애들이 비밀번호
        for i in range(0, n, side):
            #1. join과 슬라이싱을 통해 암호를 문자열로
            #2. 그 문자열을 int를 이용해 바로 16진수로 만들 수 있음
            pw = int("".join(arr[i: i + side]), 16)
            password.add(pw)

        #돌려
        q.rotate(1)

    #정렬을 위해서 변환
    password = list(password)
    password.sort()

    print(f'#{tc} {password[-k]}')