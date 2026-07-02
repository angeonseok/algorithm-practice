import sys
input = sys.stdin.readline

s = input().strip()

#주어진 문자열을 "-" 기준으로 쪼개기
cut = s.split("-")

#쪼개진 문자열을 정수형으로 변환 후 합을 구하는 함수
def part_sum(string):
    sum = 0
    part = list(map(int, string.split("+")))
    for num in part:
        sum += num
    return sum

#"-"가 나오기 전까지의 합
ans = part_sum(cut[0])

#"-" 이후 다음 "-" 이전까지의  수를 합해서 빼면 됨
for i in range(1, len(cut)):
    a = part_sum(cut[i])
    ans -= a

print(ans)