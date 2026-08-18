from collections import deque

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    #걍 덱을 쓰고싶었음.
    arr = deque(sorted(list(map(int, input().split()))))

    ans = []
    while(arr):
        ans.append(arr.pop())

        #홀수 방지용
        if arr:
            ans.append(arr.popleft())

    #출력 맞추기
    print(f'#{tc}', *ans[:10])