#분기 나누기도 귀찮다
combine = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<',
}

for tc in range(1, 11):
    input()
    text = input().strip()

    stack = []
    ans = 1
    for i in text:
        #일단 괄호 짝짓기 되게 넣어놔라
        if i in '([{<':
            stack.append(i)

        #내용물 있고 매칭시키기
        elif stack and stack[-1] == combine[i]:
            stack.pop()

        #그 외에 경우는 전부 안되는 경우라 ㄱㅊ
        else:
            ans = 0
            break

    print(f'#{tc} {ans}')