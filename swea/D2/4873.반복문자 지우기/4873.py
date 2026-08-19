T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    stack = []
    for i in text:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')