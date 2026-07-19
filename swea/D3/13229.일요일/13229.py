table = {
    "MON" : 1,
    "TUE" : 2,
    "WED" : 3,
    "THU" : 4,
    "FRI" : 5,
    "SAT" : 6,
    "SUN" : 7
}

T = int(input())
for tc in range(1, T+1):
    day = input().rstrip()

    ans = 7 if day == 'SUN' else 7 - table[day]
    print(f'#{tc} {ans}')