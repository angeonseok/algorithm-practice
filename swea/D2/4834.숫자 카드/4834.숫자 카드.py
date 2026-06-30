T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = input().strip()
    cnt = [0] * 10

    for i in arr:
        cnt[int(i)] += 1
    
    mx = max(cnt)
    ans = 0
    for i in range(10):
        if cnt[i] == mx:
            ans = i
    
    print(f"#{tc} {ans} {mx}")