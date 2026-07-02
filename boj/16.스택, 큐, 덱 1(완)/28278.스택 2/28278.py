import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num = input().split()
    
    #입력키는 int형, 지금 기준으로는 배열로 생성 되니 젤 처음인 0번
    a = int(num[0])
    
    #커맨드 이후 숫자 저장
    if a == 1:
        stack.append(num[1])
    
    #제일 나중에 들어온 수 제거하면서 출력, 비어있다면 -1
    elif a == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    #스택 내 요소 수
    elif a == 3:
        print(len(stack))
    
    #스택이 비어있으면 1 아니면 0
    elif a == 4:
        print(1 if not stack else 0)
    
    #스택에 정수가 있으면 맨 위 정수, 비어있다면 -1
    elif a == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)