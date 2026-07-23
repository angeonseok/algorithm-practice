T = int(input())
for tc in range(1, T+1):
    a = input().strip()
    b = input().strip()

    if a + 'a' == b:
        print(f'#{tc} N')
    else:
        print(f'#{tc} Y')