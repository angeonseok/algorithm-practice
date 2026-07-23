T = int(input())
for tc in range(1, T+1):
    text = sorted(input().strip())

    stack = []
    for i in text:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    ans = ""
    if not stack:
        ans = "Good"
    else:
        ans = "".join(stack)

    print(f'#{tc} {ans}')