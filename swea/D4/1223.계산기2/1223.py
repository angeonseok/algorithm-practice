for tc in range(1, 11):
    n = int(input())
    text = input().strip()

    #연산자 우선순위
    ops = {'+' : 1, '*' : 2}

    #부호 임시저장
    stack = []

    #후위순위 저장
    pf = []

    #후위식으로 표기 변환하자.
    for i in text:

        #숫자면 넣는다
        if i.isdigit():
            pf.append(i)

        else:
            #stack 맨 위 연산자가 현재 연산자보다 우선순위 높으면
            while stack and ops[stack[-1]] >= ops[i]:
                pf.append(stack.pop())
            stack.append(i)

    #안에 남은 애들 다 빼기
    while stack:
        pf.append(stack.pop())

    #연산을 하자.
    ans = []
    for k in pf:
        if k.isdigit():
            ans.append(int(k))
        else:
            a = ans.pop()
            b = ans.pop()
            c = b + a if k == '+' else b * a
            ans.append(c)

    print(f'#{tc} {ans[-1]}')