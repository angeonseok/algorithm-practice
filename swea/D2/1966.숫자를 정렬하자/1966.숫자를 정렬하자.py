T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    ans = ""
    for i in arr:
        ans += str(i) + " "
    
    print(f"#{tc} {ans}")
