T = int(input())
for tc in range(1, T+1):
    n = input().strip()

    #숫자조합 저장용.
    comb = []

    #자기 자신도 넣어둬야지
    comb.append(int(n))

    #개노가다
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            #복사해서 사용
            arr = list(n)

            #맨 앞자리랑 숫자 0이랑 바뀌는거 막기
            if i < 1 and arr[j] == '0':
                continue

            #ㅇㅇ
            arr[i], arr[j] = arr[j], arr[i]
            comb.append(int("".join(arr)))

    print(f'#{tc} {min(comb)} {max(comb)}')