T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = max(arr) + 1
    s = sum(arr)
    while(True):
        if (s + ans) % 7 == 0:
            break
        ans += 1

    print(ans)  