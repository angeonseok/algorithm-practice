T = int(input())
for tc in range(1, T+1):
    arr = input().split()

    stack = []
    for i in arr:

        #일단 숫자라면 스택에 넣는다
        if i.isdigit():
            stack.append(i)

        #연산자를 만났고 연산 가능(최소 숫자 2개 이상 있을 때)
        elif i in ('+', '-', '*', '/') and len(stack) >= 2:

            #순서 조심
            b = int(stack.pop())
            a = int(stack.pop())

            c = 0
            if i == '+':
                c = a + b

            if i == '-':
                c = a - b

            if i == '*':
                c = a * b

            if i == '/':
                c = a // b

            #다시 넣어
            stack.append(c)

        #끝났을 때 1개 있어야 출력됨
        elif i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')

            #없으면 에러지
            else:
                print(f'#{tc}', 'error')

        #연산 불가능한 경우라 다 에러임
        else:
            print(f'#{tc}', 'error')
            break