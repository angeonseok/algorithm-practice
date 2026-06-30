month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    #걍 첫날 기준 지난 날을 계산해서
    day1 = sum(month[:m1]) + d1
    day2 = sum(month[:m2]) + d2

    #서로 뺴
    diff = day2 - day1 + 1
    print(f"#{tc} {diff}")