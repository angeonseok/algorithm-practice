T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    for i in range(len(text) // 2):
        a, b = text[i], text[len(text) - i - 1]

        if a != '?' and b != '?' and a != b:
            print(f'#{tc} Not exist')
            break

    else:
        print(f'#{tc} Exist')