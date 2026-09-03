T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    #매 위치마다 체크하면서 ? 애들을 한데 몰아버리면 된다.
    qm = 0
    ans = 0
    now = 0
    for i in text:
        if i == 'R':
            now += 1

        elif i == 'L':
            now -= 1

        else:
            qm += 1

        ans = max(ans, abs(now) + qm)

    #완탐하면 시간터짐 십
    print(ans)