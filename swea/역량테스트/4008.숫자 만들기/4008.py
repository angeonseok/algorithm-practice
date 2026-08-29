def make_num(cur, total, op1, op2, op3, op4):
    global max_num, min_num

    #모든 숫자 사용하면 결과 업데이트
    if cur == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    #덧셈
    if op1 > 0:
        make_num(cur + 1, total + nums[cur], op1 - 1, op2, op3, op4)

    #뺄셈
    if op2 > 0:
        make_num(cur + 1, total - nums[cur], op1, op2 - 1, op3, op4)

    #곱셈
    if op3 > 0:
        make_num(cur + 1, total * nums[cur], op1, op2, op3 - 1, op4)

    #나눗셈
    if op4 > 0:
        make_num(cur + 1, int(total / nums[cur]), op1, op2, op3, op4 - 1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_num = -10e9
    min_num = 10e9

    make_num(1, nums[0], ops[0], ops[1], ops[2], ops[3])
    print(f'#{tc} {max_num - min_num}')