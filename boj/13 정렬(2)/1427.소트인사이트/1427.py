import sys
input = sys.stdin.readline

n = str(input().rstrip())       #입력이 2143 이런식으로 붙어서 들어옴
a = []

for i in n:                     #설명할 게 있나?
    a.append(i)

a.sort(reverse=True)

print("".join(a))
