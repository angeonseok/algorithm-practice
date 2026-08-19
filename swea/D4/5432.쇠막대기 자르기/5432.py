T = int(input())
for tc in range(1, T+1):
    line = input()

    #총 개수 / 막대 수
    ans = 0
    cnt = 0

    #함 가보자
    for i in range(len(line)):

        #막댄지 아닌지 몰라 일단 개수 더해
        if line[i] == '(':
            cnt += 1

        #일단 막대 수 늘리지 말고 생각해보자. 레이저인지 끝인지 판별해야한다.
        else:
            cnt -= 1

            #레이저다. 막대수만큼 더해라
            if line[i] == ')' and line[i - 1] == '(':
                ans += cnt

            #막대 한 놈 끝자락이 맞다. 1조각 더 나온다 
            else:
                ans += 1

    print(f'#{tc} {ans}')