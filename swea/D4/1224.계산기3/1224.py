for tc in range(1, 11):
    n = int(input())
    text = input().strip()

    #계산기2에서 괄호처리가 추가됨
    ops = {'(' : 0, '+' : 1, '*' : 2}
    stack = []
    pf = []

    for i in text:
        if i.isdigit():
            pf.append(i)

        #일단 괄호 쳐넣고
        elif i == '(':
            stack.append(i)

        #닫을 때는 괄호 사이에 모든 연산자를 다 꺼내서 집어넣고 괄호 제거
        elif i == ')':
            while stack and stack[-1] != '(':
                pf.append(stack.pop())
            stack.pop()

        #연산자 규칙은 뭐 그대로
        else:
            while stack and ops[stack[-1]] >= ops[i]:
                pf.append(stack.pop())
            stack.append(i)

    while stack:
        pf.append(stack.pop())

    ans = []
    for j in pf:
        if j.isdigit():
            ans.append(int(j))
        else:
            a = ans.pop()
            b = ans.pop()
            ans.append(b + a if j == '+' else b * a)

    print(f'#{tc} {ans[-1]}')