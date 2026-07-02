T = int(input())
for tc in range(1, T + 1):
    date = input()
    y, m, d = date[:4], int(date[4:6]), int(date[6:])

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= m <= 12 and 1 <= d <= days[m]:
        print(f'#{tc} {y}/{date[4:6]}/{date[6:]}')
    else:
        print(f'#{tc} -1')