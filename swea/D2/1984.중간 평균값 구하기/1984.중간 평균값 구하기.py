T = int(input())
for tc in range(1, T+1):
    arr = sorted(list(map(int, input().split())))

    sum_num = sum(arr) - max(arr) - min(arr)
    print(f"#{tc} {round(sum_num / 8)}")