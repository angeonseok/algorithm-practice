import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
stack = []

#순번이 맞다면 그냥 보내고, 아니면 잠시 스택에 저장
cnt = 1
for i in line:
    if cnt == i:
        cnt += 1
    else:
        stack.append(i)

    #저장 후 스택의 상태를 계속 체크하고 꺼내기
    while stack and stack[-1] == cnt:
            stack.pop()
            cnt += 1

if cnt == n + 1:
    print('Nice')
else:
    print('Sad')