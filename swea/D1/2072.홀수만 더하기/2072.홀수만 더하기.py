T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = 0
    for i in arr:
        if i % 2 != 0:
            ans += i
    
    print(f"#{tc} {ans}")