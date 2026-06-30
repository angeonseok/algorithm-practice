import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = int(input().rstrip())
    p = [0] * (a + 1)

    #dp초기값 설정에 주의하자
    if a >= 1:
        p[1] = 1
    
    if a >= 2:
        p[2] = 1
    
    if a >= 3:
        p[3] = 1
    
    if a >= 4:
        p[4] = 2
    
    if a >= 5:
        p[5] = 2

    for i in range(6, a+1):
        p[i] = p[i-1] + p[i-5]
    
    print(p[a])