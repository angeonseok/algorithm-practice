import sys
input = sys.stdin.readline

n = int(input())
sets = 0

#비트마스킹 맛을 보자
for _ in range(n):
    cmd = input().split()

    #or 연산으로 원하는 위치 비트 켜기
    if cmd[0] == "add":
        sets |= (1<<int(cmd[1]))

    # and + not으로 지우기
    if cmd[0] == "remove":
        sets &= ~(1<<int(cmd[1]))

    # and 연산으로 확인
    if cmd[0] == "check":
        if sets & (1<<int(cmd[1])):
            print(1)
        else:
            print(0)

    #xor 연산으로 토글
    if cmd[0] == "toggle":
        sets ^= (1<<int(cmd[1]))
    
    #최대길이 + 1 비트 키고 -1
    if cmd[0] == "all":
        sets = (1<<21) - 1
    
    #0으로 비트 초기화
    if cmd[0] == "empty":
        sets = 0