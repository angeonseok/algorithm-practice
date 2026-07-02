import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_num = 10e9
max_num = -10e9

def cal_max_min(cal_cnt, total, op1, op2, op3, op4):
    global min_num, max_num

    #지금까지 사용한 수가 n개면 결과에 반영
    if cal_cnt == n:
        min_num = min(min_num, total)
        max_num = max(max_num, total)
        return

    #연산자가 남아있을 때만 사용 가능
    if op1 > 0:
        cal_max_min(cal_cnt + 1, total + nums[cal_cnt], op1 - 1, op2, op3, op4)
    
    if op2 > 0:
        cal_max_min(cal_cnt + 1, total - nums[cal_cnt], op1, op2 - 1, op3, op4)
    
    if op3 > 0:
        cal_max_min(cal_cnt + 1, total * nums[cal_cnt], op1, op2, op3 - 1, op4)
    
    if op4 > 0:
        cal_max_min(cal_cnt + 1, total // nums[cal_cnt], op1, op2, op3, op4 - 1)

#num[0]을 total로 깔고 다음 숫자부터 연산
cal_max_min(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_num)
print(min_num)