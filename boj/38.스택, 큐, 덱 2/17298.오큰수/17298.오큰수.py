import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#일단 -1로 깔아
ans = [-1] * n

#인덱스 저장용
stack = []

for i in range(n):

    # 현재 값이 더 크면 스택에서 꺼내면서 정답 채움
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    
    #아직 처리 안된 인덱스 스택에 넣어
    stack.append(i)
    
print(*ans)