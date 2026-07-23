T = int(input())
for tc in range(1, T+1):
    tmp = [list(input()) for _ in range(5)]
    max_l = max(len(row) for row in tmp)

    arr = [row + [""] * (max_l - len(row)) for row in tmp]

    ans = ""
    for i in range(max_l):
        for j in range(5):
            if not arr[j][i]:
                continue

            ans += arr[j][i]
    
    print(f'#{tc} {ans}')