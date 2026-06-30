from collections import deque

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    deck = input().split()
    
    ans = []
    #장수 기준으로 케이스 분류 후 재결합
    if n % 2 == 0:
        a = deque(deck[:n//2])
        b = deque(deck[n//2:])

        for i in range(n):
            if i % 2 == 0:
                ans.append(a.popleft())
            else:
                ans.append(b.popleft())
            
    else:
        a = deque(deck[:(n + 1) // 2])
        b = deque(deck[(n + 1) // 2:])

        for i in range(n):
            if i % 2 == 0:
                ans.append(a.popleft())
            else:
                ans.append(b.popleft())
    
    print(f'#{tc}', *ans)