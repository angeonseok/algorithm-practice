arr = list(map(str, input().strip()))
for i in arr:
    print(ord(i) - 64, end = " ")