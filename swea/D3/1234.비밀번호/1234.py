for tc in range(1, 11):
    n, text = input().split()

    stack  = []
    for i in text:

        #같으면 빼
        if stack and stack[-1] == i:
            stack.pop()

        #아님 넣어놔
        else:   
            stack.append(i)

    print(f'#{tc}', "".join(stack))