#사실상 9012 강화문제

import sys
input = sys.stdin.readline

while 1:
    a = input().rstrip()
    stack = []

    #while 종료조건
    if a == ".":
        break
    
    #체크
    flag = True

    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        
        #바로 짝으로 안지워지면 실패
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            
            else:
                flag = False
                break
        
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            
            else:
                flag = False
                break
        
    if stack or not flag:
        print('no')
    else:
        print('yes')