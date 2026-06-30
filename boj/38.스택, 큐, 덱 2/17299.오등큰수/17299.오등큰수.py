import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#등장횟수 저장용 배열(딕셔너리로 하면 더 괜찮을듯)
cnt = [0] * (max(arr) + 1)
for i in arr:
    cnt[i] += 1

#오큰수와 같은 방식으로 할거다
ans = [-1] * n
stack = []

for i in range(n):

    #현재 값의 등장 횟수가 더 크다면 스택에서 꺼내서 정답 채워넣음
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        ans[stack.pop()] = arr[i]
    
    stack.append(i)

print(*ans)