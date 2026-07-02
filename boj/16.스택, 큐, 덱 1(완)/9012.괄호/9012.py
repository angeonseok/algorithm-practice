#제거 가능 조건을 잘 따지자

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    stack.clear()
    ps = input().rstrip()
    
    #스택 제거 가능 유무 체크
    flag = True

    for i in range(len(ps)):
        if ps[i] == ')':
            
            #제거 가능시 제거, 아니면 동작 종료시키고 no
            if stack:
                stack.pop()
            else:
                flag = False
                break

        else:
            stack.append(ps[i])
    
    #ㅇㅇ
    if stack or not flag:
        print('NO')
    else:
        print('YES')