import sys
input = sys.stdin.readline

while True:
    t = input().rstrip()

    if t == "0":
        break

    if t == t[::-1]:
        print("yes")
    else:
        print("no")