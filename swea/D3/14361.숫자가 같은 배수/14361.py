T = int(input())
for tc in range(1, T+1):
    nums = input().strip()
    num = int(nums)

    flag = False

    #직접 들어있는 문자 비교할거다.
    digit = sorted(nums)
    for i in range(2, 10):
        mul_num = num * i
        tmp = sorted(str(mul_num))

        if tmp == digit:
            flag = True
            break

    ans = "impossible" if not flag else "possible"
    print(f'#{tc} {ans}')