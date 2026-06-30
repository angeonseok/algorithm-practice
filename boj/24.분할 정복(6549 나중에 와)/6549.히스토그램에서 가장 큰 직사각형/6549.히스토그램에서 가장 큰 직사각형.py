#어 일단 스택으로 했어
#어 분할정복 아이디어 떠오르면 다시와
import sys

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break
    
    n = arr[0]
    stack = []
    ans = 0

    for i in range(1, n+1):
        start = i

        while stack and stack[-1][1] > arr[i]:
            a, val = stack.pop()
            start = a
            ans = max(ans, (val * (i - start)))
        
        stack.append((start, arr[i]))
    
    while stack:
        a, val = stack.pop()
        ans = max(ans, (val * (n - a + 1)))

    print(ans)