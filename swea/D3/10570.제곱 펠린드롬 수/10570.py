def pal(num):
    s_num = str(num)
    return s_num == s_num[::-1]

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    cnt = 0
    for i in range(int((a - 1) ** 0.5 + 1), int(b ** 0.5) + 1):
        if pal(i) and pal(i * i):
                cnt += 1
    
    print(f'#{tc} {cnt}')