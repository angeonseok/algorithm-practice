T = int(input())
for tc in range(1, T+1):
    n = int(input())
    text = input().strip()

    stack = []
    for i in text:

        #한줄로 때려박았다. 현재 글자가 x일 때 스택에서 2개 꺼내서 fox 되나? 체크한거다.
        if len(stack) >= 2 and i == 'x' and stack[-1] == 'o' and stack[-2] == 'f':
            stack.pop()
            stack.pop()
        else:
            stack.append(i)

    print(len(stack))