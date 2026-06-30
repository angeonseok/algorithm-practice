import sys
input = sys.stdin.readline

num = 1
for _ in range(3):
    a = int(input().rstrip())
    num *= a

cnt = [0] * 10
for i in str(num):
    cnt[(int(i))] += 1

for j in cnt:
    print(j)