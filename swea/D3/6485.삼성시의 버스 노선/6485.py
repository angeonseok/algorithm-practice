T = int(input())
for tc in range(1, T+1):
    n = int(input())
    bus = [tuple((map(int, input().split()))) for _ in range(n)]
    p = int(input())
    arr = [int(input()) for _ in range(p)]

    ans = [0] * 5001

    #버스마다 골라서
    for a, b in bus:

        #버스가 가는 정류장 범위에 들간 놈들 다 1씩 더해주기
        for i in range(a, b+1):
            ans[i] += 1

    #ㅋㅋ 잘못봤네
    print(f'#{tc}', *[ans[i] for i in arr])