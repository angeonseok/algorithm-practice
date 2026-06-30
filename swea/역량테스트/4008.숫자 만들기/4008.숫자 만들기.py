def cal_num(cnt, total, op1, op2, op3, op4):
    global max_num, min_num

    if cnt == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return 
    
    if op1 > 0:
        cal_num(cnt + 1, total + nums[cnt], op1 - 1, op2, op3, op4)
    
    if op2 > 0:
        cal_num(cnt + 1, total - nums[cnt], op1, op2 - 1, op3, op4)
    
    if op3 > 0:
        cal_num(cnt + 1, total * nums[cnt], op1, op2, op3 - 1, op4)
    
    #나눗셈이 문제다 항상
    if op4 > 0:
        cal_num(cnt + 1, int(total / nums[cnt]), op1, op2, op3, op4 - 1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_num = -10e9
    min_num = 10e9

    cal_num(1, nums[0], ops[0], ops[1], ops[2], ops[3])

    print(f"#{tc} {max_num - min_num}")