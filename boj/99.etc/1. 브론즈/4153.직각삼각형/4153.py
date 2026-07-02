import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    temp = a ** 2 + b ** 2 + c ** 2
    s = 2 * max(a, b, c) ** 2

    if temp - s == 0:
        print("right")
    else:
        print("wrong")