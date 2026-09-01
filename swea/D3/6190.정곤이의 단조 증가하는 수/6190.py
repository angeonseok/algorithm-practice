def mono(num):
    num = str(num)

    #지금 위치 수가 다음 친구보다 크면 걍 빠꾸시켜
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False

    return True


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    #문제를 잘 읽자
    ans = -1

    #뭐 다 해도 안터지겠네
    for i in range(n - 1):
        for j in range(i + 1, n):
            k = arr[i] * arr[j]

            #단조 증가하는 수인 경우에만 정답 갱신
            if k > ans and mono(k):
                ans = k

    print(f'#{tc} {ans}')