T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    sum_arr = 0
    for i in arr:
        sum_arr += i
    
    ans = sum_arr / 10
    print(f"#{tc} {ans:.0f}")