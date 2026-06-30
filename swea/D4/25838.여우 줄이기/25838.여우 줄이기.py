#????????????????
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    text = input().strip()

    #그냥 스택 담으면서 맨 뒤 3글자 'fox'면 지워
    stack = []
    for alpha in text:
        stack.append(alpha)
         
        if len(stack) >= 3:
            if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                for _ in range(3):
                    stack.pop()

    print(len(stack))