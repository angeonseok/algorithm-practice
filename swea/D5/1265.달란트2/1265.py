T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())

    #1묶음 당 개수
    a = n // p

    #나머지
    b = n % p

    #일단 a개씩 분배하고 b개 주머니에 1개씩 더해서 다 곱해버리기
    ans = a ** (p - b) * (a + 1) ** b

    print(f'#{tc} {ans}')