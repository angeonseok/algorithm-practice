import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    a = int(input().rstrip())
    
    #0들가면 최근꺼 지우고 아님 저장
    if a == 0 :
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))