T = int(input())
for tc in range(1, T+1):
    cmd = input()

    a, b = 1, 1
    for i in cmd:
        if i == 'L':
            b += a
        else:
            a += b
    
    print(f'#{tc} {a} {b}')