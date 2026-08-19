T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    stack = []
    flag = True
    for i in text:
        if i in ('(', '{'):
            stack.append(i)

        elif i in (')', '}'):
            if stack and ((stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}')):
                stack.pop()
            else:
                flag = False
                break

    ans = 1 if flag and not stack else 0

    print(f'#{tc} {ans}')