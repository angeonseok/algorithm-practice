import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = []
a = 1

for i in arr:

    #i 나올때까지 넣어
    while a <= i:
        stack.append(a)
        ans.append("+")
        a += 1
    
    #맨 위가 i면 꺼내
    if stack and stack[-1] == i:
        stack.pop()
        ans.append("-")

    #아니면 불가능
    else:
        print("NO")
        break

else:
    print('\n'.join(ans))