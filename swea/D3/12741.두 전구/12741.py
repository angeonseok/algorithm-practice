T = int(input())
for tc in range(1, T+1):
    x_start, x_end, y_start, y_end = map(int, input().split())

    time = [0] * 101
    for i in range(x_start, x_end):
        time[i] += 1
    
    for i in range(y_start, y_end):
        time[i] += 1

    ans = time.count(2)
    print(f'#{tc} {ans}')